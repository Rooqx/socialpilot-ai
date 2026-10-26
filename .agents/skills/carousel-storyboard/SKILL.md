---
name: carousel-storyboard
description: "Transform an idea into a slide-by-slide narrative for Instagram carousels or LinkedIn document posts."
---

# Carousel Storyboard

**Purpose.** A coherent slide script with meaningful pacing, one key message per slide and verified sources.

**Trigger and ownership.** When user asks for carousel, swipe post or LinkedIn document-style slide post.

**Inputs.** One takeaway, platform, target slide range (flexible), brand voice, proof and optional approved imagery.

## Required process

1. Decide platform and audience. An Instagram multi-image carousel and a LinkedIn PDF/document have different packaging and export needs.
2. Choose an arc: value stack, practical walkthrough, problem-proof, annotated comparison, data story or short case study.
3. Write a cover that states the deliverable. Make each interior slide advance the argument with a headline, short copy and one visual purpose.
4. Break heavy slides into two rather than shrinking text; check contrast, reading order, margins and mobile legibility.
5. Write a grounded close with one relevant next step, not guaranteed-saves gimmicks.
6. For every slide add `claim_refs`, `visual_idea`, `hierarchy`, `alt_text` intent and speaker/context notes; keep unsourced numerical data out.
7. Handoff to `visual-brief` then optional `visual-asset-production`. A storyboard is text, not rendered image files.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Structured per-slide storyboard plus cover, close, platform packaging and creative validation checklist.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

No copied copyrighted slides and no statement that prompts/storyboards equal final artwork.

## Acceptance tests

- Cover payoff honored.
- legible slide density.
- sources by claim.
- optional visual generation unambiguously separate.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
