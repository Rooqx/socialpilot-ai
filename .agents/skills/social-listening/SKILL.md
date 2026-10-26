---
name: social-listening
description: "Monitor publicly accessible social conversations and questions to find relevant topics and thoughtful engagement opportunities."
---

# Social Listening

**Purpose.** High-signal listening briefs without spam, unauthorized scraping or pretending engagement has occurred.

**Trigger and ownership.** Requests for trending questions, relevant discussions, mentions or community engagement opportunities.

**Inputs.** Chosen themes, saved watchlist, permitted public feeds and timestamps, user-selected cadence if any.

## Required process

1. Confirm which platforms and keywords are in scope, and the intended listening purpose (ideas, customer language, mentions or helpful replies).
2. Use permitted platform/search access; skip logged-in or prohibited scraping when no authorized tool exists. State coverage, source dates and gaps.
3. Collect candidate discussions with URL, timestamp, author-publicness, theme and a short paraphrase rather than unnecessarily storing personal data.
4. Rank by topic relevance, recency, opportunity to add genuine value and evidence quality—not solely follower count or outrage.
5. Mark duplicates against previous discoveries and backlog IDs so repeat runs do not re-surface the same opportunity.
6. Pass ideas to `idea-pipeline` and draft optional thoughtful replies via `community-engagement`; wait for permission before sending.
7. No always-on monitoring unless an actual scheduler/automation has been configured and confirmed.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Attributed opportunities list, research caveats, duplicate exclusions, suggested post angles and optional reply drafts.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

No automatic follows/comments/DMs and no promises to watch in the background.

## Acceptance tests

- Duplicate mention filtered.
- no authorized feed yields manual fallback.
- replies stay drafts.
- timeframe respected.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
