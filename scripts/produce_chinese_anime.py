#!/usr/bin/env python3
"""
Chinese anime audio production — parses Chinese anime draft JSONs,
maps Chinese character names to voice palette entries, generates
TTS via edge_tts with Chinese voices, and concatenates into final
episode audio with ID3 metadata.

Usage:
    python3 produce_chinese_anime.py
"""

import asyncio
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import edge_tts
from pydub import AudioSegment

# ── Paths ─────────────────────────────────────────────────────
PROJECT_DIR = Path.home() / ".hermes" / "projects" / "sheherazades-lantern"
VOICE_PALETTE_PATH = PROJECT_DIR / "voice_palette.json"
DRAFTS_DIR = PROJECT_DIR / "content" / "drafts"
OUTPUT_DIR = PROJECT_DIR / "audio" / "episodes"

# ── Load voice palette ────────────────────────────────────────
with open(VOICE_PALETTE_PATH, encoding="utf-8") as f:
    palette = json.load(f)

# ── Chinese character name → character id mapping ────────────
CHINESE_CHAR_MAP = {
    "提灯人": "lantern_keeper",
    "月芽": "yueya",
    "卡里姆": "karim",
    "拉希德": "rashid",
    "纳迪亚": "nadia",
    "哈立德": "khalid",
    "杜妮亚扎德": "dunyazad",
    "莱拉": "layla",
}

# Lantern Keeper default Chinese voice + base_rate
LK_ZH_VOICE = palette["lantern_keeper"]["voices"]["zh"]["voice"]
LK_ZH_RATE = palette["lantern_keeper"]["voices"]["zh"]["base_rate"]


def get_voice_zh(char_id: str) -> str:
    """Get Chinese voice for a character ID from the palette."""
    if char_id not in palette:
        return "zh-CN-XiaoxiaoNeural"
    char = palette[char_id]
    voices = char.get("voices", {})
    if "zh" in voices:
        return voices["zh"]["voice"]
    # fallback: try "en" as last resort
    if "en" in voices:
        return voices["en"]["voice"]
    return "zh-CN-XiaoxiaoNeural"


def get_base_rate_zh(char_id: str) -> str:
    """Get Chinese base_rate for a character ID from the palette.
    Uses base_rate only — no emotion rate modulation per task spec."""
    if char_id not in palette:
        return "+0%"
    char = palette[char_id]
    voices = char.get("voices", {})
    if "zh" in voices:
        return voices["zh"].get("base_rate", "+0%")
    return "+0%"


def parse_chinese_anime_script(story_text: str):
    """Parse Chinese anime-format script into TTS segments.

    Format:
      —— 场景 N：地点 — 时间 ——   → scene marker
      CHARACTER_NAME：              → character dialogue start
      （stage directions）         → skipped
      blank lines                  → flush current speaker

    Returns list of (text, voice_name, seg_type) tuples.
    """
    lines = story_text.strip().split("\n")
    segments: list = []

    current_char_id = None
    current_voice_name = LK_ZH_VOICE
    current_rate = LK_ZH_RATE
    dialogue_buffer: list[str] = []

    scene_marker_re = re.compile(r"^——\s*场景\s+\d+\s*[：:]\s*.*?——\s*$")
    alt_scene_re = re.compile(r"^——\s+.+?——\s*$")  # fallback: any —— marker

    def is_scene_marker(line: str) -> bool:
        return bool(scene_marker_re.match(line) or alt_scene_re.match(line))

    def flush_dialogue():
        nonlocal dialogue_buffer, current_char_id, current_voice_name, current_rate
        if not dialogue_buffer:
            return
        full_text = " ".join(dialogue_buffer).strip()
        if full_text and len(full_text) >= 2:
            segments.append((full_text, current_voice_name, current_rate))
        dialogue_buffer = []

    for line in lines:
        stripped = line.strip()

        # ── Scene marker ────────────────────────────────────
        if is_scene_marker(stripped):
            flush_dialogue()
            # Extract scene label for narration (voice over)
            scene_label = stripped.strip("— ")
            if scene_label:
                # Narrate scene title with Lantern Keeper voice, slower
                segments.append((scene_label, LK_ZH_VOICE, LK_ZH_RATE))
            current_char_id = None
            current_voice_name = LK_ZH_VOICE
            current_rate = LK_ZH_RATE
            continue

        # ── Blank line → flush (only reset char if buffered) ─
        if not stripped:
            had_dialogue = bool(dialogue_buffer)
            flush_dialogue()
            if had_dialogue:
                current_char_id = None
                current_voice_name = LK_ZH_VOICE
                current_rate = LK_ZH_RATE
            # If buffer was empty, preserve current character for continuation
            continue

        # ── Stage direction on its own line → skip ──────────
        if re.match(r"^[（(][^）)]*[）)]$", stripped):
            continue

        # ── Chinese character name tag —————————————————————
        # Pattern: ChineseName：text   or   ChineseName (tone)：text
        char_tag_re = re.compile(
            r"^(" + "|".join(re.escape(name) for name in CHINESE_CHAR_MAP) + r")"
            r"(?:\s*[（(][^）)]*[）)])?\s*[：:]\s*(.*)"
        )
        char_match = char_tag_re.match(stripped)
        if char_match:
            flush_dialogue()
            chinese_name = char_match.group(1).strip()
            after_colon = char_match.group(2).strip()
            char_id = CHINESE_CHAR_MAP.get(chinese_name, None)

            if char_id:
                current_char_id = char_id
                current_voice_name = get_voice_zh(char_id)
                current_rate = get_base_rate_zh(char_id)
            else:
                current_char_id = None
                current_voice_name = LK_ZH_VOICE
                current_rate = LK_ZH_RATE

            # If there's dialogue after the colon, buffer it
            if after_colon and len(after_colon) >= 2:
                dialogue_buffer.append(after_colon)
            continue

        # ── Everything else → dialogue or narration ─────────
        if current_char_id:
            dialogue_buffer.append(stripped)
        else:
            # LK narration without explicit tag
            flush_dialogue()
            cleaned = re.sub(r"[（(][^）)]*[）)]", "", stripped).strip()
            if cleaned and len(cleaned) >= 2:
                segments.append((cleaned, LK_ZH_VOICE, LK_ZH_RATE))

    # Final flush
    flush_dialogue()

    return segments


async def produce_chinese_episode(
    ep_num: str,
    filename: str,
    title: str,
) -> None:
    """Produce a single Chinese anime episode from draft JSON to final MP3."""
    story_path = DRAFTS_DIR / filename
    if not story_path.exists():
        print(f"   ⚠️  File not found: {story_path}")
        return

    with open(story_path, encoding="utf-8") as f:
        story_data = json.load(f)

    story_body = story_data.get("story_body", "")
    if not story_body:
        print(f"   ⚠️  No story_body in {filename}")
        return

    # Parse into segments
    segments = parse_chinese_anime_script(story_body)
    print(f"\n🎬 [CN-{ep_num}] {title}")
    print(f"   📋 {len(segments)} segments")

    # Show voice breakdown
    voices_used: set = set()
    for _, voice_name, rate in segments:
        voices_used.add(f"{voice_name} ({rate})")
    if voices_used:
        print(f"   🎭 Voices: {', '.join(sorted(voices_used))}")

    # ── Generate TTS for each segment ───────────────────────
    print(f"   🎧 Generating TTS...")
    temp_files: list = []

    for i, (text, voice_name, rate) in enumerate(segments):
        cleaned = text.strip().strip("。").strip()
        if not cleaned or len(cleaned) < 2:
            # Very short or empty → silence placeholder
            silent = AudioSegment.silent(duration=1500)
            sp = f"/tmp/_cn_{ep_num}_{i:04d}.mp3"
            try:
                silent.export(sp, format="mp3")
                temp_files.append((sp, i))
            except Exception as e:
                print(f"      ⚠️  [{i:04d}] Silent export failed: {e}")
            continue

        output = f"/tmp/_cn_{ep_num}_{i:04d}.mp3"
        try:
            comm = edge_tts.Communicate(cleaned, voice_name, rate=rate)
            await comm.save(output)
            sz = os.path.getsize(output)
            preview = cleaned[:40].replace("\n", " ")
            print(f"      ✅ [{i:04d}] {sz // 1024}KB | {voice_name} ({rate}) | {preview}")
            temp_files.append((output, i))
        except Exception as e:
            print(f"      ❌ [{i:04d}] FAILED: {e}")
            # Fallback: insert silence
            try:
                silent = AudioSegment.silent(duration=2000)
                silent.export(output, format="mp3")
                temp_files.append((output, i))
            except Exception:
                print(f"      ⚠️  [{i:04d}] Could not create fallback silence")

    if not temp_files:
        print(f"   ❌ No valid audio generated for episode {ep_num}")
        return

    # ── Concatenate all segments ────────────────────────────
    temp_files.sort(key=lambda x: x[1])
    print(f"   🔗 Concatenating {len(temp_files)} segments...")

    final = AudioSegment.silent(duration=500)
    prev_was_scene = False

    for tf, idx in temp_files:
        try:
            seg = AudioSegment.from_mp3(tf)
            gap = 600 if prev_was_scene else 400
            final += AudioSegment.silent(duration=gap) + seg

            # Determine if this segment was a scene marker (used for next gap)
            if idx < len(segments):
                # Scene markers are LK narration of the scene label
                # We consider a segment a "scene" if its text looks like a scene label
                scene_text, _, _ = segments[idx]
                prev_was_scene = bool(
                    re.search(r"场景", scene_text) or re.search(r"^[—\-]{2,}", scene_text)
                )
            else:
                prev_was_scene = False
        except Exception as e:
            print(f"      ⚠️  Skipping corrupt segment {tf}: {e}")
        finally:
            if os.path.exists(tf):
                try:
                    os.remove(tf)
                except OSError:
                    pass

    # ── Export final audio ───────────────────────────────────
    output_dir = OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"cn_{ep_num}_anime.mp3"
    temp_export = f"/tmp/_cn_final_{ep_num}.mp3"

    try:
        final.export(temp_export, format="mp3", bitrate="192k")
    except Exception as e:
        print(f"   ❌ Export failed: {e}")
        return

    # ── Add ID3 metadata via ffmpeg ─────────────────────────
    meta_file = f"/tmp/_cn_meta_{ep_num}.txt"
    try:
        with open(meta_file, "w", encoding="utf-8") as mf:
            mf.write(";FFMETADATA1\n")
            mf.write("artist=提灯人\n")
            mf.write("album=舍赫拉查德之灯\n")
            mf.write(f"title={title}\n")
            mf.write("genre=Podcast\n")
            mf.write("album_artist=舍赫拉查德之灯\n")
            mf.write("comment=中文动画风格音频剧\n")
            mf.write("language=zh\n")

        result = subprocess.run(
            [
                "ffmpeg", "-y",
                "-i", temp_export,
                "-i", meta_file,
                "-map_metadata", "1",
                "-codec", "copy",
                str(output_path),
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"   ⚠️  ffmpeg metadata warning: {result.stderr.strip()}")
            # Fallback: copy without metadata
            subprocess.run(
                ["cp", temp_export, str(output_path)],
                capture_output=True,
            )
    except Exception as e:
        print(f"   ⚠️  Metadata step failed: {e}")
        # Fallback: copy raw file
        try:
            subprocess.run(["cp", temp_export, str(output_path)], capture_output=True)
        except Exception:
            pass
    finally:
        # Cleanup temp files
        for p in [meta_file, temp_export]:
            if os.path.exists(p):
                try:
                    os.remove(p)
                except OSError:
                    pass

    # ── Report ───────────────────────────────────────────────
    duration_s = len(final) / 1000.0
    if output_path.exists():
        file_size_mb = output_path.stat().st_size / (1024 * 1024)
        print(f"   ✅ Done: {duration_s:.0f}s ({duration_s / 60:.1f}min) | {file_size_mb:.1f}MB")
        print(f"      📁 {output_path}")
    else:
        print(f"   ❌ Output file not created at {output_path}")


async def main():
    """Produce all Chinese anime episodes."""
    print("=" * 55)
    print("  舍赫拉查德之灯 — 中文音频制作")
    print("=" * 55)

    # Discover Chinese draft files — follow pattern cn_0*_*.json
    draft_files = sorted(DRAFTS_DIR.glob("cn_0*_*.json"))
    if not draft_files:
        print("❌ No Chinese draft files found matching cn_0*_*.json")
        sys.exit(1)

    # Build episode list from discovered files
    episodes = []
    for df in draft_files:
        try:
            with open(df, encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"⚠️  Skipping unreadable file {df.name}: {e}")
            continue

        # Extract episode number from filename: cn_01_rashid.json → "01"
        stem = df.stem  # e.g. "cn_01_rashid"
        parts = stem.split("_")
        ep_num = parts[1] if len(parts) >= 2 and parts[1].isdigit() else "00"

        title = data.get("title", f"Episode {ep_num}").strip()
        # Remove trailing subtitle like " — 动画风格"
        title_clean = re.sub(r"\s*[—\-]\s*.*$", "", title).strip()
        if not title_clean:
            title_clean = title

        episodes.append((ep_num, df.name, title_clean))

    if not episodes:
        print("❌ No valid episodes to process")
        sys.exit(1)

    print(f"\n📋 Found {len(episodes)} episode(s):")
    for ep, fn, ti in episodes:
        print(f"   CN-{ep}: {ti} ({fn})")

    # Process all episodes concurrently
    tasks = [
        produce_chinese_episode(ep_num, filename, title)
        for ep_num, filename, title in episodes
    ]
    await asyncio.gather(*tasks)

    print("\n" + "=" * 55)
    print("✅ ALL CHINESE EPISODES COMPLETE")
    print("=" * 55)


if __name__ == "__main__":
    asyncio.run(main())
