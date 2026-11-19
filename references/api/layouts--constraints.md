# Constraints

[Official source](https://www.alfredapp.com/help/alfredui/layouts/constraints/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Region is required for border children; grid is required for flex children. Position refines placement within allotted space; fit normally fills it. Stretch only applies when position is not fit. Insets add outside spacing and contribute to calculated desired size. Size overrides desired size; an integer sets both dimensions, while an object can set width/height. Zero means automatic. These are layout hints rather than unconditional frame dimensions. Grid coordinates and spans determine placement; weights control resizing. Do not put region, grid or position directly on the component outside constraints.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `region` | Properties | ENUM | Required for border layout | "top", "right", "bottom", "left", "centre" | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-region) |
| `position` | Properties | ENUM | Default: "fit" | "fit", "centre", "top", "right", "bottom", "left", "topright", "bottomright", "bottomleft", "topleft" | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-position) |
| `stretch` | Properties | ENUM | Default: "none" | "none", "horizontal", "vertical" | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-stretch) |
| `grid` | Properties | OBJECT | Required for flex layout | — | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-grid) |
| `grid.col` | Properties | INTEGER | Default: 0 , Range: 0-1024 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-grid-col) |
| `grid.row` | Properties | INTEGER | Default: 0 , Range: 0-1024 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-grid-row) |
| `grid.colspan` | Properties | INTEGER | Default: 1 , Range: 1-1024 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-grid-colspan) |
| `grid.rowspan` | Properties | INTEGER | Default: 1 , Range: 1-1024 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-grid-rowspan) |
| `grid.colweight` | Properties | DOUBLE | Default: 0.0 , Range: 0.0-1.0 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-grid-colweight) |
| `grid.rowweight` | Properties | DOUBLE | Default: 0.0 , Range: 0.0-1.0 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-grid-rowweight) |
| `insets` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-insets) |
| `insets.top` | Properties | INTEGER | Default: 0 , Range: 0-128 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-insets-top) |
| `insets.right` | Properties | INTEGER | Default: 0 , Range: 0-128 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-insets-right) |
| `insets.bottom` | Properties | INTEGER | Default: 0 , Range: 0-128 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-insets-bottom) |
| `insets.left` | Properties | INTEGER | Default: 0 , Range: 0-128 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-insets-left) |
| `size` | Properties | OBJECT \| INTEGER | — | — | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-size) |
| `size.width` | Properties | INTEGER | Default: 0 , use 0 for automatic sizing. | — | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-size-width) |
| `size.height` | Properties | INTEGER | Default: 0 , use 0 for automatic sizing. | — | [§](https://www.alfredapp.com/help/alfredui/layouts/constraints/#property-size-height) |

## Related local references

- [Alfred UI Components](components.md)
- [Layouts](layouts.md)
- [border Layout](layouts--border.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
