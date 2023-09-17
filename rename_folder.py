#!/usr/bin/env python3
import argparse
from utils import check_format_pack


def main():
    parser = argparse.ArgumentParser(description="Virtual File System - Rename a folder")
    parser.add_argument("username", type=str, help="Name of the user")
    parser.add_argument("foldername", type=str, help="Name of the folder to rename")
    parser.add_argument("new_folder_name", type=str, help="New name of the folder")

    args = parser.parse_args()

    # check the format of username & foldername & new_foldername
    name_is_ok = check_format_pack([args.username, args.foldername, args.new_folder_name])
    username = args.username.lower()
    foldername = args.foldername.lower()
    new_foldername = args.new_folder_name.lower()


if __name__ == "__main__":
    main()