#!/bin/bash
set -euo pipefail

USERNAME=murphycw
APPNAME=digital-htc-architecture
TAG=$1

export DOCKER_BUILDKIT=1

# Use cache from remote repo keep cache metadata, push new build up to remote repo
docker buildx build --platform linux/amd64,linux/arm64 \
      --tag "$USERNAME/$APPNAME:$TAG" \
      --tag "$USERNAME/$APPNAME" \
      --cache-from "$USERNAME/$APPNAME:$TAG" \
      --build-arg BUILDKIT_INLINE_CACHE=1 \
      --push .
