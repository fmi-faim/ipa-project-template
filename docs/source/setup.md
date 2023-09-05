# Generate IPA Project
These install instructions guide you through the necessary steps to generate a new Image Processing & Analysis (IPA) project with [copier](https://copier.readthedocs.io/en/stable/).

## Prerequisits
Generating a copy of this project template requires the [copier](https://copier.readthedocs.io/en/stable/) library and command line interface (CLI) app.
Our recommended way to install copier is to create a fresh environment using the [Mambaforge](https://conda-forge.org/miniforge/) environment manager.

0. If you do not have Mambaforge installed on your system download the latest version from [here](https://conda-forge.org/miniforge/) and install it.
1. Create a new environment and install copier:</br>
    `mamba create -n copier-env -y python=3.9 -c conda-forge copier`
2. Activate the environment:</br>
    `mamba activate copier-env`

```{note}
Your command line promt should now be prefixed with `(copier-env)`.
```

## Generate an IPA Project with Copier
Copier will ask you a series of questions whose answers will be used to generate a tailored IPA project for you.
To start the generation process run

```bash
copier copy git+https://github.com/fmi-faim/ipa-project .
```

inside your CLI with the active `copier-env` environment.
This will copy the personalized IPA project template into the current working directory.

```{note}
You can replace the `.` with the path to the desired destination directory.
```

Congratulations you have created a new personalized IPA project!
