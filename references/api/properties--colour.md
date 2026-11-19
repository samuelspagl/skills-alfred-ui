# COLOUR Property Type

[Official source](https://www.alfredapp.com/help/alfredui/properties/colour/) · Checked 2026-11-19 · [Index](../../INDEX.md)

COLOUR is represented by strings: `#RRGGBB` or `#RRGGBBAA`; `rgb(r,g,b)` with channels 0–255, optionally a fourth alpha 0–1; `hsv(h,s,v)` with hue 0–359 and saturation/brightness 0–100, optionally alpha 0–1. Use `rgb`, not an assumed `rgba` alias. Named values include macOS Apple/Developer/Crayons colours, adaptable system colours, application-defined colour constants, and Alfred's selected-result theme constants. Define custom names in the root `colours` map. The documentation does not enumerate every platform colour name or define whitespace/case normalization. Examples of authored values: `#235789`, `#23578980`, `rgb(35,87,137,0.5)`, `hsv(210,75,60)`, `systemBlueColor`.

## Related local references

- [ui.json](ui-json.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
