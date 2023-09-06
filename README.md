<!-- start introduction -->
# Image Processing & Analysis Project Template

Image Processing & Analysis (IPA) plays a vital role in life sciences, yet managing code snippets, scripts, configurations, and documentation can pose significant challenges. This [Copier Template](https://copier.readthedocs.io/en/stable/) offers a valuable resource, especially for those new to IPA projects. It's designed to enhance the Findability, Accessibility, Interoperability, and Reusability (the FAIR principles) of image processing and analysis routines, making it an excellent choice for simplifying and structuring your work.

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
    mamba create -n copier python=3.9 -c conda-forge copier
    mamba activate copier
    ```
2. Copy the template:
    ```bash
    copier copy git+https://github.com/fmi-faim/ipa-project-template faim_demo-project
    ```

For detailed instructions, please refer to the [documentation](https://fmi-faim.github.io/ipa-project-template/setup.html).

## License
This project is licensed under the [MIT License](LICENSE).
