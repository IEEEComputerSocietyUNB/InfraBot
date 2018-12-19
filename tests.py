import unittest
from config import get_config
from bot import check_admin_permission, check_user_permission


class TestConfigRelated(unittest.TestCase):
    def test_get_config(self):
        """
        Check if all goes well when a config file can be found
        """
        self.assertIn("token", get_config(filename="config_example.ini"))

    def test_get_config_no_file(self):
        """
        Check if fails when no config file can be found
        """
        with self.assertRaises(FileNotFoundError):
            get_config(filename="fail.ini")

    def test_check_admin(self):
        """
        Check if admin verification works correctly
        """
        self.assertFalse(check_admin_permission("notadmin", "config_example.ini"))
        self.assertTrue(check_admin_permission("admin1", "config_example.ini"))

    def test_check_user(self):
        """
        Check if user verification works correctly
        """
        self.assertFalse(check_user_permission("notuser", "config_example.ini"))
        self.assertTrue(check_user_permission("user1", "config_example.ini"))

    def test_check_user_on_admin(self):
        """
        Check if user on admin verification works correctly
        """
        self.assertFalse(check_user_permission("notadmin", "config_example.ini"))
        self.assertTrue(check_user_permission("admin1", "config_example.ini"))
