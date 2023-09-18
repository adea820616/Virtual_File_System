import unittest
from unittest.mock import patch
from io import StringIO
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from file_utils import FileManagement

class TestFileManagement(unittest.TestCase):
    """
    Unit tests for FileManagement class.
    This test suite covers the following methods of the FileManagement class:
        - create_file
        - delete_file
        - rename_file
        - list_file
    Attributes:
        username (str): The username for testing purposes.
        file_manager (FileManagement): An instance of the FileManagement class for testing purposes.
    Usage:
        python test_file_utils.py
    """

    def test_create_file(self):
        "Test the create_file method."
        username = 'test_user'
        foldername = 'test_folder'
        filename = 'test_file.txt'
        description = 'Test_description.'
        self.file_manager = FileManagement(username, foldername)
        self.file_manager.file_path = os.path.join(self.file_manager.created_file_path, filename)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.file_manager.create_file(filename, description)
            output = mock_stdout.getvalue().strip()
            self.assertIn("Create 'test_file' successfully.", output)

    def test_delete_file(self):
        "Test the delete_file method."
        username = 'test_user'
        foldername = 'test_folder'
        filename = 'test_file.txt'
        self.file_manager = FileManagement(username, foldername)
        # Create the file first
        self.file_manager.file_path = os.path.join(self.file_manager.created_file_path, filename)
        self.file_manager.create_file(filename, 'Test file to delete.')
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.file_manager.delete_file(filename)
            output = mock_stdout.getvalue().strip()
            self.assertIn("Delete 'test_file' successfully.", output)

    def test_rename_file(self):
        "Test the rename_file method."
        username = 'test_user'
        foldername = 'test_folder'
        filename = 'test_file.txt'
        new_filename = 'renamed_file.txt'
        self.file_manager = FileManagement(username, foldername)
        self.file_manager.file_path = os.path.join(self.file_manager.created_file_path, filename)
        # Create the file first
        self.file_manager.create_file(filename, 'Test file to rename.')
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.file_manager.rename_file(filename, new_filename)
            output = mock_stdout.getvalue().strip()
            self.assertIn("Rename 'test_file' to 'renamed_file' successfully.", output)

    def test_list_folder(self):
        "Test the list_file method."
        from glob import glob
        username = 'test_list_folder'
        foldername = 'folder1'
        self.file_manager = FileManagement(username, foldername)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.file_manager.files_list = glob(os.path.join(self.file_manager.created_file_path, '*'))
            self.file_manager.list_file(sort_by='name', order='asc')
            output = mock_stdout.getvalue().strip()
            print('output:', output)
            self.assertIn("test_file1 Test_description. 2023-09-18 16:05:52.196494 folder1 test_list_folder", output)
            self.assertIn("test_file2 Test_description. 2023-09-18 16:06:15.236384 folder1 test_list_folder", output)


if __name__ == '__main__':
    unittest.main()
