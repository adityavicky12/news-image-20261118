#!/usr/bin/env python3
"""Copy the bundled news image to the harness output directory.

The entry is the image in news.png: a four-panel editorial illustration
summing up one day's world news, with a masthead naming the day and one
factual caption per panel. This program does no network access and no
drawing at run time; it copies the file byte for byte, so repeated runs
are identical.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "news.png", out_dir / "entry.png")


if __name__ == "__main__":
    main()
