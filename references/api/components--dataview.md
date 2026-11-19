# dataview Component

[Official source](https://www.alfredapp.com/help/alfredui/components/dataview/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Each data entry populates a reusable cell. `cell.root` defines that cell's component hierarchy; `cell.init` resets reusable state before new data is applied; `cell.selected` applies selection-specific updates. Data keys can address `componentID.property`. Multiple cols produce row-major cells. Hover selection fires changed and can therefore repeatedly invoke scripts. The allowempty flag permits no selection, reported as null by changed. `select` chooses a uid and overrides modification reselection; invalid/empty uid resets selection. The explanatory references to behaviour.allowemptyselection and modifydata differ from the declared nested selection and provider modify objects. Follow the explicit schemas and test edge behavior. All documented functions are listed below; scrollbottom's prose incorrectly repeats scrolltop, so verify its runtime effect. The page does not formally declare a selected getter schema; official examples access selected.name and the Colour Search tutorial demonstrates selected.swatch.background. Treat that return shape as example-backed, not an exhaustive contract.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `placeholder` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-placeholder) |
| `cols` | Properties | INTEGER | Default: 1 , Range: 1-16 | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-cols) |
| `padding` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-padding) |
| `spacing` | Properties | INTEGER | Default: 0 , Range: 0-64 | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-spacing) |
| `autoadjustcontentinsets` | Properties | BOOL | Default: true | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-autoadjustcontentinsets) |
| `cell` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-cell) |
| `cell.height` | Properties | INTEGER | Default: 64 , Range: 12-1024 | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-cell-height) |
| `cell.root` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-cell-root) |
| `cell.init` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-cell-init) |
| `cell.selected` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-cell-selected) |
| `behaviour` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-behaviour) |
| `behaviour.selection` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-behaviour-selection) |
| `behaviour.selection.wrap` | Properties | ENUM | Default: "none" | "none", "vertical" | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-behaviour-selection-wrap) |
| `behaviour.selection.allowempty` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-behaviour-selection-allowempty) |
| `behaviour.selection.hover` | Properties | BOOL | Default: false | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-behaviour-selection-hover) |
| `data` | Properties | OBJECT | Required | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-data) |
| `data.type` | Properties | ENUM | Default: "basic" | "basic" | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-data-type) |
| `select` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-select) |
| `filterdata` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-filterdata) |
| `scrolltop` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-scrolltop) |
| `scrollbottom` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-scrollbottom) |
| `selectfirst` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-selectfirst) |
| `selectlast` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-selectlast) |
| `selectprevious` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-selectprevious) |
| `selectnext` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-selectnext) |
| `selectup` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-selectup) |
| `selectdown` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-selectdown) |
| `selectleft` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-selectleft) |
| `selectright` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-selectright) |
| `selectnone` | Functions | function | — | — | [§](https://www.alfredapp.com/help/alfredui/components/dataview/#property-selectnone) |

## Related local references

- [view Component](components--view.md)
- [basic Data Provider](components--dataview--providers--basic.md)
- [Shared Properties](components--shared-properties.md)
- [functions Action](actions--json--functions.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
