import os
import sys
from glob import glob
from datetime import datetime


class FolderManagement:
    def __init__(self, username):
        self.folder_path = ''
        self.created_folder = set()
        users_path = os.path.join(os.getcwd(), 'users')
        self.created_folder_path = os.path.join(users_path, username)
        self.load_created_folders()
        self.description_filename = 'description.txt'


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


    def create_description(self, description):
        self.description_path = os.path.join(self.folder_path, self.description_filename)
        with open(self.description_path, "w") as file:
            file.write(str(datetime.today()) + "\n")
            file.write(description + "\n")


    # delete a folder
    def delete_files_byfolder(self):
        files_list = glob(os.path.join(self.folder_path, '*'))
        for file in files_list:
            # the description.txt is also deleted
            os.remove(file)


    def delete_folder(self, foldername):
        self.delete_files_byfolder()
        os.rmdir(self.folder_path)
        print(f"Delete '{foldername}' successfully.", file=sys.stdout)
    

    # rename a folder
    def rename_folder(self, foldername, new_foldername):
        src = self.folder_path
        dst = os.path.join(self.created_folder_path, new_foldername)
        os.rename(src, dst)
        print(f"Rename '{foldername}' to '{new_foldername}' successfully.", file=sys.stdout)

    
    # list folders
    def check_folder_empty(self):
        self.files_list = glob(os.path.join(self.created_folder_path, '*'))
        if len(self.files_list) > 0:
            return False
        else:
            return True