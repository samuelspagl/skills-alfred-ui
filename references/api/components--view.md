# view Component

[Official source](https://www.alfredapp.com/help/alfredui/components/view/) · Checked 2026-11-19 · [Index](../../INDEX.md)

`components` holds child components; `layout` chooses the arrangement. Padding is interior spacing around the children; spacing separates them where the selected layout uses it. Border width/colour draw an inset overlay. Null removes background or border colour. `cliptobounds` clips overflowing content and may cost rendering time in complex hierarchies. `focusable` allows the container to accept focus. `vetomovablebybackground` prevents window dragging through this view. Layout-specific properties such as direction, rows and cols belong directly on the view. Appearance inherits by default; the prose mentioning automatic is inconsistent with the declared inherit enum. Shortcut scope follows focus ancestry, but precedence is ambiguously described.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `layout` | Properties | ENUM | Default: "stack" | "stack", "border", "grid", "inline", "form", "flex" | [§](https://www.alfredapp.com/help/alfredui/components/view/#property-layout) |
| `components` | Properties | ARRAY | Of type: component | — | [§](https://www.alfredapp.com/help/alfredui/components/view/#property-components) |
| `padding` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/components/view/#property-padding) |
| `spacing` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/components/view/#property-spacing) |
| `cliptobounds` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/components/view/#property-cliptobounds) |
| `cornerradius` | Properties | INTEGER | Default: 0 , Range: 0-32 | — | [§](https://www.alfredapp.com/help/alfredui/components/view/#property-cornerradius) |
| `appearance` | Properties | ENUM | Default: "inherit" | "inherit", "light", "dark" | [§](https://www.alfredapp.com/help/alfredui/components/view/#property-appearance) |
| `background` | Properties | COLOUR \| null | null → clear background | — | [§](https://www.alfredapp.com/help/alfredui/components/view/#property-background) |
| `border` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/view/#property-border) |
| `border.width` | Properties | INTEGER | Default: 0 , Range: 0-32 | — | [§](https://www.alfredapp.com/help/alfredui/components/view/#property-border-width) |
| `border.colour` | Properties | COLOUR \| null | null → clear border | — | [§](https://www.alfredapp.com/help/alfredui/components/view/#property-border-colour) |
| `focusable` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/components/view/#property-focusable) |
| `shortcuts` | Properties | ARRAY | Of type: SHORTCUT | — | [§](https://www.alfredapp.com/help/alfredui/components/view/#property-shortcuts) |
| `vetomovablebybackground` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/components/view/#property-vetomovablebybackground) |

## Related local references

- [Alfred UI Components](components.md)
- [Layouts](layouts.md)
- [stack Layout](layouts--stack.md)
- [border Layout](layouts--border.md)
- [grid Layout](layouts--grid.md)
- [inline Layout](layouts--inline.md)
- [form Layout](layouts--form.md)
- [flex Layout](layouts--flex.md)
- [COLOUR Property Type](properties--colour.md)
- [SHORTCUT Property Type](properties--shortcut.md)
- [Shared Properties](components--shared-properties.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
