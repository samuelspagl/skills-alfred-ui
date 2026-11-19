# Actions

[Official source](https://www.alfredapp.com/help/alfredui/actions/) · Checked 2026-11-19 · [Index](../../INDEX.md)

An action has type log, script, json or function. Src is respectively ignored, a script path, JSON-command object/file path, or target component id. Args respectively supplies info-level log text, script arguments, ignored input, or function names. Headers mark src required even though log ignores it. Args and variables resolve at trigger time before execution. Unresolved argument placeholders become empty strings; dictionaries become JSON and arrays do too unless recursive flattenarrayargs is enabled. Async defaults false; when enabled, UI state may change before the script response arrives. Script output is parsed as JSON Actions. No timeout, cancellation, retry or stale-result suppression contract is published here.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `type` | action Object | ENUM | Required | "log", "script", "json", "function" | [§](https://www.alfredapp.com/help/alfredui/actions/#property-type) |
| `src` | action Object | STRING \| OBJECT | Required | — | [§](https://www.alfredapp.com/help/alfredui/actions/#property-src) |
| `args` | action Object | STRING \| ARRAY | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/#property-args) |
| `variables` | action Object | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/actions/#property-variables) |
| `flattenarrayargs` | action Object | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/actions/#property-flattenarrayargs) |
| `async` | action Object | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/actions/#property-async) |

## Related local references

- [Events](events.md)
- [button Component](components--button.md)
- [Placeholders](placeholders.md)
- [JSON Actions](actions--json.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
