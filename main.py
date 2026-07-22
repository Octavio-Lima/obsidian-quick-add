from app.vault import get_default_vault
from os import mkdir
from pathlib import Path


def main():
    vault = get_default_vault()
    title = ""

    while title == "":
        title = input("Enter the markdown file title: ")

    with open(Path(vault.path, title + ".md"), "w", encoding="utf-8") as f:
        f.write("a")


if __name__ == "__main__":
    main()
