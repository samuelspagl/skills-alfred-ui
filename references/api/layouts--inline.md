# inline Layout

[Official source](https://www.alfredapp.com/help/alfredui/layouts/inline/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Horizontal layout gives children desired widths and available height; vertical gives desired heights and available width. The largest cross-axis child determines desired cross-axis size. Spacing separates sequential children. Position and stretch constraints refine each child's placement. This is a single sequential arrangement; wrapping is not documented.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `direction` | Properties | ENUM | Default: "horizontal" | "horizontal", "vertical" | [§](https://www.alfredapp.com/help/alfredui/layouts/inline/#property-direction) |
| `padding` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/inline/#property-padding) |
| `spacing` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/inline/#property-spacing) |

## Related local references

- [Constraints](layouts--constraints.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
