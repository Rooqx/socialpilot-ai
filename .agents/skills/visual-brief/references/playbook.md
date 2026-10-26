# Design specification and acceptance criteria

## The visual brief must be implementable

Specify the purpose, audience, platform, exact content to be displayed, aspect variants, reference sources, visual hierarchy, grid, typography fallback, contrast target, image rights, editing tolerance and export acceptance tests. Separate *brand tokens* from *one-off art directions*; don't invent a client's corporate branding.

## Structured handoff

1. Confirm the intended medium: infographic, quote card, carousel slide, thumbnail or illustrated demonstration.
2. Build a content hierarchy (headline, key points, annotation, optional CTA) before colors or imagery.
3. Budget text by viewing size; identify what should be shown graphically versus in a caption.
4. Provide layout regions with clear relative sizes and safe margins. Use actual aspect dimensions only after checking current platform constraints.
5. State legibility and accessibility goals, including minimum readable text in a realistic mobile preview and meaningful alt-text suggestions.
6. Record provenance of photographs, screenshots, quotes, logos and icons; unresolved rights are a blocker to publishing.
7. Deliver `content-manifest`, `design-tokens`, `per-asset-brief`, `asset-dependencies`, and `render-checklist`.

## Example

For a deployment checklist graphic: the dominant header should identify the checklist, followed by three separated, numbered checks with concise explanatory labels. A code snippet is readable only if the target export preserves useful font size. Put extended technical nuance in the caption or linked guide rather than squeezing it into the image.

## Quality checks

A brief that only says "modern purple gradient" is insufficient. A rendered file may differ from the brief; acceptance requires actual inspection. Never claim to have generated, edited or exported graphics when only prompts or HTML instructions exist.
