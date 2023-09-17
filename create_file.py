#!/usr/bin/env python3
import argparse
from utils import check_format_pack


def main():
    parser = argparse.ArgumentParser(description="Virtual File System - Create a file")
    parser.add_argument("username", type=str, help="Name of the user")
    parser.add_argument("foldername", type=str, help="Name of the folder")
    parser.add_argument("filename", type=str, help="Name of the file to create")
    parser.add_argument("description", type=str, nargs="?", default='helloworld', help="Description for the file (optional)")

    args = parser.parse_args()

    # check the format of username & foldername & filename
    name_is_ok = check_format_pack([args.username, args.foldername, args.filename])


if __name__ == "__main__":
    main()