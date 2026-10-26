---
name: visual-brief
description: "Create consistent branded design briefs for social images, infographic layouts, quote cards and carousel production."
---

# Visual Brief

**Purpose.** Reusable design intent that stays legible and adaptable to tools available in the current agent.

**Trigger and ownership.** When a post calls for graphical design, social card, cover slide or infographic.

**Inputs.** Approved content/storyboard, platform, brand palette/type guidance, imagery rights and actual renderer availability.

## Required process

1. Understand the message and audience before styling. Identify whether the asset is educational, illustrative, announcement or data visualization.
2. Define hierarchy, grid, copy density, whitespace, contrast, type scale, icon/diagram use and mobile legibility.
3. Translate brand identity into reproducible tokens, specifying fallback fonts and accessible contrast without distributing font files.
4. Specify correct aspect/output variants based on current platform documentation, not universal fixed templates.
5. Include per-asset text, alt-text intent, asset provenance, references for photography and permitted logos, and editing instructions.
6. Provide a structured prompt or HTML/CSS layout outline if no renderer is available. Explicitly label these as briefs, not images.
7. Hand off to `visual-asset-production` and require rendered-asset inspection before publish readiness.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Creative brief, asset manifest, design tokens, platform-specific format options, approval points and QA rubric.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

Do not enforce one aesthetic across unrelated contexts or use inaccessible tiny text.

## Acceptance tests

- All visual copy matches claims.
- aspect documented.
- contrast checklist.
- unlicensed images excluded.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
