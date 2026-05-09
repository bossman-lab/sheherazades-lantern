---
title: "How I Built a 4-Language AI Podcast Pipeline — and Why Distribution Is the Only Real Problem"
description: "Behind the scenes of Sheherazade's Lantern: a one-person, 4-language podcast powered by AI storytelling, edge-tts, and a static site generator. Full architecture walkthrough."
published: false
---

# How I Built a 4-Language AI Podcast Pipeline — and Why Distribution Is the Only Real Problem

*Arabian bedtime stories, rekindled for modern souls. In four languages. By one person.*

I run **Sheherazade's Lantern** — a podcast that produces original Arabian-inspired fiction in **English, Arabic, Chinese, and Spanish**. Each episode runs 15–18 minutes with a full voice cast (8 distinct characters per language, each with a different accent/voice).

Ten episodes done. Four languages. One person.

Here's exactly how the pipeline works, where the complexity really lives, and the one thing that matters more than all the engineering put together.

---

## The Architecture at 10,000 Feet

```
[Character Universe] → [LLM Story Gen] → [Parse & Save] → [Audio Production]
                                                                    ↓
[SEO + RSS + Sitemap] ← [Static Site Gen] ← [Deploy via API] ← [Cover Art]
```

Every component is **CLI-driven**, no web UI, no database, no server. The entire project lives in a `~/.hermes/projects/` directory on a Linux server.

---

## 1. The Character Universe — Making AI Stories Coherent

The #1 problem with AI-generated fiction: **every story starts from zero**. Characters don't carry over, the world resets, nothing compounds.

The fix: a shared character universe stored as JSON files.

```json
// universe/characters.json (simplified)
{
  "yueya": {
    "name": "Yueya (Moon-Child)",
    "archetype": "The Star-Seeker",
    "traits": ["curious", "dreamy", "innocent"],
    "signature_objects": ["brass astrolabe"],
    "voice": "en-GB-MaisieNeural",
    "appearances": 3,
    "status": "active"
  },
  "rashid": {
    "name": "Rashid the Mapmaker",
    "archetype": "The Unreliable Chronicler",
    "traits": ["scatterbrained", "charming", "obsessive"],
    "voice": "en-IE-ConnorNeural",  // Irish accent
    "appearances": 2,
    "status": "active"
  }
  // ... 5 more characters
}
```

**The character selection algorithm:**
1. Filter active characters
2. Sort by `appearance_count` (ascending — promote underused characters)
3. 60% chance pick the least-used, 40% random
4. Inject the character's full profile into the LLM prompt
5. After generation, increment appearance count

This single trick turns a collection of stories into a **canon**. Characters form relationships. Artifacts reappear. Listeners who skip an episode miss context. The half-life of each story goes from "read-once" to "re-listen to catch the callback."

**Proven effect**: After 10 episodes with the same 7 characters, new stories write themselves faster because the LLM has consistent character voices to draw on.

---

## 2. Multi-Language Audio Production — The SSML Trap

This is where I lost the most time to a **deceptive bug**.

### The Setup

Each language has a full voice palette — 8 distinct voices mapped to the same 8 characters:

```python
# English — different accents so listeners identify characters instantly
VOICE_MAP_EN = {
    "THE LANTERN KEEPER": "en-GB-SoniaNeural",         # BBC English
    "YUEYA":              "en-GB-MaisieNeural",         # Young British
    "RASHID":             "en-IE-ConnorNeural",          # Irish
    "NADIA":              "en-US-JennyNeural",           # American
    "DUNYAZAD":           "en-IN-NeerjaExpressiveNeural", # Indian
    "LAYLA":              "en-AU-NatashaNeural",         # Australian
    # ...
}
```

For Chinese, I use voices from mainland China, Taiwan, and Hong Kong to create the same effect — each character sounds from a different region.

### The Bug That Cost Me 3 Hours

`edge-tts` (the Python library for Microsoft Edge's TTS) **reads XML tags as speech**. I tried to use SSML for emotional control:

```python
# ❌ WRONG — edge-tts escapes the XML internally
comm = edge_tts.Communicate(
    '<mstts:express-as type="cheerful">Hello there!</mstts:express-as>',
    voice
)
# Output: "speak version 1.0 m s s t s express as type cheerful Hello there"
```

The library calls `xml.sax.saxutils.escape()` on your text before wrapping it in a `<speak>` envelope. Custom SSML is architecturally impossible.

**The fix**: Segment-by-segment plain-text concatenation.

```python
# ✅ CORRECT — plain text only, voice and rate as parameters
for segment in parsed_segments:
    comm = edge_tts.Communicate(
        segment["text"],           # plain text
        segment["voice"],          # voice name
        rate=segment["rate"]       # e.g. "+5%" for excited
    )
    await comm.save(temp_path)
    # Concatenate with pydub
```

Each 1,500-word story becomes 70–120 segments. A 5-episode batch takes ~25 minutes (each segment is a network call).

**Emotional range comes from rate modulation only:**
| Emotion | Rate |
|---------|:----:|
| Default | +0% |
| Excited | +5% to +10% |
| Calm | -3% to -5% |
| Sad/Grief | -8% to -10% |

No SSML. No XML. Plain text. This is the universal approach that works for **all languages**.

---

## 3. Cover Art — Photographic Anime, Zero Circles

Cover art for a podcast is more important than most people think. It's the first thing people see in Apple Podcasts or Spotify.

**The approach**: Royalty-free photography from Unsplash + PIL overlays.

```python
from PIL import Image, ImageDraw, ImageFont
import requests

# Download high-res photo
resp = requests.get("https://images.unsplash.com/photo-1509316785289-025f5b846b35?w=1920")
img = Image.open(BytesIO(resp.content))

# Crop to square
img = img.crop(...)  # center crop

# Apply Gaussian blur for dreamy anime feel
img = img.filter(ImageFilter.GaussianBlur(radius=1.5))

# Add edge vignette — progressive darkening
for r in range(1500, 200, -30):
    alpha = ...  # increasing toward edges
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(0,0,0,alpha))

# Typography only — episode number, title, brand
draw.text((x, y), "#01", fill=(255,255,255,200))
draw.text((x, y+80), "The Map of the Moving Streets", ...)
```

**Critical rule learned the hard way**: **No PIL-drawn circles.** No glow rings. No badge backgrounds behind episode numbers. My first version had a white glow circle behind the episode number, and the user's response was... emphatically negative. The photo provides all the visual depth. Typography is all you need.

---

## 4. Static Site — Multilingual Without a CMS

The website is **11ty (Eleventy)** — a zero-JS static site generator.

```
src/
├── _data/
│   ├── site.json       # Multilingual config (names, taglines, footer per lang)
│   └── episodes.json   # ALL episode data in one file
├── _includes/
│   ├── layout.njk      # Apple aesthetic template
│   └── rss.njk         # RSS template (generates per-language feeds)
├── en/ / cn/ / ar/ / es/  # One Nunjucks page per language
└── sitemap.njk         # Auto-generates sitemap.xml
```

Each language gets:
- Its own homepage (e.g., `/en/`, `/ar/`)
- Its own RSS feed (`/en/podcast.xml`, `/ar/podcast.xml`)
- JSON-LD structured data with PodcastSeries schema
- `<link rel="alternate" hreflang="...">` pointing to all language variants

**Adding a new episode**: Edit one JSON file → `npm run build` → deploy. No database, no CMS, no hosting bill (GitHub Pages is free).

```json
{
  "en": {
    "episodes": [
      {
        "number": "06",
        "title": "The Spice That Remembered",
        "audio": "audio/episodes/ep06_anime.mp3",
        "duration": "16:24",
        "description": "Nadia the spice merchant has a shelf...",
        "characters": ["Nadia", "Rashid"]
      }
    ]
  },
  "cn": { /* same episode, Chinese */ }
}
```

### The Nunjucks Gotcha

Inside `<script type="application/ld+json">`, Nunjucks auto-escapes `'` to `&#39;`, which **breaks JSON-LD parsing**. Fix: a custom filter.

```javascript
// .eleventy.js
eleventyConfig.addFilter("json_str", (str) => {
  return JSON.stringify(str).slice(1, -1);
});

// Template: use | json_str | safe
"name": "{{ site.names[lang] | json_str | safe }}"
```

---

## 5. Deploy — Github API, Not Git

The server doesn't have `git-remote-https`. No `git push`. The solution: **Git Data API** for atomic multi-file commits.

```python
import requests, base64

def api(method, path, data=None):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/{path}"
    return requests.request(method, url, headers=HEADERS, json=data).json()

# 1. Get current HEAD
ref = api("GET", "git/refs/heads/main")
base_sha = ref["object"]["sha"]

# 2. Get base tree
commit = api("GET", f"git/commits/{base_sha}")
base_tree = commit["tree"]["sha"]

# 3. Create blobs for each file
blobs = []
for git_path, local_path in files.items():
    with open(local_path, "rb") as f:
        content = f.read()
    is_binary = git_path.endswith(".mp3")
    blob_data = {"content": base64.b64encode(content).decode(),
                 "encoding": "base64" if is_binary else "utf-8"}
    blob = api("POST", "git/blobs", blob_data)
    blobs.append({"path": git_path, "mode": "100644",
                  "type": "blob", "sha": blob["sha"]})

# 4. Create tree → commit → update ref
tree = api("POST", "git/trees", {"base_tree": base_tree, "tree": blobs})
new_commit = api("POST", "git/commits", {
    "message": "Add Ep06: The Spice That Remembered (all 4 languages)",
    "tree": tree["sha"],
    "parents": [base_sha]
})
api("PATCH", "git/refs/heads/main", {"sha": new_commit["sha"]})
```

One deploy script. Zero infrastructure. Atomic commits with 4-language audio, RSS, and homepage in a single push.

---

## 6. The Hard Truth — HLT Analysis

After building all this, I ran the pipeline through an **HLT (Half-life × Leverage × Transferability)** framework to evaluate where to invest next.

| Metric | Score | Analysis |
|--------|:-----:|----------|
| **H — Half-life** | 8/10 | Classic tales + shared universe → content ages well |
| **L — Leverage** | 3/10 | **Bottleneck.** Great content, zero audience |
| **T — Transferability** | 7/10 | Platform-independent, portable across hosting |

**Score**: 8×3×7 = **168** (decent, but far below potential).

The diagnostic is clear: **藏书阁 (Library Trap)** — beautiful content locked in a room with no visitors. Distribution is the only bottleneck.

After distribution (L→7): 9×7×8 = **504 🏆** — higher than my top-ranked activity (writing tech blogs, 448).

---

## The One Thing That Matters More Than Engineering

I can generate a 4-language episode in ~20 minutes. I can build a 10-episode backlog in a weekend. The entire pipeline — character universe, multi-voice TTS, cover art, multilingual RSS, SEO — took about two weeks to build.

**But none of that matters if nobody listens.**

The real work isn't the pipeline. It's:
- Submitting RSS feeds to Apple Podcasts, Spotify, Deezer (none have APIs — all manual)
- Posting consistently on Substack
- Engaging on Reddit, Twitter, and podcast communities
- Getting the first 100 listeners

**If you're building an AI content pipeline**: spend 20% of your time on the pipeline and 80% on distribution. The production side is solved. The distribution side is not — and that's where the real leverage lives.

---

## What's Next

- **Apple Podcasts submission** (pending — need to work around @tutamail.com rejection)
- **Substack** for primary distribution + monetization
- **KDP collections** (ebook bundle every 10 episodes)
- **Complete Spanish (ES) distribution** — LatAm market untapped

---

*The full source code and project structure are at [github.com/bossman-lab/sheherazades-lantern](https://github.com/bossman-lab/sheherazades-lantern). Questions? Comments? Reach out below.*

*One more thing: the podcast itself is live at [bossman-lab.github.io/sheherazades-lantern](https://bossman-lab.github.io/sheherazades-lantern/) — pick a language and give it a listen.*
