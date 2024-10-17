# Optional Features
The template provides a set of optional features that can be added to your project. You can add these features to an existing project by re-running the copy command and updating your answers to the copier-questions.

__Python Batteries Included__

:    Adds a set of Python packages that we commonly use in our image processing and analysis projects.

__napari__

:   Adds napari to the project. To run napari, you can use the command `pixi run napari`.

__nextflow__

:   Adds nextflow as a dependency and a dummy workflow to `source`. The dummy workflow can be executed by running `pixi run nextflow`.

__Unix installation and init scripts__

:   Adds script to install and initialize pixi on Unix systems. We use these scripts with our local HPC setup.

__Add Demo__

:   Adds a demo processing step with `config.py` and `run.py` to the `source/s01_demo` directory. The config can be built with `pixi run build_config` and the demo can be executed with `pixi run demo`.
