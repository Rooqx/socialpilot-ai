#!/usr/bin/env python3
"""Synchronize real files from visible `skills/` to agent discovery paths.

The `skills/` directory is authoritative; `.agents/skills` and
`.claude/skills` are generated, cross-platform copies. No symlinks needed.
"""
import argparse, hashlib, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
CANON = ROOT / 'skills'
ADAPTERS = [ROOT / '.agents' / 'skills', ROOT / '.claude' / 'skills']

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def run(check=False):
    issues=[];updates=[]
    canonical={p.relative_to(CANON):p for p in CANON.rglob('*') if p.is_file()}
    if not canonical:
        print('FAIL: visible skills directory is empty')
        return 1
    for adapter in ADAPTERS:
        for rel,source in sorted(canonical.items()):
            destination=adapter/rel
            if not destination.exists() or digest(source)!=digest(destination):
                if check:
                    issues.append(str(destination.relative_to(ROOT)))
                else:
                    destination.parent.mkdir(parents=True,exist_ok=True)
                    destination.write_bytes(source.read_bytes())
                    updates.append(str(destination.relative_to(ROOT)))
        extras={p.relative_to(adapter) for p in adapter.rglob('*') if p.is_file()}-set(canonical)
        for rel in sorted(extras):
            if check:
                issues.append('unexpected_adapter:'+str((adapter/rel).relative_to(ROOT)))
            else:
                (adapter/rel).unlink()
                updates.append('deleted:'+str((adapter/rel).relative_to(ROOT)))
    print(('PASS: both agent adapters match visible skills/' if not issues else 'FAIL: adapters differ from skills/') if check else f'SYNCHRONIZED {len(updates)} files')
    for issue in issues:print('DIFF',issue)
    return int(bool(issues))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    sys.exit(run(args.check))
