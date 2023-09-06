"""
run_preprocessing.py
====================

This script expects preprocessing_config.yaml to be present in the current
working directory.
"""

import yaml
from datetime import datetime
import logging


def _create_logger(name: str) -> logging.Logger:
    """
    Create logger which logs to <timestamp>-<name>.log inside the current
    working directory.

    Parameters
    ----------
    name
        Name of the logger instance.
    """
    logger = logging.Logger(name.capitalize())
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    handler = logging.FileHandler(f"{now}-{name}.log")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


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
    logger = _create_logger(name="preprocessing")

    logger.info(f"Raw data directory: {raw_data_dir}")
    logger.info(f"Output directory: {output_dir}")

    #####################################################
    #                Add you code below.                #
    #####################################################

    logger.warning("Nothing implemented!")

    #####################################################
    #                Add you code above.                #
    #####################################################

    logger.info("Done!")


if __name__ == "__main__":
    from build_preprocessing_config import CONFIG_NAME

    with open(CONFIG_NAME, "r") as f:
        config = yaml.safe_load(f)

    main(**config)
