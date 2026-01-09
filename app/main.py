import webbrowser

from fire import Fire

from app.src.my_import import hello_world_string


class Entrypoint:
    """This docstring is the main documentation"""

    def __call__(self, url: str | None = None) -> None:
        """Default command"""
        self.main(url)

    def main(self, url: str | None = None) -> None:
        """Main command"""
        print(hello_world_string)
        if url:
            webbrowser.open(url)

    def other_command(self) -> None:
        """Another command example"""
        print("This is another command")


def main() -> None:
    Fire(Entrypoint)
