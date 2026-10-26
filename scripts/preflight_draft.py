#!/usr/bin/env python3
"""Deterministic preflight for obvious draft-format issues. NOT a fact checker or reach prediction.

Usage: python3 scripts/preflight_draft.py --platform x --text-file draft.txt
       python3 scripts/preflight_draft.py --platform linkedin --text-file draft.txt --strict
"""
import argparse,json,re,sys
from pathlib import Path
PLATFORMS={'x','linkedin','instagram'}
def preflight(text,platform,expanded_x=False):
 warnings=[];blocking=[];len_text=len(text)
 if not text.strip():blocking.append('empty draft')
 if re.search(r'(?i)(?:\b(?:TODO|TBD|lorem ipsum)\b|\[insert[^\]]*\]|\{\{[^}]+\}\})',text):
  blocking.append('unresolved placeholder detected')
 if platform=='x':
  cap=25000 if expanded_x else 280
  if len_text>cap:blocking.append(f'{len_text} Unicode codepoints exceeds conservative {cap} limit; exact X weighted count may differ')
  if expanded_x:warnings.append('Long-post entitlement must be verified on the account before handoff')
  if re.search(r'https?://',text):warnings.append('X URL character weighting differs from raw codepoint count; verify in live composer')
 if platform=='linkedin' and len_text>3000:blocking.append(f'{len_text} characters exceeds LinkedIn post limit of 3000; use article/document or shorten')
 if platform=='instagram':warnings.append('Verify current account format, caption limits and asset availability before publication')
 if re.search(r'(?:\b\d+(?:\.\d+)?%|\$\d[\d,]*)',text):warnings.append('Quantitative claim requires independent claim-by-claim evidence review')
 if re.search(r'\b(?:I|we|my|our|we\x27ve|I\x27ve)\b',text,re.I):warnings.append('First-person narrative requires author confirmation for attributed experiences')
 if re.search(r'(?i)(?:guaranteed?\s+(?:reach|views|followers)|\bviral hack\b)',text):warnings.append('Potential ungrounded performance guarantee requires editorial review')
 if len(re.findall(r'[!?]{3,}',text))>=2:warnings.append('Excessive punctuation may signal engagement bait')
 return {'platform':platform,'length_codepoints':len_text,'blocking_issues':blocking,'warnings':warnings,'status':'blocked' if blocking else 'format_pass_editorial_review_required','notice':'A passing format check does not verify claims, media files, ownership, user approval or posting.'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--platform',choices=sorted(PLATFORMS),required=True);p.add_argument('--text-file',required=True);p.add_argument('--expanded-x',action='store_true');p.add_argument('--strict',action='store_true');a=p.parse_args()
 out=preflight(Path(a.text_file).read_text(encoding='utf8'),a.platform,a.expanded_x)
 print(json.dumps(out,indent=2,ensure_ascii=False))
 return 2 if a.strict and out['blocking_issues'] else 0
if __name__=='__main__':sys.exit(main())
