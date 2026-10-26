---
name: editorial-calendar
description: "Maintain a standing cross-platform editorial calendar with draft dependencies, approvals and no destructive resets."
---

# Editorial Calendar

**Purpose.** A living calendar that shows what is due, ready, blocked, pending and already used.

**Trigger and ownership.** Weekly/monthly content planning, batching, rescheduling and returning to a campaign.

**Inputs.** Existing `.social/calendar.json`, backlog, audience pillars, capacity, dates, approvals and actual publishing capabilities.

## Required process

1. Load the existing calendar and draft statuses first. Never regenerate the whole calendar because a user says "what should I post this week?".
2. Reserve slots based on realistic creation, source checks, asset lead times and posting capacity; include evergreen reserve and topical slack.
3. Attach stable draft/idea identifiers, audience pillar, platform, format, angle, owner, due date, evidence status and approval gate to each slot.
4. Avoid collisions, double booking and duplicate content; do not count a platform adaptation as identical original work.
5. Track planned, drafting, needs_review, approved, staged and reported_published independently of external scheduling.
6. Only mark a scheduled external publication when a connected provider confirms it, otherwise produce an export and label it `manual_handoff`.
7. Extend the horizon incrementally, preserve prior approvals, and summarize changes before saving.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Calendar diff, ordered queue, dependencies, rescheduling notes, pending approvals and optional CSV export.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

No auto-publishing and no claims that merely listing a date has scheduled a post.

## Acceptance tests

- Existing calendar preserved.
- duplicate key filtered.
- pending approvals surfaced.
- future slots not fabricated as external schedules.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
