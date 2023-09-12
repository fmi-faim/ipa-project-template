<!-- start introduction -->
# Image Processing & Analysis Project Template
Image Processing and Analysis (IPA), transforming raw image data into quantitative measurements, is an important part of life sciences. However, as projects progress, IPA pipelines grow increasingly complex, involving the management of multiple tools, versions, and dependencies, which can be a challenging task. To tackle this complexity, we introduce the IPA Project [Copier](https://copier.readthedocs.io/en/stable/) Template. This template simplifies the initiation of new IPA projects and streamlines the reorganization of existing ones, contributing to research that is more Findable, Accessible, Interoperable, and Reusable (FAIR) promoting efficiency, reproducibility, and reliability in life sciences research.

## Usage
* **Newcomers:**
    If you're new to IPA, this template provides a structured starting point to simplify your project setup.
* **Experienced Users:**
    Seasoned practitioners will appreciate the quicker setup for new projects.

## Features
* Easy setup and configuration.
* Standardized directory structure for consistency.
* Configured [Sphinx](https://www.sphinx-doc.org/en/master/) documentation template.
* Configured `environment.yaml` to get started with image processing and analysis in Python.
<!-- end introduction -->

## Quick Start
1. Create a Copier environment:
    ```bash
    mamba create -n copier python=3.9 copier -c conda-forge
    mamba activate copier
    ```
2. Copy the template:
    ```bash
    copier copy git+https://github.com/fmi-faim/ipa-project-template faim_demo-project
    ```

For detailed instructions, please refer to the [documentation](https://fmi-faim.github.io/ipa-project-template/setup.html).

## License
This project is licensed under the [MIT License](LICENSE).
