import time

from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

console = Console()


def run_startup_animation() -> None:
    """Display a loading animation as modules initialize."""
    steps = [
        "[green][+] Initializing ShadowPass Framework...[/green]",
        "[green][+] Loading security modules...[/green]",
        "[green][+] Entropy engine loaded...[/green]",
        "[green][+] Hash engine loaded...[/green]",
        "[green][+] Password generator loaded...[/green]",
    ]

    with Live(console=console, refresh_per_second=4) as live:
        for step in steps:
            panel = Panel(
                Align.center(Text(step, style="bold green"), vertical="middle"),
                border_style="bright_green",
                padding=(1, 2),
            )
            live.update(panel)
            time.sleep(0.7)

    console.print("[bold green][+] ShadowPass is ready.[/bold green]\n")
