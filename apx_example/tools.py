"""MCP tools. They come out as `example_<name>`; annotate inputs and return a model so the client gets schemas. `options` is the plugin's own store — a file on a machine, a table on the hosted platform."""

from __future__ import annotations

from typing import Annotated, Any

from pydantic import BaseModel, Field

from action_platform.mcp.annotations import READ_ONLY, WRITES_LOCAL
from action_platform.plugins import Options


class Greeting(BaseModel):
    greeting: str


class Remembered(BaseModel):
    key: str
    value: Any


def register_tools(mcp: Any, options: Options) -> None:
    @mcp.tool(annotations=READ_ONLY)
    def hello(
        name: Annotated[str, Field(description="Who to greet")] = "world",
    ) -> Greeting:
        """Say hello — the smallest tool a plugin can add. The word comes from the plugin's options when set."""
        return Greeting(greeting=f"{options.get('greeting', 'hello')} {name}")

    @mcp.tool(annotations=WRITES_LOCAL)
    def remember(key: str, value: str) -> Remembered:
        """Store a value in the plugin's options — the platform keeps it for the next call."""
        options.set(key, value)

        return Remembered(key=key, value=value)
