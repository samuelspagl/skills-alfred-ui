# imageview Component

[Official source](https://www.alfredapp.com/help/alfredui/components/imageview/) · Checked 2026-11-19 · [Index](../../INDEX.md)

IMAGE selects the content. Fit preserves aspect ratio and can leave space; fill preserves it while potentially cropping; stretch may distort; centre does not resize and may crop or leave space. Content tint is relevant to tintable images such as symbols. Corner radius applies to the view, not the underlying image object. Null image removes content; null background clears the background; null tint restores its default.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `image` | Properties | IMAGE \| null [ getter ] | null → remove image | — | [§](https://www.alfredapp.com/help/alfredui/components/imageview/#property-image) |
| `resize` | Properties | ENUM | Default: "fit" | "fit", "fill", "stretch", "centre" | [§](https://www.alfredapp.com/help/alfredui/components/imageview/#property-resize) |
| `background` | Properties | COLOUR \| null | null → clear background | — | [§](https://www.alfredapp.com/help/alfredui/components/imageview/#property-background) |
| `contenttintcolour` | Properties | COLOUR \| null | null → default tint | — | [§](https://www.alfredapp.com/help/alfredui/components/imageview/#property-contenttintcolour) |
| `cornerradius` | Properties | INTEGER | Default: 0 , Range: 0-32 | — | [§](https://www.alfredapp.com/help/alfredui/components/imageview/#property-cornerradius) |

## Related local references

- [Getters](properties--getters.md)
- [IMAGE Property Type](properties--image.md)
- [COLOUR Property Type](properties--colour.md)
- [Shared Properties](components--shared-properties.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
