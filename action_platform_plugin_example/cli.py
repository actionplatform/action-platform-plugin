"""`action-platform example …` — a Typer app the plugin hangs on the CLI."""

from __future__ import annotations

import typer

app = typer.Typer(help="Example plugin commands.", no_args_is_help=True)


@app.command("hello")
def hello(name: str = typer.Argument("world")) -> None:
    """Say hello from the CLI."""
    typer.echo(f"hello {name}")
