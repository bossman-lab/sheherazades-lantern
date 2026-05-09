#!/usr/bin/env python3
"""
Batch audio generation for Ep06-10 — all 4 languages.
Run with: python3 batch_gen_06_10.py [lang]
  lang: en, cn, ar, es, or 'all' (default: all)

Outputs go to: /root/.hermes/projects/sheherazades-lantern/audio/episodes/
"""
import asyncio, json, sys, os, re, subprocess, time
from pathlib import Path

PROJECT_DIR = Path.home() / ".hermes" / "projects" / "sheherazades-lantern"
SCRIPTS_DIR = PROJECT_DIR / "scripts"
DRAFTS_DIR = PROJECT_DIR / "content" / "drafts"
AUDIO_DIR = PROJECT_DIR / "audio" / "episodes"
VOICE_PALETTE_PATH = PROJECT_DIR / "voice_palette.json"

sys.path.insert(0, str(SCRIPTS_DIR))

with open(VOICE_PALETTE_PATH, encoding="utf-8") as f:
    palette = json.load(f)

import edge_tts
from pydub import AudioSegment

# ── Shared: parse_anime_script ──────────────────────────────────
GAP_BETWEEN = 400  # ms

CHAR_TO_ID = {
    "THE LANTERN KEEPER": "lantern_keeper",
    "RASHID": "rashid",
    "YUEYA": "yueya",
    "KARIM": "karim",
    "NADIA": "nadia",
    "KHALID": "khalid",
    "DUNYAZAD": "dunyazad",
    "LAILA": "layla",
    "LAYLA": "layla",
    # Arabic
    "الراوي": "lantern_keeper",
    "حارس المصباح": "lantern_keeper",
    "التاجر": "nadia",
    "حارس السوق": "khalid",
    "رشيد": "rashid",
    "يويّا": "yueya",
    "كريم": "karim",
    "نادية": "nadia",
    "خالد": "khalid",
    "دنيازاد": "dunyazad",
    "ليلى": "layla",
    # Chinese
    "提灯人": "lantern_keeper",
    "拉希德": "rashid",
    "月芽": "yueya",
    "卡里姆": "karim",
    "纳迪亚": "nadia",
    "哈立德": "khalid",
    "杜妮亚扎德": "dunyazad",
    "莱拉": "layla",
    # Spanish
    "EL GUARDIÁN DE LA LINTERNA": "lantern_keeper",
    "GUARDIÁN DE LA LINTERNA": "lantern_keeper",
    "RASHID": "rashid",
    "YUEYA": "yueya",
    "KARIM": "karim",
    "NADIA": "nadia",
    "KHALID": "khalid",
    "DUNYAZAD": "dunyazad",
    "LAYLA": "layla",
    "VENDEDOR": "nadia",
    "VENDOR": "nadia",
}

def get_voice_and_rate(char_id, lang="en"):
    if char_id not in palette:
        if lang == "zh":
            return ("zh-CN-XiaoxiaoNeural", "+0%")
        elif lang == "ar":
            return ("ar-SA-ZariyahNeural", "+0%")
        elif lang == "es":
            return ("es-MX-DaliaNeural", "+0%")
        return ("en-GB-SoniaNeural", "+0%")
    char = palette[char_id]
    voices = char.get("voices", {})
    v = voices.get(lang, voices.get("en", {}))
    if not v:
        return ("en-GB-SoniaNeural", "+0%")
    return (v["voice"], v["base_rate"])

def parse_anime_script(story_text):
    """Parse anime-format script into TTS segments."""
    lines = story_text.strip().split("\n")
    segments = []
    current_char_id = None
    current_voice_name = None
    dialogue_buffer = []

    def flush_dialogue():
        nonlocal dialogue_buffer, current_char_id, current_voice_name
        if not dialogue_buffer:
            return
        text = " ".join(d.strip() for d in dialogue_buffer if d.strip())
        seg_type = f"char:{current_char_id}" if current_char_id else "narr:default"
        segments.append((text, current_voice_name, seg_type))
        dialogue_buffer = []

    for line in lines:
        stripped = line.strip()

        # Scene marker
        if stripped.startswith("——"):
            flush_dialogue()
            if stripped:
                segments.append((stripped, "", "scene"))
            current_char_id = None
            continue

        # Sound/mood cue — SKIP entirely (not read aloud). Handles both () and （）
        if stripped.startswith("(") and stripped.endswith(")") and len(stripped) < 200:
            flush_dialogue()
            continue
        if stripped.startswith("（") and stripped.endswith("）") and len(stripped) < 200:
            flush_dialogue()
            continue

        # Character dialogue line — accept both : and ：
        char_match = re.match(r'^([A-Za-z\u0600-\u06FF\u4e00-\u9fffÀ-ÿÑñÁáÉéÍíÓóÚúÜü\s]+)[:：]\s*(.*)', stripped)
        if char_match:
            flush_dialogue()
            raw_name = char_match.group(1).strip().upper()
            dialogue = char_match.group(2).strip()
            char_id = CHAR_TO_ID.get(raw_name, None)
            if char_id:
                current_char_id = char_id
            else:
                current_char_id = None
            if dialogue:
                dialogue_buffer.append(dialogue)
        else:
            # Continuation of previous dialogue
            if stripped and not stripped.startswith("("):
                dialogue_buffer.append(stripped)

    flush_dialogue()
    return segments

# ── Language-specific voice mapping ──────────────────────────────
def get_lang_config(lang):
    if lang == "en":
        return {
            "lk_voice": palette["lantern_keeper"]["voices"]["en"]["voice"],
            "ext": "ep{:02d}_anime.mp3",
            "prefix": ""
        }
    elif lang == "zh":
        return {
            "lk_voice": palette["lantern_keeper"]["voices"]["zh"]["voice"],
            "ext": "cn_{:02d}_anime.mp3",
            "prefix": "cn_"
        }
    elif lang == "ar":
        return {
            "lk_voice": "ar-SA-ZariyahNeural",
            "ext": "ar_ep{:02d}_anime.mp3",
            "prefix": "ar_"
        }
    elif lang == "es":
        return {
            "lk_voice": "es-MX-DaliaNeural",
            "ext": "es_{:02d}_anime.mp3",
            "prefix": "es_"
        }

# ── Episodes to produce ─────────────────────────────────────────
def get_episodes(lang):
    mapping = {
        "en": [
            (6, "06_nadia_rashid_anime.json", "The Spice That Remembered"),
            (7, "07_khalid_layla_anime.json", "The Song That Unmade a Sword"),
            (8, "08_dunyazad_yueya_anime.json", "The Story That Read Her Back"),
            (9, "09_karim_nadia_anime.json", "The Debt That Travels on the Wind"),
            (10, "10_karim_layla_anime.json", "The Elder and the Oracle"),
        ],
        "zh": [
            (6, "cn_06_nadia_rashid.json", "香料之忆"),
            (7, "cn_07_khalid_layla.json", "以歌碎剑"),
            (8, "cn_08_dunyazad_yueya.json", "读取她的故事"),
            (9, "cn_09_karim_nadia.json", "随风而行的债务"),
            (10, "cn_10_karim_layla.json", "长者和神谕"),
        ],
        "ar": [
            (6, "ar_06_nadia_rashid.json", "سوق الظل"),
            (7, "ar_07_khalid_layla.json", "الأغنية التي فكت السيف"),
            (8, "ar_08_dunyazad_yueya.json", "القصة التي قرأتها"),
            (9, "ar_09_karim_nadia.json", "الدين الذي يسافر على الريح"),
            (10, "ar_10_karim_layla.json", "الشيخ والكاهنة"),
        ],
        "es": [
            (6, "es_06_nadia_rashid.json", "La especia que recordaba"),
            (7, "es_07_khalid_layla.json", "La canción que deshizo una espada"),
            (8, "es_08_dunyazad_yueya.json", "La historia que la leyó a ella"),
            (9, "es_09_karim_nadia.json", "La deuda que viaja en el viento"),
            (10, "es_10_karim_layla.json", "El anciano y el oráculo"),
        ]
    }
    return mapping.get(lang, [])

# ── Audio production ────────────────────────────────────────────
async def produce_one(ep_num, filename, title, lang, config):
    story_path = DRAFTS_DIR / filename
    with open(story_path, encoding="utf-8") as f:
        story_data = json.load(f)

    story_body = story_data["story_body"]
    segments = parse_anime_script(story_body)

    output_file = AUDIO_DIR / config["ext"].format(ep_num)
    
    print(f"\n🎬 [{lang.upper()}-{ep_num:02d}] {title}")
    print(f"   {len(segments)} segments → {output_file.name}")

    temp_files = []
    for i, (text, voice_name, seg_type) in enumerate(segments):
        if not text.strip():
            continue

        rate = "+0%"
        voice = config["lk_voice"]

        if seg_type.startswith("char:"):
            char_id = seg_type.split(":")[1]
            v, rate = get_voice_and_rate(char_id, lang)
            voice = v
        elif seg_type == "scene":
            rate = "-5%"

        cleaned = text.strip().strip(".").strip()
        if not cleaned:
            continue

        temp = AUDIO_DIR / f"_temp_{lang}_{ep_num}_{i:04d}.mp3"
        try:
            communicate = edge_tts.Communicate(cleaned, voice, rate=rate)
            await communicate.save(str(temp))
            temp_files.append(str(temp))
        except Exception as e:
            print(f"   ⚠️ Segment {i}: {e}")
            continue

        if (i + 1) % 20 == 0:
            print(f"   ... {i+1}/{len(segments)} segments done")

    # Concatenate
    if not temp_files:
        print(f"   ❌ No segments generated!")
        return

    combined = AudioSegment.empty()
    for tf in temp_files:
        try:
            seg = AudioSegment.from_mp3(tf)
            combined += seg + AudioSegment.silent(GAP_BETWEEN)
        except Exception as e:
            print(f"   ⚠️ Error loading {tf}: {e}")

    combined.export(str(output_file), format="mp3", bitrate="192k")
    duration = len(combined) / 1000
    mb = os.path.getsize(output_file) / (1024 * 1024)

    # Cleanup
    for tf in temp_files:
        try: os.remove(tf)
        except: pass

    print(f"   ✅ {output_file.name} — {duration:.1f}s, {mb:.1f}MB")

async def main():
    langs = sys.argv[1:]
    if not langs or "all" in langs:
        langs = ["en", "zh", "ar", "es"]
    
    for lang in langs:
        print(f"\n{'='*50}")
        print(f" LANGUAGE: {lang}")
        print(f"{'='*50}")
        config = get_lang_config(lang)
        episodes = get_episodes(lang)
        for ep_num, filename, title in episodes:
            await produce_one(ep_num, filename, title, lang, config)
    
    print(f"\n{'='*50}")
    print("🎉 ALL DONE!")
    print(f"{'='*50}")

if __name__ == "__main__":
    asyncio.run(main())
