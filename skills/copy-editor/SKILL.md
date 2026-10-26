---
name: copy-editor
description: "Edit social drafts for clarity, authentic voice, pacing, evidence specificity, and readability without making every writer sound generic."
---

# Copy Editor

**Purpose.** Tight and natural copy with the author’s distinctive tone intact.

**Trigger and ownership.** After drafting, before final QA, or whenever user requests polish or human-sounding edits.

**Inputs.** Original draft, voice profile, platform, author’s intent and fact-check status.

## Required process

1. Run focused sweeps for clarity, voice, usefulness, specificity, proof, flow and needless risk. Do not rewrite every sentence mechanically.
2. Remove filler, forced urgency, repetitive formatting, invented authority and generic AI patterns; preserve intentional rhetorical contrast when it actually helps.
3. Tighten headlines, logical structure and natural transitions. Prefer clear sentences to endless fragments, rigid templates or dense jargon.
4. Check that edits do not change technical meaning, verified numbers or the author's actual position; send new claims back to fact checker.
5. Apply the platform’s native reading experience: compact X, credible LinkedIn, caption supporting Instagram visuals.
6. Return edited copy and key changes; retain author feedback for future voice-profile updates with explicit confirmation.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Edited copy, reason for significant changes, remaining factual issues and voice match notes.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

No blanket ban on normal punctuation, no flattening personal voice, no invented sources.

## Acceptance tests

- Original thesis preserved.
- readability increased.
- no new unsupported claims.
- platform fit maintained.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
