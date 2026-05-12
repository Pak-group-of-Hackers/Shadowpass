from rich.console import Console

from shadowpass.ui.animations import run_startup_animation
from shadowpass.ui.menu import display_menu

console = Console()


def main() -> None:
    console.clear()
    run_startup_animation()
    display_menu()


if __name__ == "__main__":
    main()
