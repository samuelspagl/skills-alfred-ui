# markdownarea Component

[Official source](https://www.alfredapp.com/help/alfredui/components/markdownarea/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Text or a file src supplies Markdown to parse. Programmatic text modes and scrolling modes mirror the declared textarea modes. Spacing controls affect lines, paragraphs and list items. `urischemes` replaces the default http/https scheme list and affects only subsequently parsed Markdown; explicitly retain those schemes if needed. The page's introductory description calls this an input box, but publishes neither editable nor a text getter nor editing triggers. Do not assume textarea's full API is inherited. A precise Markdown dialect or HTML support matrix is not specified. Use a desired size constraint for predictable initial layout.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `background` | Properties | COLOUR \| null | null → clear background | — | [§](https://www.alfredapp.com/help/alfredui/components/markdownarea/#property-background) |
| `font` | Properties | FONT \| null | null → default font | — | [§](https://www.alfredapp.com/help/alfredui/components/markdownarea/#property-font) |
| `colour` | Properties | COLOUR \| null | null → default text colour | — | [§](https://www.alfredapp.com/help/alfredui/components/markdownarea/#property-colour) |
| `linespacing` | Properties | DOUBLE | — | — | [§](https://www.alfredapp.com/help/alfredui/components/markdownarea/#property-linespacing) |
| `lineheightmultiple` | Properties | DOUBLE | — | — | [§](https://www.alfredapp.com/help/alfredui/components/markdownarea/#property-lineheightmultiple) |
| `paragraphspacing` | Properties | DOUBLE | — | — | [§](https://www.alfredapp.com/help/alfredui/components/markdownarea/#property-paragraphspacing) |
| `listspacing` | Properties | DOUBLE | — | — | [§](https://www.alfredapp.com/help/alfredui/components/markdownarea/#property-listspacing) |
| `autoadjustcontentinsets` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/components/markdownarea/#property-autoadjustcontentinsets) |
| `urischemes` | Properties | ARRAY | Default: "http", "https" | — | [§](https://www.alfredapp.com/help/alfredui/components/markdownarea/#property-urischemes) |
| `behaviour` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/markdownarea/#property-behaviour) |
| `behaviour.mode` | Properties | ENUM | Default: "replace" | "replace", "append", "prepend", "replacelast" | [§](https://www.alfredapp.com/help/alfredui/components/markdownarea/#property-behaviour-mode) |
| `behaviour.scroll` | Properties | ENUM | Default: "none" | "none", "auto", "start", "end" | [§](https://www.alfredapp.com/help/alfredui/components/markdownarea/#property-behaviour-scroll) |
| `text` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/components/markdownarea/#property-text) |
| `src` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/components/markdownarea/#property-src) |

## Related local references

- [Constraints](layouts--constraints.md)
- [COLOUR Property Type](properties--colour.md)
- [FONT Property Type](properties--font.md)
- [Shared Properties](components--shared-properties.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
