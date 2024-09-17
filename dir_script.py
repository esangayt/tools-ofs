#!/usr/bin/env python3

import os
import argparse

def create_directory_structure(company_name):
    base_dir = f"{company_name} Company"
    structure = {
        "EPT": ["evidence/credentials", "evidence/data", "evidence/screenshots", "logs", "scans", "scope", "tools"],
        "IPT": ["evidence/credentials", "evidence/data", "evidence/screenshots", "logs", "scans", "scope", "tools"]
    }

    if os.path.exists(base_dir):
        print(f"Directory already exists: {base_dir}")
        return

    for parent, subdirs in structure.items():
        for subdir in subdirs:
            dir_path = os.path.join(base_dir, parent, subdir)
            os.makedirs(dir_path, exist_ok=True)
            print(f"Created: {dir_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create directory structure for a company.")
    parser.add_argument('name', type=str, help="Name of the company")

    args = parser.parse_args()
    create_directory_structure(args.name)

    print("Done.")
