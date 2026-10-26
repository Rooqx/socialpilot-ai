---
name: content-repurposer
description: "Convert one approved source insight into distinct native X, Instagram, and LinkedIn formats without copying text verbatim."
---

# Content Repurposer

**Purpose.** Preserve original meaning while giving each platform a reason to exist.

**Trigger and ownership.** When user asks to repurpose a blog, video, project update, thread, existing post or content batch.

**Inputs.** Original authored material and ownership, main insight, verified claims, target platforms, voice and formats.

## Required process

1. Extract the core claims, evidence, examples, assets and copyright constraints from the approved source.
2. Identify standalone sub-insights with enough substance to merit separate posts; do not split into filler.
3. For X produce concise observation or thread; for LinkedIn produce professional takeaway with proof; for Instagram choose a visual narrative/carousel or video plus matching caption.
4. Tailor hook, depth, CTA and storytelling while retaining factual meaning and voice. Map each adaptation to original source and note what was added.
5. Detect duplicate published themes and avoid repeating identical writing on the same account within the chosen period.
6. Pass all derivative claims through factual QA; identify visual production needs and explicit original attribution where relevant.
7. Save a content-family ID so analytics can compare formats without counting variants as independent ideas.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Cross-platform adaptation plan, content-family ID, native drafts, source-to-claim trace, duplicate alerts and asset dependencies.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

No fabricated additional personal stories or unlicensed third-party repurposing.

## Acceptance tests

- Derivatives have distinct platform value.
- claims identical in substance.
- source linkage present.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
