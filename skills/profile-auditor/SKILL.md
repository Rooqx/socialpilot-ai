---
name: profile-auditor
description: "Audit and improve existing X, Instagram, and LinkedIn bios, pinned or featured content, positioning and calls to action."
---

# Profile Auditor

**Purpose.** Discoverability and credibility improvements tailored to each platform, without pretending all platforms have identical profile fields.

**Trigger and ownership.** When user requests audit, onboarding profile cleanup or consistency across platforms.

**Inputs.** Public links or text/screenshots provided; goals, niche, audience, evidence of accomplishments, available imagery.

## Required process

1. Identify which accounts are actually accessible; if a private profile cannot be read, request only the bio and visible headings needed.
2. Review consistent name/identity, unique promise, audience fit, professional evidence, link destination, CTA, and recognizable voice.
3. For LinkedIn review headline, About, featured proof, relevant roles, skills and banner. Never fabricate credentials or work history.
4. For X review concise bio, account topic signal, link, pinned post strategy and header; check actual applicable field limits at runtime.
5. For Instagram review category/bio, profile image, link, highlights, pinned content, grid cohesion and accessible visual identity.
6. Return before/after proposals and exact claims needing verification; recommend priority order by effort and expected usefulness, without predicted growth percentages.
7. Require the user's permission before making any changes to real profiles.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Per-platform findings table, proposed bios, proof gaps, visual briefs, priority actions, and verification questions.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

A link to a login-gated profile is not proof it was inspected. No automated account edits.

## Acceptance tests

- Each platform gets distinct checks.
- inaccessible profile flagged.
- bio includes only confirmed details.
- no automatic edit.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
