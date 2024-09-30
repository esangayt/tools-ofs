#!/usr/bin/env python3

import os
import argparse
from pathlib import Path

from base.styles import print_boxed_message


def create_directory_structure(company_name):
    base_dir = Path(f"{company_name} Company")
    structure = {
        "EPT": ["evidence/credentials", "evidence/data", "evidence/screenshots", "logs", "scans", "scope", "tools"],
        "IPT": ["evidence/credentials", "evidence/data", "evidence/screenshots", "logs", "scans", "scope", "tools"]
    }

    if base_dir.exists():
        print(f"Directory {base_dir} already exists.")
        return

    for parent, subdirs in structure.items():
        print_boxed_message(f"Creating directory structure for {parent}")
        for subdir in subdirs:
            dir_path = base_dir / parent / subdir
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"    Created: {subdir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create directory structure for a company.")
    parser.add_argument("-a", '--name', type=str, required=True, help="Name of the company")

    args = parser.parse_args()
    create_directory_structure(args.name)

    print("Done.")
