# form Layout

[Official source](https://www.alfredapp.com/help/alfredui/layouts/form/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Children are paired into two columns. The left column uses the widest left item; the right receives remaining width. Each row uses its tallest member. Width constraints influence a whole column and height the row. Right-aligning left-side labels is a useful authoring choice. Empty components plus insets can form gaps. The source's phrase 'two vertical rows' conflicts with its column explanation; the documented resizing behavior describes columns.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `padding` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/form/#property-padding) |
| `spacing` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/form/#property-spacing) |

## Related local references

- [Constraints](layouts--constraints.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
