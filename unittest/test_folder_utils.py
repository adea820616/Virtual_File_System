import unittest
from unittest.mock import patch
from io import StringIO
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from folder_utils import FolderManagement

class TestFolderManagement(unittest.TestCase):
    """
    Unit tests for FolderManagement class.
    This test suite covers the following methods of the FolderManagement class:
        - create_folder
        - delete_folder
        - rename_folder
        - list_folder
    Attributes:
        username (str): The username for testing purposes.
        folder_manager (FolderManagement): An instance of the FolderManagement class for testing purposes.
    Usage:
        python test_folder_utils.py
    """

    def setUp(self):
        "initializes a FolderManagement instance for each test case."
        self.username = 'test_user'
        self.folder_manager = FolderManagement(self.username)

    def test_create_folder(self):
        "Test the create_folder method."
        foldername = 'test_create_folder'
        self.folder_manager.folder_path = os.path.join('./users/test_user', foldername)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.folder_manager.create_folder(foldername)
            output = mock_stdout.getvalue().strip()
            self.assertIn(f"Create '{foldername}' successfully.", output)

    def test_delete_folder(self):
        "Test the delete_folder method."
        foldername = 'test_delete_folder'
        self.folder_manager.folder_path = os.path.join('./users/test_user', foldername)
        # Create the folder first
        self.folder_manager.create_folder(foldername)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.folder_manager.delete_folder(foldername)
            output = mock_stdout.getvalue().strip()
            self.assertIn(f"Delete '{foldername}' successfully.", output)

    def test_rename_folder(self):
        "Test the rename_folder method."
        foldername = 'test_rename_folder'
        new_foldername = 'renamed_folder'
        self.folder_manager.folder_path = os.path.join('./users/test_user', foldername)
        # Create the folder first
        self.folder_manager.create_folder(foldername)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.folder_manager.rename_folder(foldername, new_foldername)
            output = mock_stdout.getvalue().strip()
            self.assertIn(f"Rename '{foldername}' to '{new_foldername}' successfully.", output)

    def test_list_folder(self):
        "Test the list_folder method."
        from glob import glob
        username = 'test_list_folder'
        self.folder_manager = FolderManagement(username)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.folder_manager.files_list = glob(os.path.join(self.folder_manager.created_folder_path, '*'))
            self.folder_manager.list_folder(sort_by='name', order='asc')
            output = mock_stdout.getvalue().strip()
            self.assertIn("folder1", output)
            self.assertIn("folder2", output)
            self.assertIn("folder3", output)

if __name__ == '__main__':
    unittest.main()
