from pathlib import Path


def main():
    raw = input("Enter a file or directory path: ").strip()
    p = Path(raw)

    print(f"Absolute path: {p.absolute()}")
    print(f"Parent: {p.parent}")
    print(f"Name: {p.name}")
    print(f"Stem: {p.stem}")
    print(f"Suffix: {p.suffix}")


if __name__ == "__main__":
    main()
