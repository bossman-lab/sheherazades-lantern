---
layout: blog-layout.njk
lang: en
dir: ltr
permalink: "/blog/github-pages-podcast-blog-lessons.html"
title: "Everything That Can Go Wrong When Hosting a Podcast + Blog on GitHub Pages"
description: "A field guide to the silent suffering of using GitHub Pages for anything beyond a simple README — .nojekyll, absolute path hell, 11ty SSG, multi-language RSS, and the 17th time you push the same commit."
---

# Everything That Can Go Wrong When Hosting a Podcast + Blog on GitHub Pages

*Or: The .nojekyll File, the Absolute Path Trap, and Other Rites of Passage*

I host a [4-language AI podcast](https://bossman-lab.github.io/sheherazades-lantern/) on GitHub Pages. It has 10 episodes in English, Chinese, Arabic, and Spanish. Multi-language RSS feeds. A blog with two articles. A JSON-LD structured data system. A sitemap. A dark-mode design system inspired by RunwayML, Linear, Apple, and Spotify.

GitHub Pages is free, fast, and surprisingly capable for a static site. It's also a minefield of silent failures that only reveal themselves when you refresh the page and watch the 404 render for the 17th time.

Here's everything I learned the hard way.

---

## 1. The .nojekyll File (The One That Got Me 4 Times)

**The Problem:** GitHub Pages runs Jekyll by default. Jekyll ignores files and folders starting with `_` (underscore). If you're using 11ty, Hugo, or any static site generator that outputs to `_site/` or has `_data/` or `_includes/` directories, Jekyll will silently eat those files. No error. No warning. Just "Page build failed" in the GitHub API with zero useful information.

**The Fix:** Add an empty `.nojekyll` file at the root of your repository. This tells GitHub Pages to serve files as-is without Jekyll processing.

```bash
touch .nojekyll
git add .nojekyll
git commit -m "No really, I don't use Jekyll"
```

**Why it's insidious:** You'll see `Page build failed: build errors` in the GitHub Pages API but with no actionable message. The build might even show as "successful" while silently dropping your underscore-prefixed directories. The `.nojekyll` file is the first thing you should add to any new GitHub Pages project.

---

## 2. The Absolute Path Trap (A Danger for Project Pages)

**The Problem:** GitHub Pages has two modes:
- **User/Org Pages:** `username.github.io/` — files serve from the domain root
- **Project Pages:** `username.github.io/repository-name/` — files serve from a subpath

Most people start with User Pages and everything works fine. Then they add a second project, use Project Pages, and chaos erupts.

In Project Pages mode, `href="/"` resolves to `username.github.io/` — **not** `username.github.io/repository-name/`. Same for `src="/images/..."`, `src="/audio/..."`, and every other absolute path with a leading `/`.

**The Fix:** Use either:
1. **Full absolute URLs** — `href="https://username.github.io/repository-name/path"` — works from any page, any depth
2. **Relative paths** — `href="path"` (no leading `/`) — resolves relative to the current page's directory
3. **A `<base>` tag** — `<base href="https://username.github.io/repository-name/">` — but this breaks anchor links and some libraries

I went with option 1 across all templates. It's verbose but bulletproof:

```html
<!-- ❌ Breaks on Project Pages -->
<a href="/blog/">Blog</a>
<img src="/audio/assets/cover.jpg">

<!-- ✅ Works everywhere -->
<a href="https://bossman-lab.github.io/sheherazades-lantern/blog/">Blog</a>
<img src="https://bossman-lab.github.io/sheherazades-lantern/audio/assets/cover.jpg">
```

**Script generation tip:** Store your base URL as a variable (`site.url`) in your 11ty data file and reference it everywhere:

```json
{
  "url": "https://bossman-lab.github.io/sheherazades-lantern"
}
```

Then in templates: `href="{{ site.url }}/blog/"`, `src="{{ site.url }}{{ site.cover }}"`.

---

## 3. Git Data API (When Git Remote-HTTPS Is Missing)

My server doesn't have `git-remote-https`. Trying to `git push` returns a cryptic error about missing transport protocols. This is common on minimal Linux systems, Docker containers, and Synology NAS.

**The Fix:** Use GitHub's [Git Data API](https://docs.github.com/en/rest/git) to create blobs, trees, and commits programmatically:

```python
import json, urllib.request, base64

def gh_post(path, data):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}{path}"
    req = urllib.request.Request(url, json.dumps(data).encode(), headers, method='POST')
    return json.loads(urllib.request.urlopen(req).read())

# 1. Get current commit
ref = json.loads(urllib.request.urlopen(get_req('/git/refs/heads/main')).read())
base_sha = ref['object']['sha']

# 2. Create blobs
blobs = [gh_post('/git/blobs', {"content": file_content, "encoding": "utf-8"}) 
         for file_path, file_content in files.items()]

# 3. Create tree, commit, update ref
tree_items = [{"path": p, "mode": "100644", "type": "blob", "sha": b['sha']} 
              for (p, _), b in zip(files.items(), blobs)]
tree = gh_post('/git/trees', {"base_tree": base_sha, "tree": tree_items})
commit = gh_post('/git/commits', {"message": "Deploy", "tree": tree['sha'], "parents": [base_sha]})
gh_mutate('PATCH', '/git/refs/heads/main', {"sha": commit['sha']})
```

**Binary files** (audio MP3s, images) need base64 encoding. The API accepts up to 100MB per blob.

**⚠️ Warning:** The Git Data API doesn't trigger GitHub Pages rebuilds as reliably as a standard `git push`. You may need to wait 3-5 minutes for Pages to detect the new commit. I've had builds take 10+ minutes.

---

## 4. Multi-Language RSS (One Template to Rule Them All)

A podcast with 4 languages means 4 RSS feeds. The 11ty approach: one Nunjucks RSS template, one page per language:

```
src/en/podcast.njk → /podcast/podcast.xml    (English)
src/cn/podcast.njk → /cn/podcast.xml         (Chinese)
src/ar/podcast.njk → /ar/podcast.xml         (Arabic)
src/es/podcast.njk → /es/podcast.xml         (Spanish)
```

Each page has a `lang` and `lang_prefix` variable. The RSS template uses these to generate language-appropriate metadata.

**Lessons learned:**
- iTunes tags (`<itunes:author>`, `<itunes:summary>`, `<itunes:category>`) are validated by Apple's submission checker. If they're missing or malformed, the submission silently fails.
- Each RSS feed needs its own `<itunes:email>` — Deezer and Anghami send verification codes to this address.
- Arabic RSS needs `<language>ar</language>` — Anghami validates this tag and rejects the English feed.
- Cover art must be 1400×1400 to 3000×3000, JPEG or PNG, under 500KB.
- Add `<lastBuildDate>` — without it, some podcast directories re-scan your feed less frequently.

---

## 5. The Blog Integration (Layout Inheritance Is a Trap)

Adding a blog to a podcast site sounds simple: create some markdown files, add a list page, done.

But if your blog page inherits the podcast layout, you get the entire episode list rendered on your blog index page. Every episode description. Every audio player. The blog index becomes a podcast page with a blog header.

**The fix:** A separate minimal layout for blog pages. My `blog-layout.njk` has:
- The same navigation bar
- Proper article typography CSS (headings, paragraphs, code blocks, tables, blockquotes)
- No episode rendering
- No cover art hero
- A "Back to Blog" link

**Article content styling is non-trivial:** Default markdown-to-HTML rendering produces unstyled `<h1>`, `<p>`, `<ul>`, `<pre>`, `<blockquote>`, and `<table>` elements. Each needs explicit CSS. Things I forgot initially:
- Code blocks (`<pre><code>`) need `overflow-x: auto` for horizontal scroll
- Tables need `border-collapse: collapse` with visible borders and header styling
- Blockquotes need a left border, italic text, and distinct background
- Article images need `max-width: 100%` and rounded corners
- Links in articles need a distinct color from nav links

---

## 6. Design System on GitHub Pages (It's Possible, It's Painful)

I rebuilt the entire visual design using references from 5 premium design systems (Apple, Linear, RunwayML, ElevenLabs, Spotify). All within the constraints of pure HTML/CSS on GitHub Pages — no build-time CSS processing, no design tokens, no component library.

**What worked:**
- Apple's `-apple-system` font stack (no external font loading needed)
- Pure black `#000000` backgrounds with `rgba(255,255,255,0.05)` borders for the dark theme
- `backdrop-filter: blur(20px)` on the fixed navigation bar (works in all modern browsers)
- Inter font from Google Fonts for body text
- A single accent color (`#d4a747` — aged gold) for all interactive elements

**What didn't:**
- Relative path images in CSS (`url('/images/bg.jpg')`) — absolute paths only
- `backdrop-filter` doesn't work in Firefox's Reader View
- GitHub Pages has no build-time CSS processing, so no CSS variables in old browsers

---

## The Deployment Checklist

After 20+ deployments, here's my current workflow:

```bash
# 1. Edit content (episodes.json, blog post, etc.)
# 2. Build
npm run build

# 3. Copy output to root
cp -r _site/* .

# 4. Deploy
./deploy.sh

# 5. Wait (30-120 seconds for GitHub Pages)
# 6. Verify
curl -sI https://project.github.io/repo/blog/ | grep "HTTP/2 200"
curl -sI https://project.github.io/repo/podcast/podcast.xml | grep "HTTP/2 200"
```

**My deploy.sh does these critical things:**
1. Builds 11ty
2. Copies `_site/*` to root (because Pages serves from root, not `_site/`)
3. Pushes `.nojekyll` (forgot this once, never again)
4. Pushes all files via Git Data API (no `git` CLI needed)
5. Includes `src/` for versioning

---

## The Realest Lesson

GitHub Pages is **free, fast, and good enough** for a podcast + blog combo. But it's not a CMS, not a podcast host, and not a design tool. Every non-trivial feature requires a workaround.

The three things I wish I'd known from day one:
1. Add `.nojekyll` before anything else — it's the root of so many silent failures
2. Store your base URL as a variable and use it everywhere — never write `href="/..."` on a Project Page
3. Test the RSS feed with [Cast Feed Validator](https://castfeedvalidator.com) before submitting to any directory — one missing tag costs you 48+ hours of approval wait time

---

*Sheherazade's Lantern is live at [bossman-lab.github.io/sheherazades-lantern](https://bossman-lab.github.io/sheherazades-lantern/) — 6 published episodes in 4 languages, with 4 more in draft. RSS feeds for all 4 languages. Blog with 2 technical posts. All on GitHub Pages. All learned the hard way.*
