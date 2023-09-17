#!/usr/bin/env python3
import argparse
from utils import check_format
from user_utils import UserManagement
from folder_utils import FolderManagement


def main():
    parser = argparse.ArgumentParser(description="Virtual File System - List folders")
    parser.add_argument("username", type=str, help="Name of the user")

    sort_group = parser.add_mutually_exclusive_group(required=True)
    sort_group.add_argument("--sort_name", action="store_true", help="Sort by folder name")
    sort_group.add_argument("--sort_created", action="store_true", help="Sort by folder creation date")
    parser.add_argument("order", choices=["asc", "desc"], default="asc", help="Sort in ascending or descending")

    args = parser.parse_args()
    if args.sort_name:
        sort_by = 'name'
    else:
        sort_by = 'time'

    # check the format of username
    name_is_ok = check_format(args.username)
    username = args.username.lower()

    # if the format of username correct -> check the username exists or not
    if name_is_ok:
        # check if the user exists or not
        vfs_user = UserManagement()
        user_existence_flag = vfs_user.check_exists(username, False) # not for registration, give False

        if user_existence_flag:
            vfs_folder = FolderManagement(username)
            folder_empty_flag = vfs_folder.check_folder_empty()


if __name__ == "__main__":
    main()