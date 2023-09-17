#!/usr/bin/env python3
import os
import argparse
from utils import check_format_pack
from user_utils import UserManagement
from folder_utils import FolderManagement


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

    # if the format of username & foldername correct -> check the username and the foldername exists or not
    if name_is_ok:
        # check if the user exists or not
        vfs_user = UserManagement()
        user_existence_flag = vfs_user.check_exists(username, False) # not for registration, give False

        # check if the folder exists or not
        vfs_folder = FolderManagement(username)
        folder_existence_flag = vfs_folder.check_exists(foldername, False) # not for creating a folder, give False
        # the new folder name must not exist
        new_folder_existence_flag = vfs_folder.check_exists(new_foldername, True)

        if user_existence_flag and folder_existence_flag and not new_folder_existence_flag:
            vfs_folder.folder_path = os.path.join(vfs_folder.created_folder_path, foldername)
            vfs_folder.rename_folder(foldername, new_foldername)


if __name__ == "__main__":
    main()