"""
run_preprocessing.py
====================

This script expects preprocessing_config.yaml to be present in the current
working directory.
"""

import yaml
from ..utils import create_logger

CONFIG_NAME = "preprocessing_config.yaml"


def main(raw_data_dir: str, output_dir: str) -> None:
    """
    Apply preprocessing step to raw data.

    Parameters
    ----------
    raw_data_dir
        Directory containing all raw data.
    output_dir
        Directory where the preprocessed data is saved.

    """
    logger = create_logger(name="preprocessing")

    logger.info(f"Raw data directory: {raw_data_dir}")
    logger.info(f"Output directory: {output_dir}")

    logger.warning("Not implemented!")

    logger.info("Done!")


if __name__ == "__main__":
    with open(CONFIG_NAME, "r") as f:
        config = yaml.safe_load(f)

    main(**config)
