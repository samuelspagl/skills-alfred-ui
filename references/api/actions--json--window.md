# window Action

[Official source](https://www.alfredapp.com/help/alfredui/actions/json/window/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Resize sets content dimensions, excluding toolbar sizing. Each dimension can be an integer or auto to calculate from content. Null or omission retains the current dimension, even though null is absent from the header's type union. This command is separate from the initial Window configuration and from Window functions.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `resize` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/window/#property-resize) |
| `resize.width` | Properties | INTEGER \| "auto" | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/window/#property-resize-width) |
| `resize.height` | Properties | INTEGER \| "auto" | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/window/#property-resize-height) |

## Related local references

- [Package index](../../INDEX.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
