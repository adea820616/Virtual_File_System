import os
import sys
from glob import glob
from datetime import datetime
from folder_utils import FolderManagement

class FileManagement:
    def __init__(self, username, foldername):
        self.file_path = ''
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
        
    
    # create a file
    def create_file(self, filename, description):
        self.created_file.add(filename)
        with open(self.file_path, "w") as file:
            file.write(str(datetime.today()) + "\n")
            file.write(description + "\n")
        show_filename = filename.split('.txt')[0]
        print(f"Create '{show_filename}' successfully.", file=sys.stdout)


    # delete a file
    def delete_file(self, filename):
        os.remove(self.file_path)
        show_filename = filename.split('.txt')[0]
        print(f"Delete '{show_filename}' successfully.", file=sys.stdout)

    
    # rename a file
    def rename_file(self, filename, new_filename):
        src = self.file_path
        dst = os.path.join(self.created_file_path, new_filename)
        os.rename(src, dst)
        show_filename = filename.split('.txt')[0]
        show_new_filename = new_filename.split('.txt')[0]
        print(f"Rename '{show_filename}' to '{show_new_filename}' successfully.", file=sys.stdout)
    

    # list files
    def check_file_empty(self):
        self.files_list = glob(os.path.join(self.created_file_path, '*'))
        vfs_folder = FolderManagement(self.username)
        d_filename = os.path.join(self.created_file_path, vfs_folder.description_filename)
        self.files_list.remove(d_filename)
        if len(self.files_list) > 0:
            return False
        else:
            return True