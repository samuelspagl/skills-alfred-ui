# Shared Properties

[Official source](https://www.alfredapp.com/help/alfredui/components/shared-properties/) · Checked 2026-11-19 · [Index](../../INDEX.md)

The default component type is view. Keep ids globally unique; they are used for getters, mutations and function targets. Initial focus should be assigned to only one component. Hidden components still occupy layout space. Disabled components reject input; opacity changes rendering. Context menus contain MENU items. `shortcut` is a native key equivalent for supported controls, including button, checkbox and picker; view `shortcuts` is separate. Accessibility label should be a short capitalized name without a final full stop; help provides explanatory text with sentence punctuation. A file pseudo-component's id can be overridden by the referenced file. `events` is labelled ARRAY | EVENT here, while Events primarily describes arrays; use arrays for portable authoring.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `type` | Properties | ENUM | Default: "view" | — | [§](https://www.alfredapp.com/help/alfredui/components/shared-properties/#property-type) |
| `id` | Properties | STRING | Unique | — | [§](https://www.alfredapp.com/help/alfredui/components/shared-properties/#property-id) |
| `constraints` | Properties | OBJECT | View properties | — | [§](https://www.alfredapp.com/help/alfredui/components/shared-properties/#property-constraints) |
| `events` | Properties | ARRAY \| EVENT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/shared-properties/#property-events) |
| `focus` | Properties | BOOL | one component only | — | [§](https://www.alfredapp.com/help/alfredui/components/shared-properties/#property-focus) |
| `hidden` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/components/shared-properties/#property-hidden) |
| `opacity` | Properties | DOUBLE | Default: 1.0 , Range: 0.0-1.0 | — | [§](https://www.alfredapp.com/help/alfredui/components/shared-properties/#property-opacity) |
| `enabled` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/components/shared-properties/#property-enabled) |
| `tooltip` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/components/shared-properties/#property-tooltip) |
| `menu` | Properties | ARRAY | Of type: MENU | — | [§](https://www.alfredapp.com/help/alfredui/components/shared-properties/#property-menu) |
| `shortcut` | Properties | STRING | supported actionable controls only | — | [§](https://www.alfredapp.com/help/alfredui/components/shared-properties/#property-shortcut) |
| `accessibility` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/shared-properties/#property-accessibility) |
| `accessibility.label` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/components/shared-properties/#property-accessibility-label) |
| `accessibility.help` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/components/shared-properties/#property-accessibility-help) |

## Related local references

- [Alfred UI Components](components.md)
- [Actions](actions.md)
- [Properties](properties.md)
- [Constraints](layouts--constraints.md)
- [Layouts](layouts.md)
- [Events](events.md)
- [MENU Property Type](properties--menu.md)
- [popupmenu Action](actions--json--popupmenu.md)
- [button Component](components--button.md)
- [checkbox Component](components--checkbox.md)
- [picker Component](components--picker.md)
- [view Component](components--view.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
