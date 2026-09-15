"""MCP tools. They come out as `example_<name>`; annotate inputs and return a model or a typed dict so the client gets schemas."""

from __future__ import annotations

from typing import Annotated, Any

from pydantic import BaseModel, Field

from action_platform.mcp.annotations import READ_ONLY


class Greeting(BaseModel):
    greeting: str


def register_tools(mcp: Any) -> None:
    @mcp.tool(annotations=READ_ONLY)
    def hello(
        name: Annotated[str, Field(description="Who to greet")] = "world",
    ) -> Greeting:
        """Say hello — the smallest tool a plugin can add."""
        return Greeting(greeting=f"hello {name}")
