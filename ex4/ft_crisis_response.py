#!/usr/bin/env python3

"""
Exercise 4: Crisis Response

This module implements a crisis management system that handles
different types of archive access failures gracefully using
try/except blocks and the with statement.
"""


def bold(text: str) -> str:
    """A function making strings of text bold."""
    w, r = "\033[1;97m", "\033[0m"
    return f"{w}{text}{r}"


def cyan(text: str) -> str:
    """A function making strings of text bold and cyan."""
    c, r = "\033[1;96m", "\033[0m"
    return f"{c}{text}{r}"


def mag(text: str) -> str:
    """A function making strings of text bold and magenta."""
    m, r = "\033[1;95m", "\033[0m"
    return f"{m}{text}{r}"


def crisis_handler(filename: str) -> None:
    """Handle archive access attempts and manage failures gracefully."""
    try:
        with open(filename, "r") as vault:
            content = vault.read()
        print(f" {bold('ROUTINE ACCESS:')}" +
              " Attempting access to '{filename}'...")
        print(cyan(" SUCCESS: Archive recovered: ") + f"'{content}'")
        print(" STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f" {bold('CRISIS ALERT:')} Attempting access to '{filename}'...")
        print(mag(" RESPONSE: Archive not found in storage matrix"))
        print(" STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f" {bold('CRISIS ALERT:')} Attempting access to '{filename}'...")
        print(mag(" RESPONSE: Security protocols deny access"))
        print(" STATUS: Crisis handled, security maintained")
    except OSError as e:
        print(f" {bold('CRISIS ALERT:')} Attempting access to '{filename}'...")
        print(mag(f" RESPONSE: {e}"))
        print(" STATUS: Crisis handled")
    finally:
        print()


def main() -> None:
    """Entry point for the crisis response system."""
    print("\n " + bold("🚨 CYBER ARCHIVES - CRISIS RESPONSE SYSTEM"))
    print(" " + "-" * 60)

    print()
    # 1. FileNotFoundError test
    crisis_handler("lost_archive.txt")
    # 2. PermissionError test
    crisis_handler("classified_vault.txt")
    # 3. No error test
    crisis_handler("standard_archive.txt")

    print(bold(" All crisis scenarios handled successfully. Archives secure."))
    print()


if __name__ == "__main__":
    main()
