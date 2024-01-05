# IPA Project Structure
The IPA projects structure aims to support the whole development cycle of your project.

## Project Root
In the project root directory (e.g. `faim_demo-project`) we have the `README.md` and `LICENSE` files as well as two hidden files `.gitignore` and `.pre-commit-config.yaml`.

`README.md`
:  The `README.md` is the entry point to your project. This is a great place to add an abstract outlining your project and maybe even add a teaser image. If you host your project on GitHub, GitHub will use the content of this file and render it as welcome page for the repository.

`LICENSE`
:  We have opted for a BSD 3-Clause License by default. More information about licenses can be found on [choosealicense.com](https://choosealicense.com/) and you can always edit the default license.

`.gitignore`
: This file becomes relevant if you decide to host your project on GitHub. Essentially it tells git which files it is not allowed to upload to GitHub.

`.pre-commit-config.yaml`
: Like `.gitignore`, this file becomes relevant once you start versioning your code with git. [Pre-commit](https://pre-commit.com/) is a tool which formats your code before it undergoes version control, which helps to spot actual code differences.

`.copier-answers.yml`
: This document is created by copier to keep track of your [answers](https://copier.readthedocs.io/en/stable/configuring/#answers_file).

## infrastructure
In this directory we keep everything related to infrastructure.
Most importantly we document which tools are required to run the image processing and analysis of this project.

`REAMDE.md`
: Use the `README.md` in this directory to document the tools which you use in this project and how they can be installed.

`apps`
: Install the necessary tools (e.g. Fiji) into this directory. Do not forget to document which version of the tool you are using and how to install it. The contents of this sub-directory are ignored by git and not versioned.

`env-yamls`
: Use this directory to save [environment files](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually). By default we provide a basic environment file (e.g. `demo-project-env.yaml`), which contains a set of packages to get you started with IPA in Python.

## scratchpad
This is your playground.
Do you have a new idea that you want to try out?
Spin up a new jupyter notebook and go try it out.
Use git to version these notebooks and keep track of how your ideas develop over time.

```{caution}
Treat this really as a playground. Do not use scratchpad code for your final analysis runs.
```

`stackview-demo.ipynb`
: This is a short demo notebook which uses [stackview](https://github.com/haesleinhuepf/stackview) to display an image inside a jupyter notebook.

## ipa
This is where your image processing and analysis code lives which is used to produce final results.
Our recommendation is to separate your processing and analysis into several steps. For example
1. preprocessing,
2. segmentation, and
3. feature extraction.

Each of these steps has its respective sub-directory (e.g. `s01_preprocessing`) containing two scripts:
* One to build a config file from user inputs.
* One to run the step with the respective config file.

```{note}
This directory should only contain code.
```

## runs
Here we keep track of individual IPA runs.
The idea is to create for each run a dedicated sub-directory where the config files for the different `ipa` steps are saved.
Each script will create a log-file and store it next to the config file.
This allows us to keep track of each individual run and we can even use git to version them.

`example/README.md`
: An example run with instructions on how to run the defaults `ipa` steps.

## docs
This directory contains all the files used by [sphinx](https://www.sphinx-doc.org/en/master/tutorial/index.html) to create a documentation website.
This documentation website can be hosted on GitHub and serve as entry point to your IPA project.
