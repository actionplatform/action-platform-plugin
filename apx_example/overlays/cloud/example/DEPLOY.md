# Deploy — example

This project deploys to the example target. The files under `deploy/` came from the `example` plugin's overlay, copied as they are — no templating. Replace them with what your target needs (a `template.yaml`, a `Dockerfile`, a workflow) and ship the matching `DeployTarget` under the `action_platform.deploy_target` entry-point group.
