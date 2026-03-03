#!/usr/bin/env python3

"""
Exercise 3: Vault Security

This module demonstrates secure file operations using the with
statement (context manager) to ensure proper resource management
in the Cyber Archives.
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


def secure_extraction(filename: str) -> str:
    """Perform secure file opening and reading."""
    try:
        with open(filename, "r") as vault:
            extracted_data = vault.read()
        return extracted_data
    except (FileNotFoundError, OSError) as e:
        print(mag(" ERROR!") + f"{e}")
        return ""


def secure_preservation(src: str, dst: str) -> None:
    """Perform secure file opening and writing."""
    extracted_data = secure_extraction(src)
    if extracted_data == "":
        return
    try:
        with open(dst, "w") as vault:
            vault.write(extracted_data)
        print(secure_extraction(dst))
    except OSError as e:
        print(mag(" ERROR!") + f"{e}")


def main() -> None:
    """Entry point to perform secure file operations."""
    print("\n " + bold("🔒 CYBER ARCHIVES - VAULT SECURITY SYSTEM"))
    print(" " + "-" * 60)

    print(" Initiating secure vault access...")
    print(" Vault connection established with failsafe protocols")

    print(bold("\n SECURE EXTRACTION:"))
    print(" " + "-" * 60)
    print(secure_extraction("classified_data.txt"))
    print(" " + "-" * 60)

    print(bold("\n SECURE PRESERVATION:"))
    print(" " + "-" * 60)
    secure_preservation("security_protocols.txt", "secure_vault.txt")
    print(" " + "-" * 60)

    print()
    print(" Vault automatically sealed upon completion")
    print(cyan(" All vault operations completed with maximum security."))
    print()


if __name__ == "__main__":
    main()
