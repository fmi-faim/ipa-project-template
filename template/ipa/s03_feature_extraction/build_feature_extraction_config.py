"""
build_feature_extraction_config.py
==================================

Ask for user input via command line interface (CLI) to build the
feature_extraction_config.yaml. The feature_extraction_config.yaml
is consumed by the run_feature_extraction.py script.
"""


import os
import questionary
import yaml

CONFIG_NAME = "feature_extraction_config.yaml"


def main() -> None:
    """
    Create feature_extraction_config.yaml from user inputs.
    """
    cwd = os.getcwd()

    input_dir = questionary.path("Path to raw data directory:").ask()
    segmentation_dir = questionary.path("Path to segmentation directory:").ask()
    output_dir = questionary.path("Path to output directory:").ask()

    output_dir = os.path.join(output_dir, "03_feature_extraction")

    config = {
        "input_dir": os.path.relpath(input_dir, cwd),
        "segmentation_dir": os.path.relpath(segmentation_dir, cwd),
        "output_dir": os.path.relpath(output_dir, cwd),
    }

    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(cwd, CONFIG_NAME), "w") as f:
        yaml.safe_dump(config, f)


if __name__ == "__main__":
    main()
