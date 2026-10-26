---
name: reel-scriptwriter
description: "Write concise Instagram Reel scripts with timestamps, scenes, voiceover, on-screen captions and production notes."
---

# Reel Scriptwriter

**Purpose.** A shootable/editable short-video script with synchronized narration and visuals.

**Trigger and ownership.** When asked for Reel, short tutorial video, short-form explainer or adaptation of a post to video.

**Inputs.** Goal, audience, available footage and assets, maximum duration, narrator voice and verified information.

## Required process

1. Confirm the core takeaway, real footage available and desired length. Avoid downloading competitor videos as a hidden prerequisite.
2. Build an immediate visual or spoken opening aligned to the eventual payoff; do not invent a personal experience or result.
3. Divide into paced segments with timestamps: screen/shot, voiceover, on-screen text, supporting footage and transition.
4. Use readable captions and accessible language; mark code screencasts or UI recordings that must be captured by the user.
5. Match narration length to speaking time conservatively; revise overlong shots rather than claiming an unrealistic runtime.
6. Close with a clear takeaway and optional restrained CTA. Include shot list and editing notes suited to actual tools.
7. Check music/clip ownership, facts, text visibility and dependencies. A script is not a generated or edited video.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Timed script table, narration, subtitles, shot list, sources, asset dependencies and production/QA status.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

No unauthorized scraping, copyrighted audio copying or phantom completed footage.

## Acceptance tests

- Timestamps sum to requested duration.
- narration plausible.
- captions sync.
- missing clips marked.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
