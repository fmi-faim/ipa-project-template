#!/usr/bin/env bash
# Initialize pixi and set cache and temporary directories.

export PATH=$PATH:"$(pwd)/infrastructure/apps/pixi/bin"
export PIXI_CACHE_DIR="$(pwd)/infrastructure/apps/pixi/.pixi_cache"
export TMPDIR="$(pwd)/infrastructure/.tmp_$USER"
mkdir -p "$TMPDIR"

# Ensure that the latest documentation is built.
pixi run build_docs

export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export BLIS_NUM_THREADS=1
export VECLIB_MAXIMUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
