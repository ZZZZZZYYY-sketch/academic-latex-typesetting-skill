#!/usr/bin/env python3
"""Render all pages in a PDF to PNG via Poppler's pdftoppm.

Usage: python render_pages.py document.pdf --out-dir qa_pages --dpi 160
Requires an installed `pdftoppm` executable on PATH.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="PDF to render")
    parser.add_argument("--out-dir", type=Path, default=Path("pdf_pages"))
    parser.add_argument("--dpi", type=int, default=160)
    args = parser.parse_args()

    if not args.pdf.is_file():
        parser.error(f"PDF not found: {args.pdf}")
    if not 72 <= args.dpi <= 400:
        parser.error("--dpi must be between 72 and 400")
    exe = shutil.which("pdftoppm")
    if exe is None:
        parser.error("pdftoppm was not found on PATH; install Poppler or render with an equivalent PDF viewer")
    args.out_dir.mkdir(parents=True, exist_ok=True)
    prefix = args.out_dir / "page"
    command = [exe, "-f", "1", "-r", str(args.dpi), "-png", str(args.pdf), str(prefix)]
    subprocess.run(command, check=True)
    pages = sorted(args.out_dir.glob("page-*.png"))
    print(f"Rendered {len(pages)} page(s) to {args.out_dir}")
    print("Please inspect EVERY page image; rendering alone is not visual verification.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
