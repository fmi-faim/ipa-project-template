# Example
<!-- start processing steps summary -->
The image processing and analysis of this project is organized in three steps:
1. preprocessing,
2. segmentation,
3. and feature extraction.

The required scripts are organized in the `ipa` directory. Each step follows the pattern of building a config file and then running the respective script.
Each run should have its respective run-directory. Inside the run-directory the config files and log files are stored.
<!-- end processing steps summary -->

Before running the scripts you must [activate your environment](../../infrastructure/apps/README.md).

<!-- start instructions -->
## s01_preprocessing
```{note}
The scripts write the config and log files into the current working directory. In this example it is assumed that you are in `runs/example`.
```
1. Build preprocessing config:<br>
    `python ../../ipa/s01_preprocessing/build_preprocessing_config.py`
2. Run preprocessing:<br>
    `python ../../ipa/s01_preprocessing/run_preprocessing.py`

## s02_segmentation
1. Build segmentation config:<br>
    `python ../../ipa/s02_segmentation/build_segmentation_config.py`
2. Run segmentation:<br>
    `python ../../ipa/s02_segmentation/run_segmentation.py`

## s03_feature_extraction
1. Build feature extraction config:<br>
    `python ../../ipa/s03_feature_extraction/build_feature_extraction_config.py`
2. Run feature extraction:<br>
    `python ../../ipa/s03_feature_extraction/run_feature_extraction.py`
<!-- end instructions -->
