#!/usr/bin/env python3
import argparse
from utils import check_format
from user_utils import UserManagement

def main():
    parser = argparse.ArgumentParser(description="Virtual File System - Register")
    parser.add_argument("username", type=str, help="register a user")

    args = parser.parse_args()

    # check the format of username
    username_flag = check_format(args.username)
    username = args.username.lower()

    # check if the user exists or not
    vfs_user = UserManagement()
    user_exists_flag = vfs_user.check_exists(username, True)


if __name__ == "__main__":
    main()