# finish Action

[Official source](https://www.alfredapp.com/help/alfredui/actions/json/finish/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Finish closes the UI and, in a workflow, forwards args to connected objects and merges supplied variables into the workflow stream. Flattenarrayargs recursively flattens arrays. This page allows getter placeholders directly in args/variables, whereas the JSON Actions overview requires getter capture into variables. Prefer capture in the outer action and var references here, while recording the documentation conflict. External consumers or output channels beyond closing are not specified.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `flattenarrayargs` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/finish/#property-flattenarrayargs) |
| `args` | Properties | STRING \| ARRAY | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/finish/#property-args) |
| `variables` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/json/finish/#property-variables) |

## Related local references

- [Package index](../../INDEX.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
