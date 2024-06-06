#!/usr/bin/env bash
# Initialize pixi and set cache and temporary directories.

export PATH=$PATH:"$(pwd)/infrastructure/apps/pixi/bin"
export PIXI_CACHE_DIR="$(pwd)/infrastructure/apps/pixi/.pixi_cache"
export TMPDIR="$(pwd)/infrastructure/.tmp_$USER"
mkdir -p "$TMPDIR"

# Ensure that the latest documentation is built.
pixi run build_docs
