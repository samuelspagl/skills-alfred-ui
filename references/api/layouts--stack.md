# stack Layout

[Official source](https://www.alfredapp.com/help/alfredui/layouts/stack/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Children overlap, with the first at the back and the last at the front. Each receives the view's space; constraints can refine placement. The largest child's desired size determines the container's desired size. Padding applies; spacing is not listed as a stack-specific property.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `padding` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/layouts/stack/#property-padding) |

## Related local references

- [view Component](components--view.md)
- [Constraints](layouts--constraints.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
