import webbrowser

from fire import Fire

from app.src.my_import import hello_world_string


class Entrypoint:
    """Main entrypoint for the AutoDownload from Clipboard tool.

    This class provides the primary command-line interface for the application.
    """

    def __call__(self, url: str | None = None) -> None:
        """Runs the default command.

        Args:
            url (str | None): Optional; A URL to open in the web browser. If not provided,
                only the hello world string is printed.
        """
        self.main(url)

    def main(self, url: str | None = None) -> None:
        """Main command function.

        Prints a hello world string and optionally opens a given URL in the default web browser.

        Args:
            url (str | None): Optional; The URL to open. If None, only the message is printed.
        """
        print(hello_world_string)
        if url:
            webbrowser.open(url)

    def other_command(self) -> None:
        """Prints an example message.

        This method demonstrates an additional command in the interface.
        """
        print("This is another command")


def main() -> None:
    """Entry point for the command-line interface.

    Initializes the Fire CLI with the Entrypoint class.
    """
    Fire(Entrypoint)
