# Real asset production and inspection

## Tool capability negotiation

Before execution, identify the runtime's available renderer and what it can genuinely output: raster image, SVG, editable slides, HTML screenshot or video. A tool that creates a *prompt* does not count as an image generator. A generated still frame does not satisfy a requested moving video.

## Render pipeline

1. Validate the approved brief: required copy, platform format, dimensions, brand assets, source rights and accessibility needs.
2. Choose a renderer appropriate to the output. If unavailable, stop at `brief_only` and provide a concrete dependency list rather than a fake path.
3. Generate the asset with a stable output name and record tool/provider, model/version when available, generation settings and source inputs.
4. Open the actual exported file. Check critical words character-by-character, cropping, text overlap, contrast, brand consistency, misleading visuals, image artifacts and rights/attribution.
5. Repair the specific defect; don't regenerate randomly without updating the brief or a targeted parameter.
6. Verify file existence, intended dimensions, output format and viewability before setting `rendered_verified`.
7. Save an asset manifest and link it to its caption/storyboard; require a new review if text is edited after art generation.

## Example state transitions

`brief_only` (no renderer) → `rendered_needs_revision` (graphic exists but caption text clipped) → `rendered_verified` (file reopened, corrected copy confirmed, metadata recorded). Each state must be supported by actual files. A presentation of an image-generation prompt remains `brief_only`.

## Edge-case tests

Generated text is misspelled; dimensions do not fit intended platform; the face/photo isn't authorized; a missing font changes line breaks; an SVG uses external files absent in the export; an AI screenshot implies the product did something it didn't. Any of these require repair or a clear block.
