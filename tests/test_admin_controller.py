import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.admin_controller import AdminController

class TestAdminController(unittest.TestCase):
    def test_add_user(self):
        result = AdminController.add_user(
            username="testadmin", 
            password="Test@1234", 
            role="admin", 
            title="Mr.", 
            name="Test Admin", 
            phone="1234567890", 
            email="testadmin@example.com", 
            address="123 Admin Street"
        )
        self.assertTrue(result, "Failed to add user")

    def test_list_users(self):
        users = AdminController.list_users()
        self.assertIsInstance(users, list, "Users should be returned as a list")

    def test_delete_user(self):
        result = AdminController.delete_user("testadmin")
        self.assertTrue(result, "Failed to delete user")

if __name__ == "__main__":
    unittest.main()
    print()
