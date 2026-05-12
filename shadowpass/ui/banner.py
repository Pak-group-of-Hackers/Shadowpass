from colorama import init as colorama_init
from pyfiglet import Figlet
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

HoodedAsciiArt = """\
              .-\"\"\"-.
             /       \\
            /  .-=-.  \\
           /  /  _  \\  \\
          /  /  / \\  \\  \\
         /  /__/___\\__\\  \\
        /               \\
        |  #############  |
        |  #           #  |
        |  #  SHADOW    #  |
        |  #           #  |
        |  #############  |
         \\               /
          `-._______ .-'
"""

def display_startup_banner() -> None:
    """Render a full startup splash screen for ShadowPass."""
    colorama_init(autoreset=True)
    fig = Figlet(font="slant")
    title = fig.renderText("SHADOWPASS")
    title_text = Text(title, style="bold green")

    info_text = Text(
        "System : Kali Linux\n"
        "User   : root\n"
        "Terminal : ShadowPass Console\n"
        "Version  : 1.0.0\n"
        "Codename : ANONYMOUS\n",
        style="bold white",
    )

    left_panel = Panel(
        Text(HoodedAsciiArt, style="green"),
        border_style="bright_green",
        title="ShadowPass",
        subtitle="PAK GROUP OF HACKERS",
        padding=(1, 2),
    )

    right_panel = Panel(
        info_text,
        title="System Info",
        border_style="bright_green",
        padding=(1, 2),
    )

    console.print(Columns([left_panel, right_panel], expand=True))
    console.print(Panel(title_text, border_style="bright_green", padding=(1, 2)))
    console.print(Text("We are anonymous. We are legion. We do not forgive.\nWe do not forget. Expect us.", style="green"))
    console.print()


def display_banner() -> None:
    """Render the ShadowPass ASCII banner and display the project header."""
    colorama_init(autoreset=True)
    fig = Figlet(font="slant")
    title = fig.renderText("ShadowPass")
    title_text = Text(title, style="bold green")
    subtitle = Text("Defensive Password Security Framework", style="bold white on black")
    header = Text("[ PAK GROUP OF HACKERS ]", style="bold cyan")

    panel = Panel(
        Text.assemble(title_text, "\n", subtitle, "\n", header),
        title="ShadowPass",
        border_style="bright_green",
        padding=(1, 2),
        subtitle_align="center",
    )

    console.print(panel)
    console.print(
        Text(
            "Hooded cyber defense theme with Kali inspired terminal control.",
            style="green",
        )
    )
    console.print()
