# MENU Property Type

[Official source](https://www.alfredapp.com/help/alfredui/properties/menu/) · Checked 2026-11-19 · [Index](../../INDEX.md)

MENU describes one item; shared `menu` and `submenu` contain arrays of items. `text` gives the caption, `state` adds a tick or dash, and `action` accepts one action or an array. A submenu suppresses its parent's action. Separator entries ignore text/value according to the prose, but `value` is not a declared MENU property. Use lowercase `separator`; an introductory example uses inconsistent capitalization. Example: `[{"text":"Tools","submenu":[{"text":"Ready","state":"on"}]},{"type":"separator"}]`.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `type` | Properties | ENUM | Default: "text" | "text", "separator" | [§](https://www.alfredapp.com/help/alfredui/properties/menu/#property-type) |
| `text` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/properties/menu/#property-text) |
| `state` | Properties | ENUM | Default: "off" | "off", "on", "mixed" | [§](https://www.alfredapp.com/help/alfredui/properties/menu/#property-state) |
| `submenu` | Properties | ARRAY | Of type: menu | — | [§](https://www.alfredapp.com/help/alfredui/properties/menu/#property-submenu) |
| `action` | Properties | ACTION \| ARRAY | — | — | [§](https://www.alfredapp.com/help/alfredui/properties/menu/#property-action) |

## Related local references

- [Alfred UI Components](components.md)
- [Shared Properties](components--shared-properties.md)
- [popupmenu Action](actions--json--popupmenu.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
