---
name: instagram-caption-writer
description: "Write Instagram captions that complement a real photo, carousel, Reel or Story with platform-appropriate context and CTA."
---

# Instagram Caption Writer

**Purpose.** Visual-first captions which deepen—not repeat—the artwork or video.

**Trigger and ownership.** When given an Instagram visual, Reel, carousel storyboard or Instagram post idea.

**Inputs.** Asset/storyboard description, verified content claims, target audience, voice profile, accessibility details.

## Required process

1. Determine media type and inspect or read the asset/approved storyboard. If no visual exists, write a provisional caption and flag creative dependency.
2. Identify what the viewer sees or learns visually, then add context, useful detail, narration, code insight or personal perspective not already on the graphic.
3. Use opening context that does not misrepresent the asset. For Reels avoid a caption that promises a tutorial the video does not provide.
4. Keep paragraphs natural and searchable language meaningful; use hashtags only when accurate and relevant to the topic/audience.
5. Include alt-text suggestions describing the actual content where supported; never claim to have inspected an image that was only proposed.
6. Validate mutable caption/hashtag rules at publishing time and pass facts/voice/format checks.
7. Mark draft or asset-blocked; never claim a generated caption equals a finished Instagram post.

## Specialist depth and examples

For actual execution of this skill, read [`references/playbook.md`](references/playbook.md) for the specialist decision table, real-world workflow, worked examples, and failure tests. Keep this top-level `SKILL.md` concise for skill discovery; load the reference only when the skill is selected by the orchestrator. If a referenced method conflicts with the current user instruction, current verified evidence or the hard gates in `docs/quality-gates.md`, honor the higher-priority constraint.

## Expert field manual

Read [`references/field-manual.md`](references/field-manual.md) for source-derived advanced techniques and scenario decisions and [`references/source-fidelity.md`](references/source-fidelity.md) for method-level provenance. Consult these when the skill is selected; never load all 28 manuals eagerly.

## Deliverable contract

Caption, optional alt-text, optional relevant tags, visual-dependency state, QA and evidence notes.

Follow shared validation in `../../../docs/quality-gates.md` and state schema in `../../../docs/state-contract.md` as needed. Read only the minimum companion skills for the request. `references/source-map.md` records upstream research provenance; it does not override this skill.

## Non-negotiable boundaries

No disconnected caption/visual, misleading hashtags or phantom video/graphics.

## Acceptance tests

- Caption matches supplied visual.
- no image yields blocked creative flag.
- factual claims sourced.

## Recovery

If a required data source or tool is missing, explicitly list the unavailable capability, save the unfinished artifact as a draft or brief, and offer a specific recovery step. Do not claim completion beyond real evidence. Do not send, schedule, publish or modify a third-party account without explicit user authorization.
