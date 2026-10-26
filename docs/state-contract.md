# Persistent context and local state contract (schema v1)

`python3 scripts/socialctl.py init` creates `.social/` in this repo unless `--workspace` is specified. It is gitignored by default. Python standard library only; no external services.

| File | Content | Ownership |
|---|---|---|
| `state.json` | schema_version, lifecycle, last update | CLI |
| `profile.json` | author_name, audience, goals, platforms, explicit confirmed facts/conflicts | human + context-manager |
| `voice.json` | status, sample provenance, voice rules | voice-profiler and human confirmation |
| `strategy.json` | status, pillars, assumptions | content-strategy |
| `calendar.json` | planned-only entries keyed by draft id | editorial-calendar |
| `drafts/index.json` | stable idempotency keys to draft IDs | CLI |
| `drafts/<id>.json` | content, platform, format, QA, approval attestation, local handoff, report URL | CLI + post QA |
| `exports/<id>.json` | human-actionable manual export, **not scheduled** | CLI |
| `metrics/<id>.json` | only provided actual data with source and observation date | analytics |
| `run-log.jsonl` | append-only activity record | CLI |

**Core transitions**: `draft` --QA pass--> `needs_review` --human attestation--> `approved` --local export--> `manual_handoff` --user post URL--> `reported_published`. Changing a draft after approval invalidates both QA and approval. Publication is not verified by this CLI.

**Atomicity & concurrency**: JSON writes use temp-file + `os.replace`; `.write.lock` excludes simultaneous CLI writers. A crashed process may leave a lock. Do not delete it while another process is active. Filesystem backups and secure private storage remain the user's responsibility. Run log append and file writes are not one atomic transaction; if interrupted, recover by inspecting recorded state first.

**Profiles**: `set-profile path.json` rejects conflicting overwrites by default and logs the conflict, allowing explicit `--confirm-replacement` only after user confirmation. A profile change does not automatically imply new voice evidence. Generated state is **not committed**; syncing it between machines requires deliberate secure transfer.

**Upgrade rule**: unknown `schema_version` must halt writes. Plan and test a migration before upgrading old state; never silently reinterpret older records. A placeholder or `None` must never be treated as a confirmed fact.
