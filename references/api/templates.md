# Templates

[Official source](https://www.alfredapp.com/help/alfredui/templates/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Store reusable component JSON in the root templates map or a package-relative file. Instantiate it with `type: template`, `src` and a params map. `{param:name}` is substituted when the instance is created. The map is checked before file lookup. Instance-level id and constraints override template values. Avoid hardcoded ids inside reusable templates because identifiers must remain globally unique; passing distinct ids as parameters is an authoring pattern. This override behavior differs from the file pseudo-component's id caveat.

## Complete declared field/function inventory

Paths describe nesting; children under an array apply to each item. `—` means no declaration, not an inferred default or permission. Required/recommended markers apply only where explicitly published. Component properties also include [shared properties](components--shared-properties.md).

| Path | Section | Declared type | Attributes / constraints | Enumerated values | Source |
|---|---|---|---|---|---|
| `src` | Properties | STRING | — | — | [§](https://www.alfredapp.com/help/alfredui/templates/#property-src) |
| `params` | Properties | OBJECT | — | — | [§](https://www.alfredapp.com/help/alfredui/templates/#property-params) |

## Related local references

- [ui.json](ui-json.md)
- [view Component](components--view.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
