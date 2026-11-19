# basic Data Provider

[Official source](https://www.alfredapp.com/help/alfredui/components/dataview/providers/basic/) · Checked 2026-11-19 · [Index](../../INDEX.md)

`src` is an array of application-defined objects; uid is reserved for identity, filtering and reselection. Display fields may be dotted component-property keys; non-visible fields can support matching or backend data. The provider's filter is configured separately. `modify.insert` inserts before/after a uid; without uid, before means beginning and after means end. Its autoselect selects the first inserted item. `modify.replace.srcmap` maps uid to replacement object; unknown ids are ignored and autoselect targets the first replaced index. `modify.delete.uids` removes matching rows; autoselect selects the same index afterward. Reselection can be overridden by dataview.select. No duplicate-uid policy, uid generation rule, or operation ordering for simultaneous modify branches is specified. Use explicit string uids as an authoring convention, not a universally declared row-uid type requirement.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `src` | Properties | ARRAY | Required | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/providers/basic/#property-src) |
| `filter` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/providers/basic/#property-filter) |
| `filter.type` | Properties | ENUM | Default: "basic" | "basic" | [§](https://www.alfredapp.com/help/alfredui/components/dataview/providers/basic/#property-filter-type) |
| `modify` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/providers/basic/#property-modify) |
| `modify.insert` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/providers/basic/#property-modify-insert) |
| `modify.insert.position` | Properties | ENUM | Default: "after" | "after", "before" | [§](https://www.alfredapp.com/help/alfredui/components/dataview/providers/basic/#property-modify-insert-position) |
| `modify.insert.uid` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/providers/basic/#property-modify-insert-uid) |
| `modify.insert.autoselect` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/providers/basic/#property-modify-insert-autoselect) |
| `modify.insert.src` | Properties | ARRAY | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/providers/basic/#property-modify-insert-src) |
| `modify.replace` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/providers/basic/#property-modify-replace) |
| `modify.replace.autoselect` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/providers/basic/#property-modify-replace-autoselect) |
| `modify.replace.srcmap` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/providers/basic/#property-modify-replace-srcmap) |
| `modify.delete` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/providers/basic/#property-modify-delete) |
| `modify.delete.autoselect` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/providers/basic/#property-modify-delete-autoselect) |
| `modify.delete.uids` | Properties | ARRAY | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/providers/basic/#property-modify-delete-uids) |

## Related local references

- [basic Filter](components--dataview--filters--basic.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
