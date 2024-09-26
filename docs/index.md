{!README.md!lines=2-3}

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
Copier will ask you a series of questions whose answers will be used to generate a tailored IPA project for you. To start the process run the following and replace `my-ipa-project` with the name of your project directory:
```bash
pixi x copier copy git+https://github.com/fmi-faim/ipa-project-template my-ipa-project
```

!!! success "Congratulations!"
    You have created a new personalized IPA project! Now you can change into the project root-directory with
    ```bash
    cd my-ipa-project
    ```
    or open the directory in your file browser.
