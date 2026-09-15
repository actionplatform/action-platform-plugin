"""The plugin: what it declares on the MCP server, the CLI and the core's wiring, and what it does after a release or a deploy."""

from __future__ import annotations

from pathlib import Path

from action_platform.abc import Plugin, Surface
from action_platform.core.context import Context, DeployResult
from action_platform.logging import logger

from action_platform_plugin_example import cli
from action_platform_plugin_example.rules import StrictRules
from action_platform_plugin_example.tools import register_tools


class ExamplePlugin(Plugin):
    slug = "example"
    description = "Template plugin: a tool, a command, an overlay, a release strategy, stricter git-flow"
    min_core = "0.16"
    needs = ["nothing outside this machine"]

    @property
    def overlays(self) -> Path:
        return Path(__file__).parent / "overlays"

    def register(self, surface: Surface) -> None:
        if surface.mcp is not None:
            register_tools(surface.mcp)

        if surface.cli is not None:
            surface.cli.add_typer(cli.app, name="example")

        surface.core.replace("gitflow_rules", StrictRules)

    def after_release(self, ctx: Context) -> None:
        logger.info(f"example: released {ctx.next_version} from {ctx.branch}")

    def after_deploy(self, results: list[DeployResult]) -> None:
        for result in results:
            logger.info(f"example: {result.target} {'ok' if result.ok else 'failed'}")
