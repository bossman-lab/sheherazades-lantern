#!/usr/bin/env python3
"""
Arabic anime audio production — same anime parser, Arabic voices.
"""
import asyncio, json, sys, os, re, subprocess
sys.path.insert(0, str(os.path.dirname(os.path.abspath(__file__))))
from produce_anime_v2 import parse_anime_script, GAP_BETWEEN, palette, CHAR_TO_ID
import edge_tts
from pydub import AudioSegment
from pathlib import Path

PROJECT_DIR = Path.home() / ".hermes" / "projects" / "sheherazades-lantern"
lk_voice = palette["lantern_keeper"]["voices"]["ar"]["voice"]

def get_voice_ar(char_id):
    """Get Arabic voice for character."""
    if char_id not in palette:
        return "ar-SA-ZariyahNeural"
    char = palette[char_id]
    return char["voices"]["ar"]["voice"]

async def produce_arabic(ep_num, filename, title):
    story_path = PROJECT_DIR / "content" / "drafts" / filename
    with open(story_path, encoding='utf-8') as f:
        story_data = json.load(f)
    
    story_body = story_data["story_body"]
    segments = parse_anime_script(story_body)
    
    print(f"\n🎬 [AR-{ep_num}] {title}")
    print(f"   {len(segments)} segments")
    
    lk_ar_voice = palette["lantern_keeper"]["voices"]["ar"]["voice"]
    
    temp_files = []
    for i, (text, voice_name, seg_type) in enumerate(segments):
        # Map to Arabic voice
        ar_voice = lk_ar_voice
        if seg_type.startswith("char:"):
            char_id = seg_type.split(":")[1]
            ar_voice = get_voice_ar(char_id)
        
        rate = "+0%"
        
        cleaned = text.strip().strip(".").strip()
        if not cleaned or len(cleaned) < 2:
            silent = AudioSegment.silent(duration=1500)
            sp = f"/tmp/_ar_{ep_num}_{i:04d}.mp3"
            silent.export(sp, format="mp3")
            temp_files.append((sp, i))
            continue
        
        output = f"/tmp/_ar_{ep_num}_{i:04d}.mp3"
        try:
            comm = edge_tts.Communicate(text, ar_voice, rate=rate)
            await comm.save(output)
            sz = os.path.getsize(output)
            preview = text[:30].replace("\n", " ")
            print(f"      [{i:04d}] {sz//1024}KB {ar_voice} | {preview}")
            temp_files.append((output, i))
        except Exception as e:
            print(f"      ❌ [{i:04d}] FAILED: {e}")
            silent = AudioSegment.silent(duration=2000)
            silent.export(output, format="mp3")
            temp_files.append((output, i))
    
    temp_files.sort(key=lambda x: x[1])
    print(f"   🔗 Concatenating...")
    
    final = AudioSegment.silent(duration=500)
    prev_was_scene = False
    for tf, idx in temp_files:
        try:
            seg = AudioSegment.from_mp3(tf)
            gap = 600 if prev_was_scene else 400
            final += AudioSegment.silent(duration=gap) + seg
            if idx < len(segments):
                _, _, seg_type = segments[idx]
                prev_was_scene = (seg_type == "scene")
        except:
            pass
        finally:
            if os.path.exists(tf):
                os.remove(tf)
    
    output_path = PROJECT_DIR / "audio" / "episodes" / f"ar_ep{ep_num}_anime.mp3"
    temp_export = f"/tmp/_ar_final_{ep_num}.mp3"
    final.export(temp_export, format="mp3", bitrate="192k")
    
    meta_file = f"/tmp/_ar_meta_{ep_num}.txt"
    with open(meta_file, "w", encoding='utf-8') as mf:
        mf.write(";FFMETADATA1\n")
        mf.write("artist=حارس المصباح\n")
        mf.write("album=مصباح شهرزاد\n")
        mf.write(f"title={title}\n")
        mf.write("genre=Podcast\n")
        mf.write("album_artist=مصباح شهرزاد\n")
        mf.write("comment=حكايات ألف ليلة وأسلوب الأنمي\n")
    
    subprocess.run(
        ["ffmpeg", "-y", "-i", temp_export, "-i", meta_file,
         "-map_metadata", "1", "-codec", "copy", str(output_path)],
        capture_output=True
    )
    os.remove(meta_file)
    os.remove(temp_export)
    
    dur = len(final) / 1000.0
    sz = os.path.getsize(output_path) / 1024 / 1024
    print(f"   ✅ Done: {dur:.0f}s ({dur/60:.1f}min) | {sz:.1f}MB")

async def main():
    episodes = [
        ("01", "ar_01_rashid.json", "خريطة الشوارع المتحركة"),
        ("02", "ar_02_nadia.json", "بهار الأشياء المنسية"),
        ("03", "ar_03_khalid.json", "النصل الذي لم يكتمل"),
        ("04", "ar_04_dunyazad.json", "كتاب ما لم يُقل"),
        ("05", "ar_05_layla.json", "الرمال التي غنَّت مرتين"),
    ]
    
    tasks = [produce_arabic(ep, fn, title) for ep, fn, title in episodes]
    await asyncio.gather(*tasks)
    
    print("\n" + "=" * 50)
    print("✅ ALL ARABIC EPISODES COMPLETE")

if __name__ == "__main__":
    asyncio.run(main())
