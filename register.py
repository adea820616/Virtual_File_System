#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="Virtual File System - Register")
    parser.add_argument("username", type=str, help="register a user")

    args = parser.parse_args()


if __name__ == "__main__":
    main()