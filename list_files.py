#!/usr/bin/env python3
import argparse
from utils import check_format_pack
from user_utils import UserManagement


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

    # check username & foldername format
    name_is_ok = check_format_pack([args.username, args.foldername])
    username = args.username.lower()
    foldername = args.foldername.lower()

    # if the format of username & foldername correct -> check the username and the foldername exists or not
    if name_is_ok:
        # check if the user exists or not
        vfs_user = UserManagement()
        user_existence_flag = vfs_user.check_exists(username, False) # not for registration, give False


if __name__ == "__main__":
    main()