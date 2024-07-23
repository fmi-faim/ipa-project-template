import json
import shutil
import subprocess

info = subprocess.run(["pixi", "info", "--json"], stdout=subprocess.PIPE)
cache_dir = json.loads(info.stdout)["cache_dir"]

GB = 1024 * 1024 * 1024
if shutil.disk_usage(cache_dir).free < 2 * GB:
    message = f"""
    Low disk space in cache directory.

    The PIXI_CACHE_DIR is set to:
    {cache_dir}

    Did you initialize your session correctly ('source ./init.sh') ?"""
    raise RuntimeError(message)
