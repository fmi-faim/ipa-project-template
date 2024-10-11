from pathlib import Path

import questionary
from faim_ipa.utils import IPAConfig, get_git_root


class DemoConfig(IPAConfig):
    raw_data_dir: Path = get_git_root() / "raw_data"

    def config_name(self) -> str:
        return "demo_config.yaml"

    def prompt(self):
        self.raw_data_dir = Path(
            questionary.path(
                "Select the raw_data dir:",
                default=str(get_git_root() / "raw_data"),
            ).ask()
        )

        self.save()


if __name__ == "__main__":
    config = DemoConfig()
    config.prompt()
