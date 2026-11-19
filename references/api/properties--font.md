# FONT Property Type

[Official source](https://www.alfredapp.com/help/alfredui/properties/font/) · Checked 2026-11-19 · [Index](../../INDEX.md)

`size` accepts named sizes and a numeric pixel size, despite being labelled ENUM. The numeric range is not specified. `monospaced` is a boolean or the string `digits`; the latter changes numeric glyph spacing without selecting a fully monospaced font. `width` only affects non-monospaced fonts. Weight and width names correspond to AppKit font weights and widths. Example: `{"size":18,"weight":"semibold","monospaced":"digits"}`.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `size` | Properties | ENUM | Default: "default" | size-px, "default", "hairline", "extrasmall", "small", "medium", "large", "extralarge", "ginormous" | [§](https://www.alfredapp.com/help/alfredui/properties/font/#property-size) |
| `monospaced` | Properties | BOOL \| "digits" | Default: false | true, false, "digits" | [§](https://www.alfredapp.com/help/alfredui/properties/font/#property-monospaced) |
| `weight` | Properties | ENUM | Default: "regular" | "ultralight", "thin", "light", "regular", "medium", "semibold", "bold", "heavy", "black" | [§](https://www.alfredapp.com/help/alfredui/properties/font/#property-weight) |
| `width` | Properties | ENUM | Default: "standard" | "compressed", "condensed", "standard", "expanded" | [§](https://www.alfredapp.com/help/alfredui/properties/font/#property-width) |

## Related local references

- [Alfred UI Components](components.md)
- [label Component](components--label.md)
- [textfield Component](components--textfield.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
