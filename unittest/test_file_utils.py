import unittest
from unittest.mock import patch
from io import StringIO
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from file_utils import FileManagement

class TestFileManagement(unittest.TestCase):

    def init_class(self):
        self.username = 'test_user'
        self.foldername = 'test_folder'
        self.file_manager = FileManagement(self.username, self.foldername)

    def test_create_file(self):
        filename = 'test_file.txt'
        description = 'Test_description.'
        self.file_manager.file_path = os.path.join(self.file_manager.created_file_path, filename)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.file_manager.create_file(filename, description)
            output = mock_stdout.getvalue().strip()
            self.assertIn("Create 'test_file' successfully.", output)

    def test_delete_file(self):
        filename = 'test_file.txt'
        # Create the file first
        self.file_manager.file_path = os.path.join(self.file_manager.created_file_path, filename)
        self.file_manager.create_file(filename, 'Test file to delete.')
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.file_manager.delete_file(filename)
            output = mock_stdout.getvalue().strip()
            self.assertIn("Delete 'test_file' successfully.", output)

    def test_rename_file(self):
        filename = 'test_file.txt'
        new_filename = 'renamed_file.txt'
        self.file_manager.file_path = os.path.join(self.file_manager.created_file_path, filename)
        # Create the file first
        self.file_manager.create_file(filename, 'Test file to rename.')
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.file_manager.rename_file(filename, new_filename)
            output = mock_stdout.getvalue().strip()
            self.assertIn("Rename 'test_file' to 'renamed_file' successfully.", output)


if __name__ == '__main__':
    unittest.main()
