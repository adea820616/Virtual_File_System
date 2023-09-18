import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from user_utils import UserManagement
from io import StringIO
from unittest.mock import patch

class TestUserManagement(unittest.TestCase):
    """
    Unit tests for UserManagement class.
    This test suite covers the following methods of the UserManagement class:
        - check_user_exists
        - check_user_does_not_exist
        - register_user

    Attributes:
        vfs_user (UserManagement): An instance of the UserManagement class for testing purposes.

    Usage:
        python test_user_utils.py
    """
    def init_class(self):
        "initializes a UserManagement instance for each test case."
        self.vfs_user = UserManagement()

    def test_check_user_exists(self):
        "checks the check_exists method when the user exists."
        with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            result = self.vfs_user.check_exists('test_user', False)
            output = mock_stderr.getvalue().strip()
            self.assertTrue(result)
            self.assertIn(output, "The 'test_user' exists.")

    def test_check_user_does_not_exist(self):
        "checks the check_exists method when the user does not exist."
        with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            result = self.vfs_user.check_exists('nonexistent_user', False)
            output = mock_stderr.getvalue().strip()
            self.assertFalse(result)
            self.assertIn(output, "The 'nonexistent_user' has not registered.")

    def test_register_user_success(self):
        "Test the register_user method for successful registration."
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.vfs_user.register_user('new_user')
            output = mock_stdout.getvalue().strip()
            self.assertIn(output, "Add 'new_user' successfully.")

if __name__ == '__main__':
    unittest.main()