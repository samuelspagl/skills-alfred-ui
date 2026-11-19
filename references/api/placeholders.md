# Placeholders

[Official source](https://www.alfredapp.com/help/alfredui/placeholders/) · Checked 2026-11-19 · [Index](../../INDEX.md)

Preprocessing replaces `{var:name}` without recursively processing its result, `{const:name}` with workflow constants, `{file:path}` with recursively processed file contents, and `{fileraw:path}` with unprocessed contents. The ignored keys are bundleid, variablesconfig, variables, args, action.src and data.filter. Args, variables and action.src are processed at use time. Action args/variables additionally support `{value:id.property}` and `{data:property}`; the latter addresses a dataview cell's data. A placeholder occupying the whole JSON string retains its underlying JSON type. Mixing it with literal text always yields a string; non-string values are JSON-encoded. Template `{param:name}` substitution happens immediately when instantiated. Pulse has stricter argument rules. Do not assume arbitrary properties are continuously bound to variable changes.

## Related local references

- [Properties](properties.md)
- [ui.json](ui-json.md)
- [Actions](actions.md)
- [Variables](variables.md)
- [dataview Component](components--dataview.md)
- [Data Filters](components--dataview--filters.md)
- [Alfred UI Components](components.md)
- [Getters](properties--getters.md)

See [uncertainties](../uncertainties.md) before relying on conflicting examples.
