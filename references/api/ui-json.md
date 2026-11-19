# ui.json

[Official source](https://www.alfredapp.com/help/alfredui/ui-json/) · Checked 2026-11-19 · [Index](../../INDEX.md)

The entry file contains configuration maps and the initial `window` object. `window` is demonstrated on the Window page although absent from this page's property list. `variablesconfig` maps variable names to configuration objects; `variables` maps names to initial values. `templates` maps names to component objects and takes precedence over file lookup. `colours` maps names to COLOUR values. A `bundleid` is needed for persistence. `iconpath` affects the dock icon for external execution. The two Alfred theme constants are `alfredSelectedResultTextColor` and `alfredSelectedResultBackgroundColor`. Their spelling uses `Color`, despite the `colours` configuration key. Script-environment defaults conflict with the Variables page; configure them explicitly.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `bundleid` | Properties | STRING | Recommended | — | [§](https://www.alfredapp.com/help/alfredui/ui-json/#property-bundleid) |
| `variablesconfig` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/ui-json/#property-variablesconfig) |
| `variables` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/ui-json/#property-variables) |
| `iconpath` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/ui-json/#property-iconpath) |
| `log` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/ui-json/#property-log) |
| `debug` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/ui-json/#property-debug) |
| `templates` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/ui-json/#property-templates) |
| `colours` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/ui-json/#property-colours) |
| `pulse` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/ui-json/#property-pulse) |

## Related local references

- [Variables](variables.md)
- [Log](log.md)
- [Debug](debug.md)
- [Templates](templates.md)
- [COLOUR Property Type](properties--colour.md)
- [Pulse](pulse.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
