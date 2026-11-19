# progress Component

[Official source](https://www.alfredapp.com/help/alfredui/components/progress/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Progress is a numeric getter/setter in 0–1. Linear and round are the two styles. Thickness zero selects the style's default thickness. Colour controls the foreground, background the track/background; their null reset/removal rules differ. The official example uses color while the property declaration uses colour; use the declared spelling. Indeterminate animation is not documented by this page.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `style` | Properties | ENUM | Default: "linear" | "linear", "round" | [§](https://www.alfredapp.com/help/alfredui/components/progress/#property-style) |
| `thickness` | Properties | INTEGER | Default 0 . Range 0-32 | — | [§](https://www.alfredapp.com/help/alfredui/components/progress/#property-thickness) |
| `progress` | Properties | DOUBLE [ getter ] | Default 0.0 , Range 0.0-1.0 | — | [§](https://www.alfredapp.com/help/alfredui/components/progress/#property-progress) |
| `colour` | Properties | COLOUR \| null | null → default accent colour | — | [§](https://www.alfredapp.com/help/alfredui/components/progress/#property-colour) |
| `background` | Properties | COLOUR \| null | null → clear background | — | [§](https://www.alfredapp.com/help/alfredui/components/progress/#property-background) |

## Related local references

- [Getters](properties--getters.md)
- [COLOUR Property Type](properties--colour.md)
- [Shared Properties](components--shared-properties.md)
- [update Action](actions--json--update.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
