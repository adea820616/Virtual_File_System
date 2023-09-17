#!/usr/bin/env python3
import argparse
from utils import check_format_pack

def main():
    parser = argparse.ArgumentParser(description="Virtual File System - Delete a folder")
    parser.add_argument("username", type=str, help="Name of the user")
    parser.add_argument("foldername", type=str, help="Name of the folder to delete")

    args = parser.parse_args()

    # check the format of username & foldername
    name_is_ok = check_format_pack([args.username, args.foldername])
    username = args.username.lower()
    foldername = args.foldername.lower()


if __name__ == "__main__":
    main()