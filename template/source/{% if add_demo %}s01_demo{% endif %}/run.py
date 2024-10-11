import argparse
from os import scandir
from pathlib import Path

from faim_ipa.utils import get_git_root, create_logger
import sys

from rich.pretty import pretty_repr

sys.path.append(str(get_git_root()))

from source.s01_demo.config import DemoConfig


def main(config: DemoConfig):
    logger = create_logger("demo")
    logger.info(pretty_repr(config))

    for item in scandir(config.raw_data_dir):
        logger.info(f"Found item: {item.name}")

    logger.info("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    args = parser.parse_args()

    config = DemoConfig.load(args.config)
    main(config)
