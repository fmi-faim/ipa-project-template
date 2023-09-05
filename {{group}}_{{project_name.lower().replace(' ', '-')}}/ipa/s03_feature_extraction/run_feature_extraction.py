"""
run_feature_extraction.py
=========================

This script expects feature_extraction_config.yaml to be present in the
current working directory.
"""

import yaml
from ..utils import create_logger

CONFIG_NAME = "feature_extraction_config.yaml"


def main(input_dir: str, output_dir: str) -> None:
    """
    Apply feature_extraction step to data in input_dir.

    Parameters
    ----------
    input_dir
        Directory containing all input data.
    output_dir
        Directory where the preprocessed data is saved.

    """
    logger = create_logger(name="feature_extraction")

    logger.info(f"Input directory: {input_dir}")
    logger.info(f"Output directory: {output_dir}")

    logger.warning("Not implemented!")

    logger.info("Done!")


if __name__ == "__main__":
    with open(CONFIG_NAME, "r") as f:
        config = yaml.safe_load(f)

    main(**config)
