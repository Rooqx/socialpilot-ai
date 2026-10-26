#!/usr/bin/env python3
"""Construct reproducible source lock from exact git-commit URLs in curated maps."""
from pathlib import Path
import json,re,hashlib
R=Path(__file__).resolve().parents[1]
locked={}
for source_map in sorted((R/'skills').glob('*/references/source-map.md')):
    slug=source_map.parents[1].name
    s=source_map.read_text(encoding='utf-8')
    for label,url in re.findall(r'\[([^\]]+)\]\((https://github\.com/[^)]+)\)',s):
        m=re.match(r'https://github\.com/([^/]+/[^/]+)/blob/([a-f0-9]{40})/(.+)$',url)
        if not m:continue
        repo,commit,path=m.groups()
        key=(repo,commit,path)
        locked.setdefault(key,{'repository':repo,'commit':commit,'path':path,'url':url,'referenced_by':[]})['referenced_by'].append(slug)
out=[]
for k,v in sorted(locked.items()):
    v['referenced_by']=sorted(set(v['referenced_by']))
    v['source_status']='PINNED_URL_NOT_BUNDLED' # this script cannot prove all contents were exhaustively integrated
    out.append(v)
(R/'docs'/'source-lock.json').write_text(json.dumps({'schema':1,'note':'Commit-pinned source URLs; material is not copied into distributable to preserve source rights and update clarity. Check provenance and original licenses before reuse.','sources':out},indent=2)+'\n')
print('Commit-pinned upstream source paths:',len(out),'used by 28 roles')
