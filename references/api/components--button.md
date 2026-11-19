# button Component

[Official source](https://www.alfredapp.com/help/alfredui/components/button/) · Checked 2026-11-19 · [Index](../../INDEX.md)

`text` and `image` are getters as well as setters. Font null restores the default. A normal click dispatches actioned. A mousedown handler overrides that normal behavior, removing native highlighting and drag-out cancellation. `bordershape` requires bordered=true and is marked macOS 26+. `effect` is also macOS 26+. Content tint applies when the button is unbordered. Do not assume the same border-shape choices apply to picker; button additionally documents circle.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `image` | Properties | IMAGE \| null [ getter ] | null → remove image | — | [§](https://www.alfredapp.com/help/alfredui/components/button/#property-image) |
| `text` | Properties | STRING [ getter ] | Default: "Button" | — | [§](https://www.alfredapp.com/help/alfredui/components/button/#property-text) |
| `font` | Properties | FONT \| null | null → default font | — | [§](https://www.alfredapp.com/help/alfredui/components/button/#property-font) |
| `bordered` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/components/button/#property-bordered) |
| `bordershape` | Properties | ENUM | Default: "auto" , macOS 26+ | "auto", "capsule", "roundedrectangle", "circle" | [§](https://www.alfredapp.com/help/alfredui/components/button/#property-bordershape) |
| `effect` | Properties | ENUM | Default: "default" , macOS 26+ | "default", "glass" | [§](https://www.alfredapp.com/help/alfredui/components/button/#property-effect) |
| `contenttintcolour` | Properties | COLOUR \| null | null → default tint | — | [§](https://www.alfredapp.com/help/alfredui/components/button/#property-contenttintcolour) |

## Component-specific triggers

`actioned`, `mousedown`. Semantics are described above.

## Related local references

- [Shared Properties](components--shared-properties.md)
- [Getters](properties--getters.md)
- [IMAGE Property Type](properties--image.md)
- [FONT Property Type](properties--font.md)
- [COLOUR Property Type](properties--colour.md)
- [Events](events.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
