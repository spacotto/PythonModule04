#!/usr/bin/env python3

"""
Exercise 2: Stream Management

This module demonstrates the use of the three sacred data channels
of the Cyber Archives: stdin, stdout, and stderr.
"""

import sys


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


def ft_input(message: str) -> str:
    """Reproduce the the behaviour of built-in function input()."""
    print(message, end="", flush=True)
    return sys.stdin.readline().strip()


def ft_print(message: str) -> str:
    """Reproduce the the behaviour of built-in function print()."""
    sys.stdout.write(f"{message}\n")


def ft_error(message: str) -> str:
    """Reproduce the the behaviour of built-in function print()."""
    sys.stderr.write(f"{message}\n")


def stream_management() -> None:
    """Collect input and route messages to the correct streams."""
    print("\n " + bold("🌐 CYBER ARCHIVES - COMMUNICATION SYSTEM"))
    print(" " + "-" * 60)

    archivist_id = input(bold(" Input Stream active. Enter archivist ID: "))
    status_report = input(bold(" Input Stream active. Enter status report: "))
    print()

    print(f" [STANDARD] Archive status from {archivist_id}: {status_report}")
    ft_error(" [ALERT] System diagnostic: Communication channels verified")
    print(" [STANDARD] Data transmission complete")
    print()

    print(cyan(" Three-channel communication test successful."))
    print()


if __name__ == "__main__":
    stream_management()
