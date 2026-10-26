from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CATALOG = ROOT / "ports" / "portsdr-projects.md"
START = "<!-- BEGIN PORTSDR CATALOG -->"
END = "<!-- END PORTSDR CATALOG -->"


def main():
    catalog = CATALOG.read_text(encoding="utf-8")
    catalog = catalog.replace(
        "| SNES | Donkey Kong Country 3: Dixie's Double Trouble! |",
        "| SNES | Donkey Kong Country 3: Dixie Kong's Double Trouble! |",
    )
    CATALOG.write_text(catalog, encoding="utf-8", newline="\n")

    lines = catalog.splitlines()
    table_start = next((i for i, line in enumerate(lines) if line.startswith("| Plataforma original |")), None)
    if table_start is None:
        raise ValueError("Could not find the PortsDR catalogue table")

    rows = [line for line in lines[table_start:] if line.startswith("|") and "[GitHub](https://github.com/" in line]
    links = re.findall(r"\[GitHub\]\((https://github\.com/[^)]+)\)", "\n".join(rows))
    if not rows or len(rows) != len(links) or len(set(links)) != len(links):
        raise ValueError(f"Invalid catalogue rows or duplicate links: {len(rows)} rows, {len(set(links))} unique links")

    section = "\n## Catálogo completo por plataforma original\n\n" \
        "La lista conserva la plataforma original de la fuente; no implica que el destino esté confirmado. " \
        "Los enlaces del catálogo se muestran aquí para que puedas recorrerlos desde esta portada. " \
        "El [catálogo fuente](ports/portsdr-projects.md) mantiene la instantánea completa y los detalles de origen.\n\n" \
        + "\n".join(lines[table_start:])

    readme = README.read_text(encoding="utf-8")
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError("README must contain exactly one pair of catalogue markers")
    before, rest = readme.split(START, 1)
    _, after = rest.split(END, 1)
    README.write_text(before + START + section + "\n" + END + after, encoding="utf-8", newline="\n")
    print(f"Synced {len(rows)} catalogue links into README.md")


if __name__ == "__main__":
    main()
