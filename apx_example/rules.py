"""A replaced slot: git-flow rules with fewer branch kinds. `surface.core.replace("gitflow_rules", StrictRules)` puts it in; disabling the plugin takes it out."""

from __future__ import annotations

from action_platform.core.flow.gitflow import Rules


class StrictRules(Rules):
    kinds = {"feature", "bugfix", "hotfix", "release"}
    develop_based = {"feature", "bugfix"}
