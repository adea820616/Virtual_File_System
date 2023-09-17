#!/usr/bin/env python3
import argparse
from utils import check_format_pack


def main():
    parser = argparse.ArgumentParser(description="Virtual File System - Delete a file")
    parser.add_argument("username", type=str, help="Name of the user")
    parser.add_argument("foldername", type=str, help="Name of the folder")
    parser.add_argument("filename", type=str, help="Name of the file to delete")

    args = parser.parse_args()
    # check username & foldername & filename format
    name_is_ok = check_format_pack([args.username, args.foldername, args.filename])
    username = args.username.lower()
    foldername = args.foldername.lower()
    filename = args.filename.lower() + '.txt'


if __name__ == "__main__":
    main()