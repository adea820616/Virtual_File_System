import os
import sys
from glob import glob
from datetime import datetime
from folder_utils import FolderManagement

class FileManagement:
    def __init__(self, username, foldername):
        self.username = username
        self.foldername = foldername
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
        

    # Define a custom sorting key function
    def sort_lines(self, line):
        elements = line.split(',')

        if self.sort_by == 'name':
            return elements[0]
        else:
            return elements[2]


    def sort_by_list_files(self, lines):
        sort_reverse = False if self.order == 'desc' else True
        
        lines = lines.strip().split('\n')
        # Sort the lines based on the sort_name or sort_time in ascending or descending
        sorted_lines = sorted(lines, key=self.sort_lines, reverse = sort_reverse)

        # Join the sorted lines back into a string
        sorted_data = '\n'.join(sorted_lines).replace(',', '').replace('.txt', '')
        return sorted_data


    # get the filename, description, created_time, foldername, username
    def list_file_str(self):
        list_folder = ''
        for file in self.files_list:
            # filename
            file_path = str(file)
            folder_name = file_path.split('/')[-1]
            list_ = f'{folder_name}, '

            # description & creaetd time
            with open(file_path, 'r') as f:
                content = f.read().splitlines()
                created_time = content[0]
                description = content[1]
                list_ += f'{description}, '
                list_ += f'{created_time}, '
            # foldername
            list_ += f'{self.foldername}, '
            # username
            list_ += f'{self.username}'
            list_folder += list_
            list_folder += '\n'
        return list_folder


    def list_file(self, sort_by, order):
        self.sort_by = sort_by
        self.order = order
        list_file = self.list_file_str()
        list_file = self.sort_by_list_files(list_file)
        
        print(f'{list_file}', file=sys.stdout)
