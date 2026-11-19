# textfield Component

[Official source](https://www.alfredapp.com/help/alfredui/components/textfield/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Text is a getter. User edits dispatch changed; return dispatches actioned; a pause in typing dispatches typingstopped. `multiline` allows newlines via Option-Return or Shift-Return. `linebreak` controls horizontal scrolling versus wrapping. Insets are horizontal and vertical pairs; vertical inset affects desired height. Editable and selectable have no declared defaults. Null font/colour restore defaults; null background clears it. The example's bordertype is not a declared textfield property; use bordered. A desired size is a layout hint, not a guaranteed fixed frame.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `multiline` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/components/textfield/#property-multiline) |
| `text` | Properties | STRING [ getter ] | — | — | [§](https://www.alfredapp.com/help/alfredui/components/textfield/#property-text) |
| `font` | Properties | FONT \| null | null → default font | — | [§](https://www.alfredapp.com/help/alfredui/components/textfield/#property-font) |
| `colour` | Properties | COLOUR \| null | null → default text colour | — | [§](https://www.alfredapp.com/help/alfredui/components/textfield/#property-colour) |
| `bordered` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/components/textfield/#property-bordered) |
| `background` | Properties | COLOUR \| null | null → clear background | — | [§](https://www.alfredapp.com/help/alfredui/components/textfield/#property-background) |
| `textinsets` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/textfield/#property-textinsets) |
| `textinsets.horizontal` | Properties | INTEGER | Default: 2 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/components/textfield/#property-textinsets-horizontal) |
| `textinsets.vertical` | Properties | INTEGER | Default: 4 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/components/textfield/#property-textinsets-vertical) |
| `focusring` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/components/textfield/#property-focusring) |
| `placeholdercolour` | Properties | COLOUR \| null | null → placeholder colour reset | — | [§](https://www.alfredapp.com/help/alfredui/components/textfield/#property-placeholdercolour) |
| `placeholder` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/components/textfield/#property-placeholder) |
| `editable` | Properties | BOOL | — | — | [§](https://www.alfredapp.com/help/alfredui/components/textfield/#property-editable) |
| `selectable` | Properties | BOOL | — | — | [§](https://www.alfredapp.com/help/alfredui/components/textfield/#property-selectable) |
| `linebreak` | Properties | "scroll" \| "wrap" | Default: "scroll" | "scroll", "wrap" | [§](https://www.alfredapp.com/help/alfredui/components/textfield/#property-linebreak) |

## Component-specific triggers

`actioned`, `changed`, `typingstopped`. Semantics are described above.

## Related local references

- [Getters](properties--getters.md)
- [FONT Property Type](properties--font.md)
- [COLOUR Property Type](properties--colour.md)
- [Shared Properties](components--shared-properties.md)
- [Events](events.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
