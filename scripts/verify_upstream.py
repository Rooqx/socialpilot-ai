#!/usr/bin/env python3
"""Opt-in source verification; no credentials, no committing upstream text.

Usage:
  python3 scripts/verify_upstream.py --check-manifest     # offline
  python3 scripts/verify_upstream.py --fetch --limit 5    # permitted public network only

Fetch mode verifies Git blob SHA against returned GitHub content object; cache is gitignored.
Not part of local release tests because network connectivity is optional.
"""
import argparse, hashlib,json,sys,urllib.request,urllib.error
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def git_blob_sha(content):return hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--check-manifest',action='store_true');p.add_argument('--fetch',action='store_true');p.add_argument('--limit',type=int,default=0);args=p.parse_args()
 sources=json.loads((ROOT/'docs/source-lock.json').read_text())['sources']
 assert len(sources)>=30,'Unexpectedly small pinned source set'
 assert len({(x['repository'],x['commit'],x['path']) for x in sources})==len(sources),'duplicate source'
 for x in sources:
  assert len(x['commit'])==40 and x['path'].endswith('.md')
 if not args.fetch:
  print(json.dumps({'source_count':len(sources),'online_verified':False,'manifest_check':'PASS'}));return 0
 from urllib.parse import quote
 cache=ROOT/'.source-cache';cache.mkdir(exist_ok=True)
 results=[]
 for x in (sources[:args.limit] if args.limit else sources):
  repo,commit,path=x['repository'],x['commit'],x['path']
  url=f'https://api.github.com/repos/{repo}/contents/{quote(path)}?ref={commit}'
  req=urllib.request.Request(url,headers={'Accept':'application/vnd.github+json','User-Agent':'social-agent-source-audit/0.3'})
  try:
   with urllib.request.urlopen(req,timeout=15) as response:meta=json.load(response)
   import base64
   raw=base64.b64decode(meta['content'].replace('\n',''))
   assert meta['sha']==git_blob_sha(raw),'content SHA mismatch'
   filename=cache/(hashlib.sha256((repo+commit+path).encode()).hexdigest()+'.md')
   filename.write_bytes(raw)
   results.append({'path':f'{repo}/{path}','sha':meta['sha'],'result':'verified'})
  except (OSError,KeyError,ValueError,AssertionError) as e:
   results.append({'path':f'{repo}/{path}','result':'error','reason':str(e)[:200]})
 print(json.dumps({'attempted':len(results),'verified':sum(x['result']=='verified' for x in results),'results':results},indent=2))
 return 0 if all(x['result']=='verified' for x in results) else 1
if __name__=='__main__':sys.exit(main())
