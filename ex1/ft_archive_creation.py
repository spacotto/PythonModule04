#!/usr/bin/env python3

"""
Exercise 1: Archive Creation
This module creates new archive entries in the Cyber Archives
preservation system.

Objective: write into files.
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


def create_archive(filename: str) -> None:
    """Create a new archive file and inscribe data entries into it."""
    print("\n " + bold("📜 CYBER ARCHIVES - PRESERVATION SYSTEM"))
    print(" " + "-" * 60)

    print(bold("\n Initializing new storage unit: ") + f"{filename}")
    try:
        file = open(filename, "w")
        print(cyan(" Storage unit created successfully..."))
    except (PermissionError, OSError) as e:
        print(mag(" ERROR: ") + f"{e}")
        return
    finally:
        print()

    data_entries = ["[ENTRY 001] New quantum algorithm discovered",
                    "[ENTRY 002] Efficiency increased by 347%",
                    "[ENTRY 003] Archived by Data Archivist trainee"]

    print(bold(" Inscribing preservation data..."))
    print(" " + "-" * 60)

    try:
        for entry in data_entries:
            file.write(entry)
            print(f" {entry}")
    except (OSError) as e:
        print(mag(" ERROR: ") + f"{e}")
        return
    finally:
        print(" " + "-" * 60)
        file.close()
        print(" Data inscription complete. Storage unit sealed.")

    print(f" Archive '{filename}' ready for long-term preservation.")
    print()


if __name__ == "__main__":
    create_archive("new_discovery.txt")
