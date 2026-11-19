# Getters

[Official source](https://www.alfredapp.com/help/alfredui/properties/getters/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Read annotated getter properties in action args or variables using `{value:componentID.property}`. `{value:self.property}` addresses the component owning the action without requiring an id. Nested selection access is documented for picker, for example `{value:format.selected.value}`. Do not infer that every configurable property has a getter. Before JSON commands, capture component values into action variables; then use `{var:name}` within commands.

## Related local references

- [Actions](actions.md)
- [Shared Properties](components--shared-properties.md)
- [Properties](properties.md)
- [picker Component](components--picker.md)
- [checkbox Component](components--checkbox.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
