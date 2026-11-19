# textarea Component

[Official source](https://www.alfredapp.com/help/alfredui/components/textarea/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Editable/selectable defaults are not specified. Text is a getter. User edits trigger changed; typing pauses trigger typingstopped. Programmatic text mode is replace, append, prepend or replacelast (replace the last supplied segment). Scroll mode is independent: none, auto, start or end. Functions move the caret to either end or scroll to top/bottom. Insets surround text; automatic content insets account for overlapping window chrome. `disableallsubstitutions` suppresses system text substitutions such as smart punctuation and spelling behavior; its header quotes false despite declaring BOOL. Supply a boolean. The first source example has a trailing comma; generated JSON here is strict. Specify constraints.size for a useful desired size.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `background` | Properties | COLOUR \| null | null → clear background | — | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-background) |
| `font` | Properties | FONT \| null | null → default font | — | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-font) |
| `colour` | Properties | COLOUR \| null | null → default text colour | — | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-colour) |
| `bordertype` | Properties | ENUM | Default: "none" | "bezel", "solid", "none" | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-bordertype) |
| `editable` | Properties | BOOL | — | — | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-editable) |
| `selectable` | Properties | BOOL | — | — | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-selectable) |
| `behaviour` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-behaviour) |
| `behaviour.mode` | Properties | ENUM | Default: "replace" | "replace", "append", "prepend", "replacelast" | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-behaviour-mode) |
| `behaviour.scroll` | Properties | ENUM | Default: "none" | "none", "auto", "start", "end" | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-behaviour-scroll) |
| `autoadjustcontentinsets` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-autoadjustcontentinsets) |
| `text` | Properties | STRING [ getter ] | — | — | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-text) |
| `textinsets` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-textinsets) |
| `textinsets.horizontal` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-textinsets-horizontal) |
| `textinsets.vertical` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-textinsets-vertical) |
| `disableallsubstitutions` | Properties | BOOL | Default: "false" | — | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-disableallsubstitutions) |
| `scrolltop` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-scrolltop) |
| `scrollbottom` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-scrollbottom) |
| `caretstart` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-caretstart) |
| `caretend` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/textarea/#property-caretend) |

## Component-specific triggers

`changed`, `typingstopped`. Semantics are described above.

## Related local references

- [Constraints](layouts--constraints.md)
- [COLOUR Property Type](properties--colour.md)
- [FONT Property Type](properties--font.md)
- [Getters](properties--getters.md)
- [Shared Properties](components--shared-properties.md)
- [Events](events.md)
- [functions Action](actions--json--functions.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
