# Deploy — example

This project deploys to the `example` target. The files under `deploy/` came from the `example` plugin's overlay, copied as they are — no templating.

The contract a real cloud overlay follows: every web project **serves HTTP on `$PORT`**, and the overlay's build step is `ap-build package` (from [images-base](https://github.com/actionplatform/images-base)), which assembles the app, its dependencies and `run.sh` for any language. One `template.yaml` (or Dockerfile, or workflow) per cloud is enough — no files per language. See [apx-aws-lambda](https://github.com/actionplatform/apx-aws-lambda) for the real thing: `template.yaml` with the runtime chosen by language, a `Makefile` with one line, `requirements/` with the least-privilege policy.

The platform calls the target's `readiness(ctx)` after every release, for every scope of the app, and refuses a deploy the checks block. The scope's name arrives as `ctx.stage`.
