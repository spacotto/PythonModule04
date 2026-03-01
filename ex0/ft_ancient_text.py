#!/usr/bin/env python3
"""
ft_ancient_text.py - Ancient Text Recovery Module

This module recovers ancient data fragments from storage vaults
in the Cyber Archives system.

In other words, a "cat file.txt" with extra steps.
"""


def bold(text: str) -> str:
    """A function making strings of text bold."""
    w, r = "\033[1;97m", "\033[0m"
    return f"{w}{text}{r}"


def recover_ancient_text(filename: str) -> None:
    """Recover and display data from a given file."""
    print("\n" + bold(" 📜 CYBER ARCHIVES - DATA RECOVERY SYSTEM"))
    print(" " + "-" * 60)
    print(bold(" Accessing Storage Vault: ") + f"{filename}")

    try:
        file = open(filename, "r")
        print(" Connection established...\n")
        content = file.read()
        print(bold(" RECOVERED DATA:"))
        print(" " + "-" * 60)
        print(content)
        print(" " + "-" * 60)
        file.close()
        print(" Data recovery complete. Storage unit disconnected.")
        print()
    except FileNotFoundError:
        print(bold(" 🚨 ERROR: ") + "Storage vault not found!")
        print(" Have you tried to run data generator first?")
        print(" Are you sure filename is correct?")
        print()


if __name__ == "__main__":
    recover_ancient_text("ancient_fragment.txt")
