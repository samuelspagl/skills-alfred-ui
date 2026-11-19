# flex Layout

[Official source](https://www.alfredapp.com/help/alfredui/layouts/flex/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Children are explicitly assigned grid row/column positions, spans and resizing weights. Rows and cols configure the containing view. Weight zero is the default; positive weights distribute remaining space. A spanning component's weight is divided across its span, and the largest weight specified for a shared row/column wins. Prefer simpler nested layouts when explicit grid control is unnecessary. Flex uses constraints.grid, unlike equal-cell grid layout. Range limits for coordinates and layout dimensions differ; the docs do not define out-of-grid handling.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `rows` | Properties | INTEGER | Default: 2 , Range: 1-128 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/flex/#property-rows) |
| `cols` | Properties | INTEGER | Default: 2 , Range: 1-128 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/flex/#property-cols) |
| `padding` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/flex/#property-padding) |
| `spacing` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/flex/#property-spacing) |
| `grid` | Constraints | OBJECT | Required for flex layout | — | [§](https://www.alfredapp.com/help/alfredui/layouts/flex/#property-grid) |
| `grid.col` | Constraints | INTEGER | Default: 0 , Range: 0-1024 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/flex/#property-grid-col) |
| `grid.row` | Constraints | INTEGER | Default: 0 , Range: 0-1024 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/flex/#property-grid-row) |
| `grid.colspan` | Constraints | INTEGER | Default: 1 , Range: 1-1024 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/flex/#property-grid-colspan) |
| `grid.rowspan` | Constraints | INTEGER | Default: 1 , Range: 1-1024 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/flex/#property-grid-rowspan) |
| `grid.colweight` | Constraints | DOUBLE | Default: 0.0 , Range: 0.0-1.0 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/flex/#property-grid-colweight) |
| `grid.rowweight` | Constraints | DOUBLE | Default: 0.0 , Range: 0.0-1.0 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/flex/#property-grid-rowweight) |

## Related local references

- [border Layout](layouts--border.md)
- [inline Layout](layouts--inline.md)
- [view Component](components--view.md)
- [Constraints](layouts--constraints.md)
- [Alfred UI Components](components.md)
- [stack Layout](layouts--stack.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
