# Properties

[Official source](https://www.alfredapp.com/help/alfredui/properties/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Primitive types are STRING, BOOL, INTEGER, DOUBLE, ARRAY and ENUM. OBJECT appears throughout the API. Ranged numbers are clamped by AlfredUI, rather than necessarily rejected. A property accepting null may reset to its default or apply a property-specific removal rule. Null is not automatically legal everywhere. Getter annotations identify values accessible through action placeholders; a setter's type need not match its getter's return shape. The custom formats are COLOUR, FONT, IMAGE, SHORTCUT and MENU.

## Related local references

- [Getters](properties--getters.md)
- [Actions](actions.md)
- [COLOUR Property Type](properties--colour.md)
- [FONT Property Type](properties--font.md)
- [IMAGE Property Type](properties--image.md)
- [SHORTCUT Property Type](properties--shortcut.md)
- [MENU Property Type](properties--menu.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
