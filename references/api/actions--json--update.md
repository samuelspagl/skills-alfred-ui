# update Action

[Official source](https://www.alfredapp.com/help/alfredui/actions/json/update/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Ids maps component ids to property patches. Unlike remove/insert/replace, successful update only schedules layout when relayout=true. Enable it for changes that affect desired dimensions; colour-only changes ordinarily do not need it. Do not assume update changes a component's type; use replace for that.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `relayout` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/update/#property-relayout) |
| `ids` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/update/#property-ids) |

## Related local references

- [Package index](../../INDEX.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
