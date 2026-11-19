# Variables

[Official source](https://www.alfredapp.com/help/alfredui/variables/) · Checked 2026-11-19 · [Index](../../INDEX.md)

`variablesconfig` is a map keyed by variable name, with the per-variable schema below. `src` selects an incoming argument (`args[x]`), the incoming argument array (`args`), or a same-named workflow variable (`variable`). Workflow variables are not imported automatically. The Web Browser tutorial identifies args[0] as the first argument; see its linked reference. `variables` sets initial values, whereas `default` is the fallback when the value is null and the baseline for persistence. Values different from that baseline are persisted and restored; a bundleid is required. Actions and JSON-action responses can change variables. The declared `default` type is STRING, but its documented default is null; support for other configuration-default types is not specified. General variable values can hold structured JSON, as shown on the Placeholders page. Set `scriptenv` explicitly because its false default here conflicts with root-level prose.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `default` | Variables Configuration | STRING | Default: null | — | [§](https://www.alfredapp.com/help/alfredui/variables/#property-default) |
| `persist` | Variables Configuration | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/variables/#property-persist) |
| `scriptenv` | Variables Configuration | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/variables/#property-scriptenv) |
| `src` | Variables Configuration | SPECIAL | Optional | args[x], args, variable | [§](https://www.alfredapp.com/help/alfredui/variables/#property-src) |

## Related local references

- [Placeholders](placeholders.md)
- [ui.json](ui-json.md)
- [Actions](actions.md)
- [JSON Actions](actions--json.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
