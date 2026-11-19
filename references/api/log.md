# Log

[Official source](https://www.alfredapp.com/help/alfredui/log/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Logging can target a file, the macOS console, and the Alfred workflow debugger. Relative log paths use AlfredUI's shared logs folder, not the general package-root rule. Levels accumulate from error through warning, info, debug, verbose to all; none disables logging. Timestamp prefixes records. Colourful adds ANSI styling only to written files. Internal logging works only while running inside Alfred. Use log actions to emit args at info level.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `path` | Properties | STRING | Optional | — | [§](https://www.alfredapp.com/help/alfredui/log/#property-path) |
| `level` | Properties | ENUM | Default: "none" | "none", "error", "warning", "info", "debug", "verbose", "all" | [§](https://www.alfredapp.com/help/alfredui/log/#property-level) |
| `timestamp` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/log/#property-timestamp) |
| `colourful` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/log/#property-colourful) |
| `console` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/log/#property-console) |
| `internal` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/log/#property-internal) |

## Related local references

- [Package index](../../INDEX.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
