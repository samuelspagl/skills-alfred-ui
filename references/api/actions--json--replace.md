# replace Action

[Official source](https://www.alfredapp.com/help/alfredui/actions/json/replace/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Ids maps existing component ids to replacement component objects. Retainids defaults true: the old id is reused unless the replacement supplies its own. Successful replacement schedules the entire UI for layout. This changes the component, unlike update's property patch.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `retainids` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/replace/#property-retainids) |
| `ids` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/replace/#property-ids) |

## Related local references

- [Package index](../../INDEX.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
