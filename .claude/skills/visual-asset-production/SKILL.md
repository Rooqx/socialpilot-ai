---
name: visual-asset-production
description: "Produce or coordinate actual approved social images using available tools and verify rendered deliverables, never confusing prompts with assets."
---

# Visual Asset Production

**Purpose.** A truthfully tracked production step: produced-and-inspected, brief-only, or blocked.

**Trigger and ownership.** After approved visual brief, when user explicitly asks for actual rendered assets.

**Inputs.** Approved brief and assets with rights, available image or design tools, output paths, platform specs.

## Required process

1. Detect actual renderer capabilities and provider permissions. Do not assume Gemini, Canva, ImageGen, Python graphics, or browser automation exists in every agent.
2. Check input source rights and ensure image requests are authorized. For external accounts or paid tools ask approval where needed.
3. Render one requested asset in supported tooling, preserving the exact brief and exported dimensions. Keep editable intermediate files only where the user requested them.
4. Inspect the actual result visually for copy accuracy, layout clipping, mobile text legibility, brand coherence, spelling and copyright pitfalls.
5. Re-render after issues; do not call an asset complete until the file exists, passes inspection, and has a verified path.
6. Report production state (`rendered_verified`, `rendered_needs_revision`, `brief_only`, `blocked`) and any tool limitations.
7. Never fake a download link, filename, image URL, or claim that an unattended render succeeded.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Actual verified artifact paths when produced, inspection log, dimensions and source rights; otherwise honest brief-only handoff.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

No fabricated artifacts or automatic tool fallback into paid/unsafe providers.

## Acceptance tests

- No renderer stays brief-only.
- nonexistent file never verified.
- revision loop on clipping.
- sources and approval recorded.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
