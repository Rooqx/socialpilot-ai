# Implementation audit — development gate log

This document records what was actually built and locally tested. The baseline is the previously audited 255 `SKILL.md` sources and 28-capability comparison register in `docs/`.

## Phase 1 — Source extraction and mapping
- Input: 255 source entries from four pinned repositories, explicitly dispositioned Keep/Merge/Adapt/Defer/Reject in `source-inventory-255.csv`.
- Gate: all proposed 28 compiled skills point to named source files; deprecated compatibility redirects are not imported.
- Loop: source map produced for each skill, and independent lint cross-checks 28 roles/255 disposition rows.

## Phase 2 — Compilation
- Produced 28 original, platform-specific skill documents with frontmatter, triggers, scope, inputs, procedures, outputs, QA boundaries, recovery, and individual test cases.
- Repair loop: removed inappropriate upstream provider assumptions (BlackTwist, Gemini, Canva/HubSpot, scraped media) from mandatory paths; clarified text brief vs rendered visual and subjective scoring vs real analytics.
- Gate: file count, heading contract, manifest uniqueness, name/parent directory matching, source map and UTF-8 parser checks.

## Phase 3 — Orchestration & durable context
- Implemented single root bootstrap, first-run recovery, guarded JSON state, conflict-preserving profile updates, duplicate-key detection, QA transition, human-attested approval, manual export, reported publication and sourced metrics.
- Explicitly **not** implemented: credential-backed publishing/scheduling or real-time social analytics ingestion.
- Test-driven repair loop: (a) initial resume priority was wrong if onboarding facts still missing; now pending reviews are surfaced, (b) improved state transitions after QA/approval/export, (c) bound approval to exact SHA-256 content to prevent tampered-copy handoffs.
- Gate: functional unit tests in `tests/test_state.py`.

## Phase 4 — Portability
- Canonical skills: `.agents/skills`; complete plain-file copies for Claude: `.claude/skills` (no platform-dependent symlinks).
- Root instruction files: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`; `sync_adapters.py` detects/corrects divergence.
- Gate: 84 canonical files == 84 Claude-adapter files; **not** proof native discovery is functional without testing on real agents.

## Phase 5 — Local testing and repair
- Initial run revealed 3 issues: lint wrongly treated warnings *against* algorithm multipliers as promises; QA resume precedence ignored an existing queue; a release-label assertion expected wording not present. Repaired all.
- Adversarial tests added: post-edit approval hash mismatch, workflow transition consistency, conflicting profile facts, duplicate posts, unapproved handoff, invalid publishing links, unsourced metrics, timezone-free calendar dates, interrupted-style resume and unknown schema fail-closed.
- Run `python3 scripts/lint_skills.py`, `python3 scripts/sync_adapters.py --check`, `python3 -m unittest discover -s tests -v` and `python3 scripts/independent_release_audit.py` to recreate local verdicts.

## Phase 6 — Independent strict re-audit
- Separate `independent_release_audit.py` checks source accounting, role coverage, distinct workflows, provenance, adapter drift, security boundaries and explicit release blockers.
- **Static candidate signoff only.** Production signoff requires cold-start tests in four real agents, real author samples, actual draft-quality review, visually verified media with intended tool support, and user acceptance. Do not declare production ready until then.

## Known risks and next required external validations
1. Real agent runtime discovery and loading; a text entry file may be ignored depending on configuration or versions.
2. Real user voice calibration and content sample evaluation with the owner's consent.
3. Tool-specific output quality and accessible rendering; image generators/providers have distinct requirements.
4. Platform limits must be checked at execution time, not assumed from static docs.
5. Human-attested CLI approval does not cryptographically authenticate a human; deployment integrations should use real permissions.
6. `.social` remains local-private and is not automatically synced across machines; use secure optional backup later.
7. GitHub destination and permissions have not been selected. No GitHub mutation in this build.
