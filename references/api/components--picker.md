# picker Component

[Official source](https://www.alfredapp.com/help/alfredui/components/picker/) · Checked 2026-11-19 · [Index](../../INDEX.md)

`items` contains item objects. Each selectable item's `value` is its unique underlying string, while `text` is the visible caption; omitting text can create a blank option. Separator items ignore text and value. Set `selected` to a value string, but its getter returns an object containing text and value. Read nested selected.value or selected.text. `changed` fires on selection changes. Functions move selection to the first, last, previous or next item. Border shape is marked macOS 26+ and depends on bordered=true. Getter return structure must not be confused with the setter schema.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `items` | Properties | ARRAY | Of type: OBJECT | — | [§](https://www.alfredapp.com/help/alfredui/components/picker/#property-items) |
| `items.type` | Properties | ENUM | Default: "item" | "item", "separator" | [§](https://www.alfredapp.com/help/alfredui/components/picker/#property-items-type) |
| `items.text` | Properties | STRING [ getter ] | Recommended | — | [§](https://www.alfredapp.com/help/alfredui/components/picker/#property-items-text) |
| `items.value` | Properties | STRING [ getter ] | Unique | — | [§](https://www.alfredapp.com/help/alfredui/components/picker/#property-items-value) |
| `selected` | Properties | STRING [ getter ] | setter: item value | — | [§](https://www.alfredapp.com/help/alfredui/components/picker/#property-selected) |
| `font` | Properties | FONT \| null | null → default font | — | [§](https://www.alfredapp.com/help/alfredui/components/picker/#property-font) |
| `bordered` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/components/picker/#property-bordered) |
| `bordershape` | Properties | ENUM | Default: "auto" , macOS 26+ | "auto", "capsule", "roundedrectangle" | [§](https://www.alfredapp.com/help/alfredui/components/picker/#property-bordershape) |
| `selectfirst` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/picker/#property-selectfirst) |
| `selectlast` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/picker/#property-selectlast) |
| `selectprevious` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/picker/#property-selectprevious) |
| `selectnext` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/picker/#property-selectnext) |

## Component-specific triggers

`changed`. Semantics are described above.

## Related local references

- [Getters](properties--getters.md)
- [FONT Property Type](properties--font.md)
- [Shared Properties](components--shared-properties.md)
- [Events](events.md)
- [functions Action](actions--json--functions.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
