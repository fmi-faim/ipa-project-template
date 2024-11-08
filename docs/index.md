{!README.md!lines=2-3}

!!! example "Example Project"
    Take a look at our [example-project](https://fmi-faim.github.io/example-project/) if you'd like to see the template in action!


## Prerequisites
In our project template we use [pixi.sh](https://pixi.sh) as environment manager and [copier](https://copier.readthedocs.io/en/stable/) to generate a copy of the project template. The installation instructions for pixi can be found [here](https://pixi.sh/latest/#installation).
After successful installation of pixi and restarting your terminal, you can type `pixi info` to get the current version of pixi.

??? info "Update pixi"
    If you have installed pixi already, please make sure to update it to the latest version by running:
    ```bash
    pixi self-update
    ```

Now install copier as a global package with pixi:
```bash
pixi global install copier
```

## Generate an IPA Project with Copier
Copier will ask you a series of questions whose answers will be used to generate a tailored IPA project for you. To start the process provide the name of your project and then copy the command:

{{{user-defined-values}}}

```bash
pixi x copier copy git+https://github.com/fmi-faim/ipa-project-template PROJECT_NAME
```

!!! success "Congratulations!"
    You have created a new personalized IPA project! Now you can change into the project root-directory with
    ```bash
    cd PROJECT_NAME
    ```
    or open the directory in your file browser.
