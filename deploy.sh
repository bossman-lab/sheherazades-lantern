#!/bin/bash
# Deploy script for Sheherazade's Lantern
# Usage: ./deploy.sh
# Prerequisites: edit src/_data/episodes.json first, then run this

set -e
cd "$(dirname "$0")"

echo "🔨 Building 11ty..."
npx eleventy

echo "📋 Copying to root..."
cp -r _site/* .

echo "🚀 Pushing to GitHub..."
python3 -c "
import json, os, urllib.request

TOKEN = open('secrets/github.json').read()
t = json.loads(TOKEN)['token'] if TOKEN.startswith('{') else TOKEN
OWNER = 'bossman-lab'
REPO = 'sheherazades-lantern'
R = '.'
API = f'https://api.github.com/repos/{OWNER}/{REPO}'

def gh(method, path, data=None):
    url = f'{API}{path}'
    h = {'Authorization': f'token {t}', 'Accept': 'application/vnd.github.v3+json'}
    b = json.dumps(data).encode() if data else None
    if data: h['Content-Type'] = 'application/json'
    req = urllib.request.Request(url, data=b, headers=h, method=method)
    with urllib.request.urlopen(req) as r:
        raw = r.read()
        return json.loads(raw) if raw else {}

head = gh('GET', '/git/refs/heads/main')
parent = head['object']['sha']
base = gh('GET', f'/git/commits/{parent}')['tree']['sha']

# Files that get deployed (built output + src data + blog)
import glob
files = ['index.html','cn/index.html','ar/index.html','es/index.html',
         'podcast/podcast.xml','cn/podcast.xml','ar/podcast.xml','es/podcast.xml',
         'sitemap.xml','robots.txt','.nojekyll']

# Also push audio files
for fp in glob.glob('audio/episodes/*.mp3', recursive=True):
    if os.path.isfile(fp):
        files.append(fp)
for fp in glob.glob('audio/assets/*.*', recursive=True):
    if os.path.isfile(fp):
        files.append(fp)

# Also push src data for versioning
for fp in glob.glob('blog/**/*', recursive=True):
    if os.path.isfile(fp):
        files.append(fp)
for root, dirs, fnames in os.walk('src'):
    for fn in fnames:
        files.append(os.path.join(root, fn))

items = []
for fp in files:
    if not os.path.exists(fp): continue
    ext = os.path.splitext(fp)[1].lower()
    if ext in ('.mp3', '.png', '.jpg', '.jpeg', '.webp'):
        with open(fp, 'rb') as f:
            import base64
            b = gh('POST', '/git/blobs', {'content': base64.b64encode(f.read()).decode(), 'encoding': 'base64'})
    else:
        with open(fp, 'rb') as f:
            b = gh('POST', '/git/blobs', {'content': f.read().decode('utf-8','replace'), 'encoding': 'utf-8'})
    items.append({'path': fp, 'mode': '100644', 'type': 'blob', 'sha': b['sha']})

tree = gh('POST', '/git/trees', {'base_tree': base, 'tree': items})
cm = gh('POST', '/git/commits', {
    'message': 'Update podcast content',
    'tree': tree['sha'], 'parents': [parent]
})
gh('PATCH', '/git/refs/heads/main', {'sha': cm['sha'], 'force': False})
print('✅ Published!')
"
echo "✅ Deployment complete!"
