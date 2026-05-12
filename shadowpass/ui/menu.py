from getpass import getpass
from pathlib import Path
from typing import Dict

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text

from shadowpass.core.breach import HaveIBeenPwnedBreachChecker
from shadowpass.core.cracktime import CrackTimeEstimator
from shadowpass.core.entropy import calculate_entropy
from shadowpass.core.generator import PasswordGenerator
from shadowpass.core.hashgen import HashGenerator
from shadowpass.core.strength import PasswordStrengthAnalyzer
from shadowpass.ui.banner import display_banner

console = Console()


def _create_options_table() -> Table:
    table = Table(show_header=False, box=None)
    table.add_row("[bold green]1.[/bold green]", "Analyze Password")
    table.add_row("[bold green]2.[/bold green]", "Entropy Calculator")
    table.add_row("[bold green]3.[/bold green]", "Crack Time Estimator")
    table.add_row("[bold green]4.[/bold green]", "Breach Check")
    table.add_row("[bold green]5.[/bold green]", "Password Generator")
    table.add_row("[bold green]6.[/bold green]", "Hash Generator")
    table.add_row("[bold green]7.[/bold green]", "About")
    table.add_row("[bold green]8.[/bold green]", "Exit")
    return table


def _prompt_password(hidden: bool = False) -> str:
    if hidden:
        return getpass("Enter password: ")
    return Prompt.ask("Enter password", default="")


def _prompt_yes_no(label: str, default: str = "y") -> bool:
    answer = Prompt.ask(label, choices=["y", "n"], default=default)
    return answer.lower() == "y"


def _prompt_integer(label: str, default: int = 16, minimum: int = 4, maximum: int = 128) -> int:
    while True:
        try:
            value = int(Prompt.ask(label, default=str(default)))
            if minimum <= value <= maximum:
                return value
            console.print(f"[bold red][-] Enter a number between {minimum} and {maximum}.[/bold red]")
        except ValueError:
            console.print("[bold red][-] Invalid number. Please try again.[/bold red]")


def _render_panel(title: str, body: str) -> None:
    console.print(Panel(Text(body, style="green"), title=title, border_style="bright_green"))


def analyze_password() -> None:
    password = _prompt_password(hidden=False)
    if not password:
        console.print("[bold red][-] No password provided.[/bold red]")
        return

    analyzer = PasswordStrengthAnalyzer()
    report = analyzer.analyze_password(password)
    table = Table(title="Password Analysis", box=None)
    table.add_column("Metric", style="bold cyan")
    table.add_column("Value", style="green")
    table.add_row("Length", str(report["length"]))
    table.add_row("Uppercase", str(report["has_uppercase"]))
    table.add_row("Lowercase", str(report["has_lowercase"]))
    table.add_row("Digits", str(report["has_digits"]))
    table.add_row("Symbols", str(report["has_symbols"]))
    table.add_row("Repeated patterns", str(report["repeated_sequences"]))
    table.add_row("Sequential patterns", str(report["sequential_patterns"]))
    table.add_row("Common password", str(report["common_password"]))
    table.add_row("Rating", f"[bold yellow]{report['rating']}[/bold yellow]")
    table.add_row("zxcvbn score", str(report["zxcvbn_score"]))
    console.print(table)


def entropy_calculator() -> None:
    password = _prompt_password(hidden=False)
    if not password:
        console.print("[bold red][-] No password provided.[/bold red]")
        return

    entropy, pool = calculate_entropy(password)
    table = Table(title="Entropy Calculation", box=None)
    table.add_column("Metric", style="bold cyan")
    table.add_column("Value", style="green")
    table.add_row("Character pool size", str(pool))
    table.add_row("Entropy (bits)", f"{entropy}")
    console.print(table)


def crack_time_estimator() -> None:
    password = _prompt_password(hidden=False)
    if not password:
        console.print("[bold red][-] No password provided.[/bold red]")
        return

    estimator = CrackTimeEstimator()
    results = estimator.estimate(password)
    table = Table(title="Crack Time Estimation", box=None)
    table.add_column("Scenario", style="bold cyan")
    table.add_column("Years", style="green")
    table.add_column("Days", style="green")
    table.add_column("Hours", style="green")
    table.add_column("Minutes", style="green")
    for label in ["online", "offline_fast_hashing", "offline_slow_hashing"]:
        stats = results[label]
        table.add_row(
            label.replace("_", " ").title(),
            str(stats["years"]),
            str(stats["days"]),
            str(stats["hours"]),
            str(stats["minutes"]),
        )
    console.print(table)


def breach_check() -> None:
    password = _prompt_password(hidden=False)
    if not password:
        console.print("[bold red][-] No password provided.[/bold red]")
        return

    checker = HaveIBeenPwnedBreachChecker()
    try:
        count, prefix = checker.check_password(password)
        if count > 0:
            _render_panel(
                "Breach Detection",
                f"[bold red]This password has appeared {count} times in breach data.[/bold red]\nSHA1 range prefix: {prefix}",
            )
        else:
            _render_panel(
                "Breach Detection",
                "[bold green]Good news: this password does not appear in known breaches.[/bold green]",
            )
    except ConnectionError as exc:
        _render_panel("Error", f"[bold red]{exc}[/bold red]")


def password_generator() -> None:
    length = _prompt_integer("Password length", default=16, minimum=8, maximum=64)
    uppercase = _prompt_yes_no("Include uppercase? (y/n)")
    digits = _prompt_yes_no("Include digits? (y/n)")
    symbols = _prompt_yes_no("Include symbols? (y/n)")
    avoid_ambiguous = _prompt_yes_no("Avoid ambiguous characters? (y/n)")

    generator = PasswordGenerator()
    try:
        password = generator.generate(
            length=length,
            uppercase=uppercase,
            digits=digits,
            symbols=symbols,
            avoid_ambiguous=avoid_ambiguous,
        )
        _render_panel("Generated Password", f"[bold green]{password}[/bold green]")
    except ValueError as exc:
        _render_panel("Error", f"[bold red]{exc}[/bold red]")


def hash_generator() -> None:
    secret = _prompt_password(hidden=True)
    if not secret:
        console.print("[bold red][-] No value provided to hash.[/bold red]")
        return

    hasher = HashGenerator()
    table = Table(title="Hash Generator", box=None)
    table.add_column("Algorithm", style="bold cyan")
    table.add_column("Digest", style="green")
    table.add_row("MD5", hasher.md5(secret))
    table.add_row("SHA1", hasher.sha1(secret))
    table.add_row("SHA256", hasher.sha256(secret))
    table.add_row("bcrypt", hasher.bcrypt_hash(secret))
    console.print(table)


def about_panel() -> None:
    about_text = (
        "ShadowPass is a defensive password security framework inspired by Kali Linux tools.\n"
        "It is designed for local analysis, entropy calculation, breach detection, secure password generation, and hashing.\n"
        "All features are built for defensive use and secure password hygiene."
    )
    _render_panel("About ShadowPass", about_text)


def display_menu() -> None:
    while True:
        display_banner()
        console.print(Panel(_create_options_table(), title="Main Menu", border_style="bright_green"))
        choice = Prompt.ask("Choose an option", choices=[str(i) for i in range(1, 9)], default="8")

        if choice == "1":
            analyze_password()
        elif choice == "2":
            entropy_calculator()
        elif choice == "3":
            crack_time_estimator()
        elif choice == "4":
            breach_check()
        elif choice == "5":
            password_generator()
        elif choice == "6":
            hash_generator()
        elif choice == "7":
            about_panel()
        elif choice == "8":
            console.print("[bold green][+] Exiting ShadowPass. Stay secure.[/bold green]")
            break

        console.print()
        Prompt.ask("Press enter to return to the menu", default="")
        console.clear()
