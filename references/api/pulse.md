# Pulse

[Official source](https://www.alfredapp.com/help/alfredui/pulse/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Pulse runs a script repeatedly and handles its JSON-command output at the end of the event thread. Args may contain strings or variable placeholders, resolved each tick, but not UI-value getters or composed variable strings. Interval zero disables it; otherwise the documented range is 0.1–1000 seconds. Delay mode waits after completion; regular mode attempts a fixed cadence. Now requests one immediate pulse without shifting the configured schedule. Returned JSON can change pulse configuration, including disabling it. The docs do not give a hard real-time guarantee, overlapping-run policy, or shutdown/cancellation semantics.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `src` | Properties | STRING | Required | — | [§](https://www.alfredapp.com/help/alfredui/pulse/#property-src) |
| `args` | Properties | STRING \| ARRAY | — | — | [§](https://www.alfredapp.com/help/alfredui/pulse/#property-args) |
| `now` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/pulse/#property-now) |
| `intervalmode` | Properties | ENUM | Default: "delay" | "delay", "regular" | [§](https://www.alfredapp.com/help/alfredui/pulse/#property-intervalmode) |
| `interval` | Properties | DOUBLE | Default: 0 , Range: 0.1-1000 | — | [§](https://www.alfredapp.com/help/alfredui/pulse/#property-interval) |

## Related local references

- [ui.json](ui-json.md)
- [JSON Actions](actions--json.md)
- [Variables](variables.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
