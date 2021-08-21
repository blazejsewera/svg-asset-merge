# Svg asset merge

Simple script to convert multiple svgs into one.

Especially useful when generating Affinity Designer assets
from multiple svg files (like an icon pack).
Tested with [feather icons](https://feathericons.com).

Usage:
```sh
python3 merge.py -o merged.svg icon_dir
```

Then open merged.svg in Affinity Designer, select all the layers
(e.g. with shift), and from Assets menu select 'Add from selection'.
