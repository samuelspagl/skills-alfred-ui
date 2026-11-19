# webkitview Component

[Official source](https://www.alfredapp.com/help/alfredui/components/webkitview/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Supply HTML in text, or a URL/file path in src. Only src is annotated as a getter. `openlinksexternally` is false for internal navigation, true for external handling, or a regular-expression value for selective external handling. Regex engine and flags are not specified. The changed trigger reports URL changes, including programmatic assignment and navigation. Functions are back, forward and reload. No JavaScript-to-AlfredUI bridge, script execution action, navigation policy beyond this flag, or HTML/text precedence is documented here.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `openlinksexternally` | Properties | BOOL \| REGEX | Default: false (i.e. all links open internally) | — | [§](https://www.alfredapp.com/help/alfredui/components/webkitview/#property-openlinksexternally) |
| `text` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/components/webkitview/#property-text) |
| `src` | Properties | STRING [ getter ] | — | — | [§](https://www.alfredapp.com/help/alfredui/components/webkitview/#property-src) |
| `back` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/webkitview/#property-back) |
| `forward` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/webkitview/#property-forward) |
| `reload` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/webkitview/#property-reload) |

## Component-specific triggers

`changed`. Semantics are described above.

## Related local references

- [Constraints](layouts--constraints.md)
- [Getters](properties--getters.md)
- [Shared Properties](components--shared-properties.md)
- [functions Action](actions--json--functions.md)
- [Events](events.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
