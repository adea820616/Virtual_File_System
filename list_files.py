#!/usr/bin/env python3
import sys
import argparse
from utils import check_format_pack
from user_utils import UserManagement
from folder_utils import FolderManagement
from file_utils import FileManagement


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

        # check if the folder exists or not
        vfs_folder = FolderManagement(username)
        folder_existence_flag = vfs_folder.check_exists(foldername, False) # not for creating, give False

        if user_existence_flag and folder_existence_flag:
            vfs_file = FileManagement(username, foldername)
            file_empty_flag = vfs_file.check_file_empty()
            
            if not file_empty_flag:
                vfs_file.list_file(sort_by, args.order)
            else:
                print(f"Warning: The files is empty!", file=sys.stdout)


if __name__ == "__main__":
    main()