# label Component

[Official source](https://www.alfredapp.com/help/alfredui/components/label/) · Checked 2026-11-19 · [Index](../../INDEX.md)

A label is short read-only text, optionally selectable. Text is a getter. Line-break modes either truncate at the head/middle/tail, wrap by word/character, or clip. Alignment uses British-spelled centre; natural follows the text's natural direction. Null colour and font restore their defaults.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `text` | Properties | STRING [ getter ] | — | — | [§](https://www.alfredapp.com/help/alfredui/components/label/#property-text) |
| `colour` | Properties | COLOUR \| null | null → default text colour | — | [§](https://www.alfredapp.com/help/alfredui/components/label/#property-colour) |
| `font` | Properties | FONT \| null | null → default font | — | [§](https://www.alfredapp.com/help/alfredui/components/label/#property-font) |
| `selectable` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/components/label/#property-selectable) |
| `linebreak` | Properties | ENUM | Default: "truncatetail" | "truncatehead", "truncatemiddle", "truncatetail", "wordwrap", "charwrap", "clip" | [§](https://www.alfredapp.com/help/alfredui/components/label/#property-linebreak) |
| `textalign` | Properties | ENUM | Default: "natural" | "left", "right", "centre", "justify", "natural" | [§](https://www.alfredapp.com/help/alfredui/components/label/#property-textalign) |

## Related local references

- [Getters](properties--getters.md)
- [COLOUR Property Type](properties--colour.md)
- [FONT Property Type](properties--font.md)
- [Shared Properties](components--shared-properties.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
