#!/usr/bin/env python3
import os
import argparse
from utils import check_format_pack
from user_utils import UserManagement
from folder_utils import FolderManagement
from file_utils import FileManagement


def main():
    parser = argparse.ArgumentParser(description="Virtual File System - Create a file")
    parser.add_argument("username", type=str, help="Name of the user")
    parser.add_argument("foldername", type=str, help="Name of the folder")
    parser.add_argument("filename", type=str, help="Name of the file to create")
    parser.add_argument("description", type=str, nargs="?", default='helloworld', help="Description for the file (optional)")

    args = parser.parse_args()

    # check the format of username & foldername & filename
    name_is_ok = check_format_pack([args.username, args.foldername, args.filename])
    username = args.username.lower()
    foldername = args.foldername.lower()
    filename = args.filename.lower() + '.txt'

    # if the format of username & foldername correct -> check the username and the foldername exists or not
    if name_is_ok:
        # check if the user exists or not
        vfs_user = UserManagement()
        user_existence_flag = vfs_user.check_exists(username, False) # not for registration, give False

        # check if the folder exists or not
        vfs_folder = FolderManagement(username)
        folder_existence_flag = vfs_folder.check_exists(foldername, False) # not for creating, give False

        # check if the file exists or not
        vfs_file = FileManagement(username, foldername)
        file_existence_flag = vfs_file.check_exists(filename, True) # check file not exists -> to create the file

        if user_existence_flag and folder_existence_flag and not file_existence_flag:
            vfs_file.file_path = os.path.join(vfs_file.created_file_path, filename)
            vfs_file.create_file(filename, args.description)


if __name__ == "__main__":
    main()