"""Named providers platform.toml picks: `[release] strategy = "calver"`, `[release] changelog = "plain"`."""

from __future__ import annotations

from datetime import date

from action_platform.abc import ChangelogRenderer, ReleaseStrategy


class Calver(ReleaseStrategy):
    """YYYY.MM.N — N counts releases in the month; a pre-release adds -rc.N."""

    name = "calver"

    def next(self, current: str, level: str, prerelease: bool, taken: list[str]) -> str:
        today = date.today()
        prefix = f"{today.year}.{today.month:02d}."
        used = [
            int(tag.removeprefix("v")[len(prefix) :].split("-")[0])
            for tag in taken
            if tag.removeprefix("v").startswith(prefix)
            and tag.removeprefix("v")[len(prefix) :].split("-")[0].isdigit()
        ]
        stable = f"{prefix}{max(used, default=0) + 1}"

        if not prerelease:
            return stable

        rcs = [
            int(tag.rsplit("-rc.", 1)[1])
            for tag in taken
            if tag.removeprefix("v").startswith(stable + "-rc.")
        ]

        return f"{stable}-rc.{max(rcs, default=0) + 1}"


class Plain(ChangelogRenderer):
    """One line per commit, no sections."""

    name = "plain"

    def render(self, version: str, commits: list[str]) -> str:
        lines = [f"## {version} — {date.today().isoformat()}", ""]
        lines.extend(f"- {c}" for c in commits)

        return "\n".join(lines).rstrip() + "\n"
