# Generate IPA Project
These install instructions guide you through the necessary steps to generate a new Image Processing & Analysis (IPA) project with [copier](https://copier.readthedocs.io/en/stable/).

## Prerequisites
Generating a copy of this project template requires the [copier](https://copier.readthedocs.io/en/stable/) library and command line interface (CLI) app.
Our recommended way to install copier is to create a fresh environment using the [Mambaforge](https://conda-forge.org/miniforge/) environment manager.

0. If you do not have Mambaforge installed on your system, download the latest version from [here](https://conda-forge.org/miniforge/) and install it.
1. Create a new environment and install copier:</br>
    ```
    mamba create -y -n copier-env python=3.9 copier -c conda-forge
    ```
2. Activate the environment:</br>
    ```
    mamba activate copier-env
    ```

```{note}
Your command line promt should now be prefixed with `(copier-env)`.
```

## Generate an IPA Project with Copier
Copier will ask you a series of questions whose answers will be used to generate a tailored IPA project for you.
To start the generation process run:

```bash
copier copy git+https://github.com/fmi-faim/ipa-project-template faim_demo-project
```

inside your CLI with the active `copier-env` environment.
This will copy the personalized IPA project template into the current working directory.

```{note}
The template will create a directory `faim_demo-project` and copy all required files into it.
```

Congratulations you have created a new personalized IPA project!

Now you can deactivate the `copier-env` and change into the project root-directory with

```bash
mamba deactivate
cd faim_demo-project
```

or open the directory in your file browser.
