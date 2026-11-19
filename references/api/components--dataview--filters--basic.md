# basic Filter

[Official source](https://www.alfredapp.com/help/alfredui/components/dataview/filters/basic/) · Checked 2026-11-19 · [Index](../../INDEX.md)

`args` names one field or multiple fields to match; `match` supplies the query, including a getter placeholder. exactfromstartorwhitespace matches at a word boundary; exactfromstart matches the beginning; wordmatchanyorder permits rearranged query words; wordmatchsequential preserves their order. Empty queries return everything by default or nothing with matchempty=false. A dedicated invisible match field can combine application-specific search terms. The filter uses Alfred's internal word search; case sensitivity, Unicode normalization and fuzzy scoring details are not specified here.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `args` | Properties | STRING\|ARRAY | Required | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/filters/basic/#property-args) |
| `match` | Properties | STRING | Required | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/filters/basic/#property-match) |
| `matchmode` | Properties | ENUM | Default: "exactfromstartorwhitespace" | "exactfromstartorwhitespace", "exactfromstart", "wordmatchanyorder", "wordmatchsequential" | [§](https://www.alfredapp.com/help/alfredui/components/dataview/filters/basic/#property-matchmode) |
| `matchempty` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/filters/basic/#property-matchempty) |

## Related local references

- [Package index](../../INDEX.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
