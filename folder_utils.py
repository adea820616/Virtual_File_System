import os
import sys


class FolderManagement:
    def __init__(self, username):
        self.folder_path = ''
        self.created_folder = set()
        users_path = os.path.join(os.getcwd(), 'users')
        self.created_folder_path = os.path.join(users_path, username)
        self.load_created_folders()


    def check_created_folder_path(self):
        if not os.path.exists(self.created_folder_path):
            os.mkdir(self.created_folder_path)


    def load_created_folders(self):
        try:
            self.check_created_folder_path()
            self.created_folder = set(os.listdir(self.created_folder_path)) #ann: folder_a, folder_aa
        except FileNotFoundError:
            pass


    def check_exists(self, foldername, to_create):
        if foldername in self.created_folder:
            if to_create:
                print(f"Error: The '{foldername}' has already existed.", file=sys.stderr)
            else:
                print(f"The '{foldername}' exists.")
            return True
        else:
            print(f"The '{foldername}' has not existed.")
            return False


    # create a folder
    def create_folder(self, foldername):
        self.created_folder.add(foldername)
        os.mkdir(self.folder_path)
        print(f"Create '{foldername}' successfully.", file=sys.stdout)
    