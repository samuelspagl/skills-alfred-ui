# SHORTCUT Property Type

[Official source](https://www.alfredapp.com/help/alfredui/properties/shortcut/) · Checked 2026-11-19 · [Index](../../INDEX.md)

A SHORTCUT object pairs a key-equivalent string with one action or an action array. View `shortcuts` work when focus is in a descendant. Modifier symbols include ⌘, ⇧, ⌃, ⌥ and ↩︎. The precedence statement combines 'deepest' with 'root', so collision behavior is unclear; avoid competing assignments until tested. Component `shortcut` is a separate native key-equivalent mechanism. Example: `{"shortcut":"⌘K","action":{"type":"function","src":"editor","args":"caretstart"}}`.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `shortcut` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/properties/shortcut/#property-shortcut) |
| `action` | Properties | ACTION \| ARRAY | — | — | [§](https://www.alfredapp.com/help/alfredui/properties/shortcut/#property-action) |

## Related local references

- [view Component](components--view.md)
- [Actions](actions.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
