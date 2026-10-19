#!/usr/bin/env python3
"""Small, dependency-free LaTeX log triage helper.

Usage: python check_latex_log.py path/to/main.log
Exit: 0 if no likely fatal or unresolved-reference problems; 1 otherwise.
This does not certify a visually correct PDF.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

PATTERNS = {
    "latex_error": re.compile(r"(?m)^! (?:LaTeX Error|Package .* Error|Undefined control sequence|Emergency stop|I can't find file|File .* not found)"),
    "undefined_reference": re.compile(r"(?:LaTeX Warning: Reference .* undefined|LaTeX Warning: There were undefined references|Reference .* on page .* undefined)"),
    "undefined_citation": re.compile(r"(?:Citation .* undefined|There were undefined citations|Please \(re\)run Biber|Please rerun Biber)"),
    "overfull_hbox": re.compile(r"Overfull \\hbox"),
    "overfull_vbox": re.compile(r"Overfull \\vbox"),
    "underfull_hbox": re.compile(r"Underfull \\hbox"),
    "underfull_vbox": re.compile(r"Underfull \\vbox"),
    "font_warning": re.compile(r"(?:Font shape .* not available|Font .* not loadable|Missing character:)", re.IGNORECASE),
}
FATAL = {"latex_error", "undefined_reference", "undefined_citation"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log", type=Path, help="Path to LaTeX .log file")
    args = parser.parse_args()
    if not args.log.is_file():
        parser.error(f"file not found: {args.log}")
    body = args.log.read_text(encoding="utf-8", errors="replace")
    result = {name: len(pattern.findall(body)) for name, pattern in PATTERNS.items()}
    print(f"Log: {args.log}\n")
    print("Category                 Count")
    print("------------------------  -----")
    for name, count in result.items():
        print(f"{name:24}  {count:5}")
    critical = any(result[k] for k in FATAL)
    print("\nStatus:", "NEEDS REVIEW / REBUILD" if critical else "No detected blocking log patterns")
    print("Note: check actual output PDF and every page; heuristic log parsing is not proof of correctness.")
    return 1 if critical else 0


if __name__ == "__main__":
    raise SystemExit(main())
