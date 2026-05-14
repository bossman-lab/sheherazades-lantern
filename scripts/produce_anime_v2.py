#!/usr/bin/env python3
"""
Fixed anime audio production — properly tracks current speaker across lines.
Fixes: multi-line dialogue, voice mapping, speed.
"""

import json, re, asyncio, edge_tts, os, subprocess
from pydub import AudioSegment
from pathlib import Path

PROJECT_DIR = Path.home() / ".hermes" / "projects" / "sheherazades-lantern"
VOICE_PALETTE = PROJECT_DIR / "voice_palette.json"
GAP_BETWEEN = 400  # ms between segments (was 200)

with open(VOICE_PALETTE) as f:
    palette = json.load(f)

# Character name → voice_id mapping
CHAR_TO_ID = {
    "THE LANTERN KEEPER": "lantern_keeper",
    "EL GUARDIÁN DE LA LINTERNA": "lantern_keeper",
    "RASHID": "rashid",
    "YUEYA": "yueya",
    "KARIM": "karim",
    "NADIA": "nadia",
    "KHALID": "khalid",
    "DUNYAZAD": "dunyazad",
    "LAILA": "layla",
    "LAYLA": "layla",
    # Arabic character names
    "خَالِد": "khalid",
    "خالد": "khalid",
    "لَيْلَى": "layla",
    "ليلى": "layla",
}
# Build regex from known names to avoid false matches (e.g. "CLOSE ON:")
# Sorted longest-first so longer names match before their prefixes
_KNOWN_NAMES = sorted(CHAR_TO_ID.keys(), key=len, reverse=True)
CHAR_TAG_PATTERN = re.compile(
    r'^(' + '|'.join(re.escape(n) for n in _KNOWN_NAMES) + r')'
    r'(?:\s*\([^)]*\))?\s*:\s*(.*)',
    re.IGNORECASE  # case-insensitive so "El Guardián..." matches
)


def get_voice_and_rate(char_id, emotion_key="default"):
    """Get voice and base_rate from palette. 
    Uses character's natural base rate only — emotion modulates style, not speed."""
    if char_id not in palette:
        return "en-GB-SoniaNeural", "+0%"
    char = palette[char_id]
    v = char["voices"]["en"]
    return v["voice"], v["base_rate"]


def detect_emotion(text, char_id):
    """Heuristic emotion detection."""
    t = text.lower()
    char = palette.get(char_id, {})
    emotions = char.get("emotions", {})
    if not emotions:
        return "default"
    
    if any(w in t for w in ["no!", "never!", "stop!", "enough!"]):
        return "defiant" if "defiant" in emotions else "default"
    if any(w in t for w in ["run", "danger", "quick", "help"]):
        return "urgent" if "urgent" in emotions else "default"
    if any(w in t for w in ["sad", "sorry", "lost", "crying", "tears", "died"]):
        return "sad" if "sad" in emotions else "default"
    if any(w in t for w in ["what?", "why?", "who?", "look!", "see?"]):
        return "curious" if "curious" in emotions else "default"
    if any(w in t for w in ["quiet", "gentle", "soft", "warm", "smile"]):
        return "affectionate" if "affectionate" in emotions else "default"
    
    # Character-specific defaults
    defaults = {"rashid": "excited", "yueya": "curious", "lantern_keeper": "default"}
    return defaults.get(char_id, "default")


def parse_anime_script(story_text):
    """
    Parse anime-format script into TTS segments.
    Now correctly tracks current speaker across multi-line dialogue.
    """
    lines = story_text.strip().split("\n")
    segments = []
    current_char_id = None
    current_voice_name = None
    dialogue_buffer = []
    
    def flush_dialogue():
        """Flush buffered dialogue as character speech."""
        nonlocal dialogue_buffer, current_char_id, current_voice_name
        if not dialogue_buffer:
            return
        full_text = " ".join(dialogue_buffer).strip()
        if full_text and len(full_text) >= 2:
            emotion = detect_emotion(full_text, current_char_id or "lantern_keeper")
            if current_char_id and current_char_id != "lantern_keeper":
                voice, rate = get_voice_and_rate(current_char_id, emotion)
                segments.append((full_text, voice, f"char:{current_char_id}:{rate}"))
            else:
                # Lantern Keeper narration
                em = palette["lantern_keeper"]["emotions"].get("default", {"rate": "+5%"})
                segments.append((full_text, current_voice_name or "en-GB-SoniaNeural", f"narr:{em['rate']}"))
        dialogue_buffer = []
    
    lk_voice = palette["lantern_keeper"]["voices"]["en"]["voice"]
    current_voice_name = lk_voice
    
    for line in lines:
        stripped = line.strip()
        
        # Scene markers
        if stripped.startswith("——"):
            flush_dialogue()
            scene_text = stripped.strip("— ")
            if scene_text:
                segments.append((f"[{scene_text}]", lk_voice, "scene"))
            current_char_id = None
            current_voice_name = lk_voice
            continue
        
        # Blank line = end of dialogue block, flush (only reset if actual dialogue)
        if not stripped:
            had_dialogue = bool(dialogue_buffer)
            flush_dialogue()
            if had_dialogue:
                current_char_id = None
                current_voice_name = lk_voice
            continue
        
        # Stage direction on its own line: skip but don't reset speaker
        if re.match(r'^\(.*\)$', stripped) or re.match(r'^[（(][^）)]*[）)]$', stripped):
            continue
        
        # Character tag: use known-name pattern to avoid false matches
        char_match = CHAR_TAG_PATTERN.match(stripped)
        if char_match:
            flush_dialogue()
            char_name = char_match.group(1).strip()
            after_colon = char_match.group(2).strip()
            
            char_id = CHAR_TO_ID.get(char_name)
            if char_id:
                current_char_id = char_id
                voice, _ = get_voice_and_rate(char_id)
                current_voice_name = voice
            else:
                # Unknown character tag → narrator
                current_char_id = None
                current_voice_name = lk_voice
            
            # There might be dialogue after the colon
            if after_colon and len(after_colon) >= 2:
                dialogue_buffer.append(after_colon)
            continue
        
        # Anything else → dialogue or narration for current speaker
        if current_char_id:
            dialogue_buffer.append(stripped)
        else:
            # Narration without character tag
            flush_dialogue()
            cleaned = re.sub(r'\([^)]*\)', '', stripped).strip()
            if cleaned and len(cleaned) >= 2:
                em = palette["lantern_keeper"]["emotions"].get("default", {"rate": "+5%"})
                segments.append((cleaned, lk_voice, f"narr:{em['rate']}"))
    
    # Final flush
    flush_dialogue()
    return segments


async def main():
    story_path = PROJECT_DIR / "content" / "drafts" / "01_rashid_anime.json"
    with open(story_path) as f:
        story_data = json.load(f)
    
    title = story_data["title"]
    story_body = story_data["story_body"]
    
    print(f"🎬 Anime audio (FIXED): {title}")
    print("-" * 50)
    
    segments = parse_anime_script(story_body)
    print(f"📋 Parsed {len(segments)} segments")
    
    # Show voice breakdown
    voices_used = set()
    for _, voice, seg_type in segments:
        if ":" in seg_type:
            parts = seg_type.split(":")
            if parts[0] == "char":
                voices_used.add(f"{parts[1]} ({voice})")
    print(f"🎭 Voices: {', '.join(sorted(voices_used))}")
    
    # Generate TTS
    print(f"\n🎧 Generating TTS...")
    temp_files = []
    
    for i, (text, voice_name, seg_type) in enumerate(segments):
        # Parse rate from seg_type
        if seg_type.startswith("char:"):
            parts = seg_type.split(":")
            rate = parts[2] if len(parts) > 2 else "+5%"
        elif seg_type == "scene":
            rate = "-5%"
        elif seg_type.startswith("narr:"):
            rate = seg_type.split(":")[1]
        else:
            rate = "+5%"
        
        output = f"/tmp/_aseg_{i:04d}.mp3"
        try:
            comm = edge_tts.Communicate(text, voice_name, rate=rate)
            await comm.save(output)
            # Check file size
            sz = os.path.getsize(output)
            status = "✅" if sz > 1000 else "⚠️"
            preview = text[:50].replace("\n", " ")
            print(f"   {status} [{i:04d}] {sz//1024}KB | {voice_name} ({rate}) | {preview}")
            temp_files.append((output, i))
        except Exception as e:
            print(f"   ❌ [{i:04d}] FAILED: {e}")
            silent = AudioSegment.silent(duration=2000)
            silent.export(output, format="mp3")
            temp_files.append((output, i))
    
    # Sort and concatenate
    temp_files.sort(key=lambda x: x[1])
    print(f"\n🔗 Concatenating {len(temp_files)} segments...")
    
    final = AudioSegment.silent(duration=500)
    prev_was_scene = False
    for tf, idx in temp_files:
        try:
            seg = AudioSegment.from_mp3(tf)
            gap = 600 if prev_was_scene else GAP_BETWEEN
            final += AudioSegment.silent(duration=gap) + seg
            # Check if this segment is a scene marker for next gap
            if idx < len(segments):
                _, _, seg_type = segments[idx]
                prev_was_scene = (seg_type == "scene")
            else:
                prev_was_scene = False
        except Exception as e:
            print(f"   ⚠️ Skipping corrupt file {tf}: {e}")
        finally:
            if os.path.exists(tf):
                os.remove(tf)
    
    # Export
    output_path = PROJECT_DIR / "audio" / "episodes" / "ep01_anime_fixed.mp3"
    temp_export = "/tmp/_afinal.mp3"
    final.export(temp_export, format="mp3", bitrate="192k")
    
    meta_file = "/tmp/_ameta.txt"
    with open(meta_file, "w") as mf:
        mf.write(";FFMETADATA1\n")
        mf.write("artist=The Lantern Keeper\n")
        mf.write("album=Sheherazade's Lantern\n")
        mf.write(f"title={title}\n")
        mf.write("genre=Podcast\n")
        mf.write("album_artist=Sheherazade's Lantern\n")
        mf.write("comment=Anime-style audio drama v2.\n")
    
    subprocess.run(
        ["ffmpeg", "-y", "-i", temp_export, "-i", meta_file,
         "-map_metadata", "1", "-codec", "copy", str(output_path)],
        capture_output=True
    )
    os.remove(meta_file)
    os.remove(temp_export)
    
    duration_s = len(final) / 1000.0
    print(f"\n✅ Done!")
    print(f"   File: {output_path}")
    print(f"   Duration: {duration_s:.0f}s ({duration_s/60:.1f} min)")
    print(f"   Size: {os.path.getsize(output_path)/1024/1024:.1f} MB")


if __name__ == "__main__":
    asyncio.run(main())
