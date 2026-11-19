# border Layout

[Official source](https://www.alfredapp.com/help/alfredui/layouts/border/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Child constraints.region selects top, right, bottom, left or centre. Regions may be empty. Top/bottom span the full width at desired height; left/right use desired width and the remaining height; centre receives what remains. Place nested views in regions to compose more complex layouts. Behavior for multiple children assigned to the same region is not specified.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `padding` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/border/#property-padding) |
| `spacing` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/border/#property-spacing) |
| `region` | Constraints | ENUM | Required for border layout | "top", "right", "bottom", "left", "centre" | [§](https://www.alfredapp.com/help/alfredui/layouts/border/#property-region) |

## Related local references

- [Alfred UI Components](components.md)
- [view Component](components--view.md)
- [Constraints](layouts--constraints.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
