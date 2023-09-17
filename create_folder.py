import argparse
from utils import check_format_pack


def main():
    parser = argparse.ArgumentParser(description="Virtual File System - Create a folder")
    parser.add_argument("username", type=str, help="Name of the user")
    parser.add_argument("foldername", type=str, help="Name of the folder to create")
    parser.add_argument("description", type=str, nargs="?", default='helloworld', help="Description for the folder (optional)")

    args = parser.parse_args()

    # check the format of username & foldername
    name_is_ok = check_format_pack([args.username, args.foldername])


if __name__ == "__main__":
    main()