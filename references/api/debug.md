# Debug

[Official source](https://www.alfredapp.com/help/alfredui/debug/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Colourful paints layout regions for inspection. Reloadshortcut reloads an external AlfredUI instance; it does not work inside Alfred. No default for these two options is declared. Reload is a development aid, not a persistence guarantee.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `colourful` | Properties | BOOL | — | — | [§](https://www.alfredapp.com/help/alfredui/debug/#property-colourful) |
| `reloadshortcut` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/debug/#property-reloadshortcut) |

## Related local references

- [ui.json](ui-json.md)
- [Layouts](layouts.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
