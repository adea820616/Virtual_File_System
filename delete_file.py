#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description="Virtual File System - Delete a file")
    parser.add_argument("username", type=str, help="Name of the user")
    parser.add_argument("foldername", type=str, help="Name of the folder")
    parser.add_argument("filename", type=str, help="Name of the file to delete")

    args = parser.parse_args()


if __name__ == "__main__":
    main()