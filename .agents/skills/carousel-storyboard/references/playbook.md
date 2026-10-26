# Slide-level narrative and production spec

## Choose one spine

A **walkthrough** requires sequential steps; a **problem–proof** arc needs verified evidence; a **value stack** needs distinct useful takeaways; a **comparison** needs fair alternatives and consistent criteria; a **case study** needs true observed project details. Choose before designing visuals.

## Slide schema

Every slide must specify `number`, `purpose`, `headline`, `body_copy`, `visual_direction`, `evidence_refs`, `accessibility_note`, and `status`. On-screen copy should be intentionally shorter than explanatory speaker notes. Avoid shrinking text to fit a predetermined count; split slides instead.

## Production sequence

1. Determine platform and format (Instagram image set vs LinkedIn document/PDF); check real platform rules separately.
2. Write cover promise and final takeaway. Confirm the intermediate slides actually fulfill the promise.
3. Draft a content-only outline with one major idea per slide, including citations for statistical or factual illustrations.
4. For each slide add a visual purpose—diagram, code screenshot, annotated interface, illustration, or simple typographic emphasis. Do not use art merely to fill whitespace.
5. Inspect reading order, contrast, type size and safe margins on a mobile-sized preview once visual assets are produced.
6. Produce a slide manifest for the renderer, with consistent brand tokens and export requirements.

## Example outline

Theme: "Why a successful retry can be unsafe." Slide 1—promise; 2—request and timeout; 3—server may already have applied the operation; 4—retry duplicates side effects; 5—idempotency key concept; 6—tradeoffs and failure cases; 7—operational checklist. An imagined graph or test statistic must not appear without actual data.

## Failures to catch

The cover promises five checks but the deck contains four; a slide introduces a new unsupported fact; copy and visual imply contradictory outcomes; the exported dimensions are wrong; the package has no per-slide asset paths. A storyboard must remain `brief_only` until actual assets are verified.
