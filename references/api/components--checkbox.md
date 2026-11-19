# checkbox Component

[Official source](https://www.alfredapp.com/help/alfredui/components/checkbox/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Use `text` for the caption and `checked` for boolean state; both are getters. A user state change dispatches changed. Read `{value:self.checked}` in the action owning the checkbox, or address it by id from another action.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `text` | Properties | STRING [ getter ] | Recommended | — | [§](https://www.alfredapp.com/help/alfredui/components/checkbox/#property-text) |
| `checked` | Properties | BOOL [ getter ] | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/components/checkbox/#property-checked) |

## Component-specific triggers

`changed`. Semantics are described above.

## Related local references

- [Getters](properties--getters.md)
- [Shared Properties](components--shared-properties.md)
- [Events](events.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
