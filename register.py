#!/usr/bin/env python3
import argparse
from utils import check_format
from user_utils import UserManagement

def main():
    """
    Main function to register a user in the Virtual File System.
    It takes a username as input and registers it if it meets the required format
    and does not already exist.

    Usage:
        python register_user.py <username>

    Args:
        username (str): The username to register.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Virtual File System - Register")
    parser.add_argument("username", type=str, help="register a user")

    args = parser.parse_args()

    # check the format of username
    username_flag = check_format(args.username)
    username = args.username.lower()

    # check if the user exists or not
    vfs_user = UserManagement()
    user_exists_flag = vfs_user.check_exists(username, True)

    # if the format of username corrects and the username exists -> register it.
    if username_flag and not user_exists_flag:
        vfs_user.register_user(username)


if __name__ == "__main__":
    main()