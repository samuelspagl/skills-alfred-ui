# share Action

[Official source](https://www.alfredapp.com/help/alfredui/actions/json/share/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Type is required and selects file or url. Src is one value or an array passed to the macOS sharing interface. Sharing destinations and completion callbacks are not documented.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `type` | Properties | ENUM | Required | "file", "url" | [§](https://www.alfredapp.com/help/alfredui/actions/json/share/#property-type) |
| `src` | Properties | STRING \| ARRAY | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/share/#property-src) |

## Related local references

- [Package index](../../INDEX.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
