# insert Action

[Official source](https://www.alfredapp.com/help/alfredui/actions/json/insert/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Ids maps parent view ids to arrays of new component objects. Children append to the parent's components array. Successful insertion schedules the entire UI for layout. Ensure inserted ids remain unique; insertion position parameters are not documented for this UI command (the data-provider insert is different).

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `ids` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/insert/#property-ids) |

## Related local references

- [Alfred UI Components](components.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
