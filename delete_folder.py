#!/usr/bin/env python3
import os
import argparse
from utils import check_format_pack
from user_utils import UserManagement
from folder_utils import FolderManagement

def main():
    parser = argparse.ArgumentParser(description="Virtual File System - Delete a folder")
    parser.add_argument("username", type=str, help="Name of the user")
    parser.add_argument("foldername", type=str, help="Name of the folder to delete")

    args = parser.parse_args()

    # check the format of username & foldername
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
        folder_existence_flag = vfs_folder.check_exists(foldername, False) # not for creating a folder, give False

        if user_existence_flag and folder_existence_flag:
            vfs_folder.folder_path = os.path.join(vfs_folder.created_folder_path, foldername)
            vfs_folder.delete_folder(foldername)

if __name__ == "__main__":
    main()