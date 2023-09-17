#!/usr/bin/env python3
import argparse
from utils import check_format_pack
from user_utils import UserManagement
from folder_utils import FolderManagement
from file_utils import FileManagement


def main():
    parser = argparse.ArgumentParser(description="Virtual File System - Rename a file")
    parser.add_argument("username", type=str, help="Name of the user")
    parser.add_argument("foldername", type=str, help="Name of the folder")
    parser.add_argument("filename", type=str, help="Name of the file to rename")
    parser.add_argument("new_file_name", type=str, help="New name of the file")

    args = parser.parse_args()
    # check username & foldername & filename format
    name_is_ok = check_format_pack([args.username, args.foldername, args.filename, args.new_file_name])
    username = args.username.lower()
    foldername = args.foldername.lower()
    filename = args.filename.lower() + '.txt'
    new_filename = args.new_file_name.lower() + '.txt'

    # if the format of username & foldername & filename correct -> check the username, foldername, filename exists or not
    if name_is_ok:
        vfs_user = UserManagement()
        user_existence_flag = vfs_user.check_exists(username, False) # check user exists

        # check if the folder exists or not
        vfs_folder = FolderManagement(username)
        folder_existence_flag = vfs_folder.check_exists(foldername, False) # not for creating, give False

        vfs_file = FileManagement(username, foldername)
        file_existence_flag = vfs_file.check_exists(filename, False) # not for creating, give False


if __name__ == "__main__":
    main()