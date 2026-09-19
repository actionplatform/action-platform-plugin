"""The deploy target: what the platform calls to ship a release to the `example` cloud. Replace the bodies with your cloud's CLI; keep the shape."""

from __future__ import annotations

from action_platform.abc import DeployTarget
from action_platform.core.context import Check, Context, DeployResult, Diagnosis
from action_platform.core.process import stream
from action_platform.logging import logger


class ExampleTarget(DeployTarget):
    name = "example"

    def preflight(self, ctx: Context) -> None:
        if not (ctx.repo_root / "deploy" / "run.sh").exists():
            raise FileNotFoundError(
                "deploy/run.sh not found: apply the example overlay first"
            )

    def readiness(self, ctx: Context) -> list[Check]:
        present = (ctx.repo_root / "deploy" / "run.sh").exists()

        return [
            Check(
                "example.overlay",
                present,
                "deploy/run.sh is there" if present else "deploy/run.sh not found",
                fix=None if present else "action-platform cloud set example",
            )
        ]

    def deploy(self, ctx: Context) -> DeployResult:
        result = stream(
            ["sh", "deploy/run.sh"],
            cwd=ctx.repo_root,
            env={**ctx.env, "SCOPE": ctx.stage},
        )
        logger.info("example: deployed %s to %s", ctx.next_version, ctx.stage)

        return DeployResult(
            ok=result.ok,
            target=self.name,
            version=ctx.next_version,
            error=None if result.ok else result.output,
        )

    def verify(self, version: str, stage: str | None = None) -> bool:
        return True

    def diagnose(self, ctx: Context) -> Diagnosis:
        return Diagnosis(
            ok=True, target=self.name, status="example", details={"scope": ctx.stage}
        )

    def delete(self, ctx: Context) -> None:
        logger.info("example: nothing to tear down for %s", ctx.stage)
