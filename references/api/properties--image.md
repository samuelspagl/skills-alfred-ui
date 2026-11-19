# IMAGE Property Type

[Official source](https://www.alfredapp.com/help/alfredui/properties/image/) · Checked 2026-11-19 · [Index](../../INDEX.md)

`type` determines how `src` is interpreted: image file, a file's icon, a file-type icon using a path, or an SF Symbol name. Paths may be absolute or package-relative. `size` is a preferred size; zero means automatic. Supplying just width or height allows the other dimension to be derived. The docs do not prescribe a pixel range, list supported codecs, or guarantee that every symbol exists on every macOS version. Example: `{"type":"symbol","src":"star","size":{"width":24}}`.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `size` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/properties/image/#property-size) |
| `size.width` | Properties | INTEGER | Default: 0 | — | [§](https://www.alfredapp.com/help/alfredui/properties/image/#property-size-width) |
| `size.height` | Properties | INTEGER | Default: 0 | — | [§](https://www.alfredapp.com/help/alfredui/properties/image/#property-size-height) |
| `type` | Properties | "file" \| "fileicon" \| "filetypeicon" \| "symbol" | Default: "file" | "file", "fileicon", "filetypeicon", "symbol" | [§](https://www.alfredapp.com/help/alfredui/properties/image/#property-type) |
| `src` | Properties | STRING | Required | — | [§](https://www.alfredapp.com/help/alfredui/properties/image/#property-src) |

## Related local references

- [Package index](../../INDEX.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
