# sheet Action

[Official source](https://www.alfredapp.com/help/alfredui/actions/json/sheet/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Root defines the sheet's UI. Id lets another action address it using close. Escape closes by default; if closeonescape=false, id is required so the sheet can be dismissed programmatically. A close command only needs the id under close, not a new root. Do not make root universally required across both show and close forms.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `id` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/sheet/#property-id) |
| `close` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/sheet/#property-close) |
| `closeonescape` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/sheet/#property-closeonescape) |
| `root` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/sheet/#property-root) |

## Related local references

- [Package index](../../INDEX.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
