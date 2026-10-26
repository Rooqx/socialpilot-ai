---
name: x-thread-writer
description: "Outline and write coherent X threads with a strong opening, independent steps and a clear conclusion."
---

# X Thread Writer

**Purpose.** A linked narrative where every entry advances the reader’s understanding.

**Trigger and ownership.** When the topic requires sequencing beyond one X post or user explicitly requests a thread.

**Inputs.** One thesis, evidence, reader knowledge level, desired outcome and current post character limit.

## Required process

1. Determine whether a thread is necessary: multiple steps, chronology, code walkthrough or nuanced argument. Otherwise recommend a single post.
2. Choose the thread arc (problem → cause → example → solution, tutorial sequence, case study or clear argument with counterpoint).
3. Draft an opening that previews the real payoff without promising unprovided data.
4. Give each subsequent post one point, natural transitions and enough standalone context to remain understandable out of order.
5. Add concrete examples, sources and screenshots only if available; mark gaps instead of inventing case studies.
6. Conclude with the key takeaway and one relevant question/action; omit manipulative engagement bait.
7. Number and length-check every entry using verified platform rules. Pass entire thread to `fact-checker` and `post-qa` for continuity and accessibility.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Ordered thread items with per-item character counts, claims/sources map, visual suggestions and verified finish.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

Never split a paragraph arbitrarily or prescribe a rigid 7/10/12-post thread formula.

## Acceptance tests

- Each item fits limit.
- chain coherent and non-repetitive.
- statistics verified.
- accessible standalone post 1.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
