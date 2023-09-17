#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description="Virtual File System - List files")

    parser.add_argument("username", type=str, help="Name of the user")
    parser.add_argument("foldername", type=str, help="Name of the folder")

    sort_group = parser.add_mutually_exclusive_group(required=True)
    sort_group.add_argument("--sort_name", action="store_true", help="Sort by file name")
    sort_group.add_argument("--sort_created", action="store_true", help="Sort by file creation date")
    parser.add_argument("order", choices=["asc", "desc"], default="asc", help="Sort in ascending or descending")

    args = parser.parse_args()
    if args.sort_name:
        sort_by = 'name'
    else:
        sort_by = 'time'


if __name__ == "__main__":
    main()