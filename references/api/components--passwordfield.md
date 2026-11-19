# passwordfield Component

[Official source](https://www.alfredapp.com/help/alfredui/components/passwordfield/) · Checked 2026-11-19 · [Index](../../INDEX.md)

This control masks entry. `text` is documented for reading the secret in an action; the source cautions against pre-populating it. Handle values in backend logic rather than embedding credentials. Font, colour, border, background, insets and focus-ring appearance are configurable. Colour's text states a textColor default. No event-trigger table is provided on this page; do not invent one. Its example misspells triggers as trigers; authored examples should use the Events spelling.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `text` | Properties | STRING [ getter ] | — | — | [§](https://www.alfredapp.com/help/alfredui/components/passwordfield/#property-text) |
| `font` | Properties | FONT \| null | null → default font | — | [§](https://www.alfredapp.com/help/alfredui/components/passwordfield/#property-font) |
| `colour` | Properties | COLOUR | — | — | [§](https://www.alfredapp.com/help/alfredui/components/passwordfield/#property-colour) |
| `bordered` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/components/passwordfield/#property-bordered) |
| `background` | Properties | COLOUR \| null | null → clear background | — | [§](https://www.alfredapp.com/help/alfredui/components/passwordfield/#property-background) |
| `textinsets` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/passwordfield/#property-textinsets) |
| `textinsets.horizontal` | Properties | INTEGER | Default: 2 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/components/passwordfield/#property-textinsets-horizontal) |
| `textinsets.vertical` | Properties | INTEGER | Default: 4 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/components/passwordfield/#property-textinsets-vertical) |
| `focusring` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/components/passwordfield/#property-focusring) |

## Related local references

- [Getters](properties--getters.md)
- [FONT Property Type](properties--font.md)
- [COLOUR Property Type](properties--colour.md)
- [Shared Properties](components--shared-properties.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
