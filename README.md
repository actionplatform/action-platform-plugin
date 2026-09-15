# action-platform-plugin

Template for an [Action Platform](https://github.com/actionplatform/action-platform) plugin. Every extension point once, small enough to read in one sitting:

| File | Extension point |
|---|---|
| `plugin.py` | the `Plugin`: slug, `needs`, `register`, `after_release`, `after_deploy` |
| `tools.py` | an MCP tool, published as `example.hello` with input and output schemas |
| `cli.py` | `action-platform example hello` |
| `rules.py` | a replaced core slot (`gitflow_rules`) — stricter branch kinds while the plugin is enabled |
| `release.py` | named providers: `[release] strategy = "calver"`, `[release] changelog = "plain"` |
| `overlays/` | a cloud overlay `example`, applied by `action-platform cloud set example` |

## Use this template

1. Create a repository from it, named `action-platform-plugin-<slug>`.
2. Rename `action_platform_plugin_example` → `action_platform_plugin_<slug>`, `example` → `<slug>` in `pyproject.toml` (package name, entry points), `plugin.py` (`slug`), `cli.py`, `overlays/index.json`.
3. Delete what you do not need; a plugin with only `plugin.py` and one tool is fine.
4. `pip install -e ".[dev]"`, `pytest`, `action-platform plugin list` (shows `example` once installed).
5. Publish to PyPI; open a pull request to [plugins-index](https://github.com/actionplatform/plugins-index) with `<slug>.json`.

## Rules

- `register` only declares; no I/O, threads or connections at import or in `register`.
- No monkey-patching of `action_platform.*` — replace a slot (`surface.core.replace`) or ask for a hook.
- `needs` lists every host you talk to and every environment variable you read.

Reference: [writing a plugin](https://github.com/actionplatform/action-platform/blob/master/docs/contribute_plugins.md) · [plugins](https://github.com/actionplatform/action-platform/blob/master/docs/use_plugins.md).
