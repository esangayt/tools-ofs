#!/usr/bin/env python3

import argparse
from pathlib import Path
from base.styles import print_boxed_message, print_boxed_message_custom


class DirectoryStructure:
    def __init__(self, company_name):
        self.company_name = company_name
        self.base_dir = Path(f"{company_name} Company")
        self.structure = {
            "EPT": ["evidence/credentials", "evidence/data", "evidence/screenshots", "logs", "scans", "scope", "tools"],
            "IPT": ["evidence/credentials", "evidence/data", "evidence/screenshots", "logs", "scans", "scope", "tools"]
        }

    def is_new_dir(self):
        if self.base_dir.exists():
            return False
        return True

    def create_directory_structure(self):
        if not self.is_new_dir():
            print(f"Directory {self.base_dir} already exists.")
            return

        for parent, subdirs in self.structure.items():
            print_boxed_message(f"Creating directory structure for {parent}")
            for subdir in subdirs:
                dir_path = self.base_dir / parent / subdir
                dir_path.mkdir(parents=True, exist_ok=True)
                print(f"    Created: {subdir}")


def main():
    parser = argparse.ArgumentParser(description="Create directory structure for a company.")
    parser.add_argument("-a", '--name', type=str, required=True, help="Name of the company")

    args = parser.parse_args()
    ds = DirectoryStructure(args.name)
    ds.create_directory_structure()
    print("Done!")


if __name__ == "__main__":
    main()
