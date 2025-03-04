import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.nurse_controller import NurseController

class TestNurseController(unittest.TestCase):
    def test_add_nurse(self):
        result = NurseController.add_nurse(
            user_id=1, 
            department="All Wards", 
            supervising_doctor="Admin", 
        )
        self.assertTrue(result, "Failed to add nurse")

    def test_list_nurses(self):
        nurses = NurseController.list_nurses()
        print(nurses)
        self.assertIsInstance(nurses, list, "Nurse should be returned as a list")

    def test_delete_nurse(self):
        result = NurseController.delete_nurse("Admin")
        self.assertTrue(result, "Failed to delete nurse")

if __name__ == "__main__":
    unittest.main()
    print()
