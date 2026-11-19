# grid Layout

[Official source](https://www.alfredapp.com/help/alfredui/layouts/grid/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Children fill equal-sized cells in rows beginning at the upper left. Unused cells remain empty. Desired size comes from the largest child. Available width/height are divided equally by cols/rows after spacing and padding. No overflow policy for more children than configured capacity is documented.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `rows` | Properties | INTEGER | Default: 2 , Range: 1-128 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/grid/#property-rows) |
| `cols` | Properties | INTEGER | Default: 2 , Range: 1-128 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/grid/#property-cols) |
| `padding` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/grid/#property-padding) |
| `spacing` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/grid/#property-spacing) |

## Related local references

- [Constraints](layouts--constraints.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
