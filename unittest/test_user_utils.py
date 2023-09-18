import unittest
from user_utils import UserManagement
from io import StringIO
from unittest.mock import patch

class TestUserManagement(unittest.TestCase):

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