import os
import sys


class FileManagement:
    def __init__(self, username, foldername):
        self.created_file = set()
        users_path = os.path.join(os.getcwd(), 'users')
        folder_path = os.path.join(users_path, username)
        self.created_file_path = os.path.join(folder_path, foldername)
        self.load_created_files()


    def check_created_file_path(self):
        if not os.path.exists(self.created_file_path):
            os.mkdir(self.created_file_path)


    def load_created_files(self):
        self.check_created_file_path()
        self.created_file = set(os.listdir(self.created_file_path))


    def check_exists(self, filename, to_create):
        if filename in self.created_file:
            if to_create:
                print(f"Error: The '{filename}' has already existed.", file=sys.stderr)
            else:
                print(f"The '{filename}' exists.")
            return True
        else:
            print(f"The '{filename}' has not existed.")
            return False
