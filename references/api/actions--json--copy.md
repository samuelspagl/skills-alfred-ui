# copy Action

[Official source](https://www.alfredapp.com/help/alfredui/actions/json/copy/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Copy plain text, file references or URLs using type and src. Type defaults text. Src accepts a string or array; multiple file paths are explicitly documented. Copying a file reference is different from reading that file's contents.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `type` | Properties | ENUM | Default: "text" | "text", "file", "url" | [§](https://www.alfredapp.com/help/alfredui/actions/json/copy/#property-type) |
| `src` | Properties | STRING \| ARRAY | Required | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/copy/#property-src) |

## Related local references

- [Package index](../../INDEX.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
