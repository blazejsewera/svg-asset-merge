import re
from pathlib import Path
import argparse


def main():
    """
    Simple script to convert multiple svgs into one.

    Especially useful when generating Affinity Designer assets
    from multiple svg files (like an icon pack).
    Tested with feather icons.

    Usage: python3 merge.py -o merged.svg icon_dir
    Then open merged.svg in Affinity Designer, select all the layers
    (e.g. with shift), and from Assets menu select 'Add from selection'.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("dir")
    parser.add_argument("--out", "-o", required=True, help="Output file to write to")
    args = parser.parse_args()

    dir = Path(args.dir)
    outfile = Path(args.out)

    merged_svgs = ""

    for file in dir.iterdir():
        with open(file, "r") as in_file:
            svg = in_file.read()
            name = re.sub(r"\.svg$", "", file.name)
            _svg = re.sub(r' xmlns=".*?"', "", svg)
            _svg = re.sub(r' width="[0-9]*"', "", _svg)
            _svg = re.sub(r' height="[0-9]*"', "", _svg)
            _svg = re.sub(r' viewBox="[0-9 ]*"', "", _svg)
            _svg = re.sub(r"<svg( ?)", r"<g\1", _svg)
            _svg = re.sub(r"</svg>", "</g>", _svg)
            svg_group = re.sub(r"<g([ >])", f'<g id="{name}"\\1', _svg)
            merged_svgs = "\n".join((merged_svgs, svg_group))

    final_svg = (
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg width="100px" height="100px" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">\n'
        f"{merged_svgs}\n"
        f"</svg>\n"
    )

    with open(outfile, "w") as out_file:
        out_file.write(final_svg)


if __name__ == "__main__":
    main()
