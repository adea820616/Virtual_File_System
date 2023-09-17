#!/usr/bin/env python3
import argparse
from utils import check_format

def main():
    parser = argparse.ArgumentParser(description="Virtual File System - Register")
    parser.add_argument("username", type=str, help="register a user")

    args = parser.parse_args()

    # check the format of username
    username_flag = check_format(args.username)


if __name__ == "__main__":
    main()