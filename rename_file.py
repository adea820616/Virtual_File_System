#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description="Virtual File System - Rename a file")
    parser.add_argument("username", type=str, help="Name of the user")
    parser.add_argument("foldername", type=str, help="Name of the folder")
    parser.add_argument("filename", type=str, help="Name of the file to rename")
    parser.add_argument("new_file_name", type=str, help="New name of the file")


if __name__ == "__main__":
    main()