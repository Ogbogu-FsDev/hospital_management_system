import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.receptionist_controller import ReceptionistController


class TestReceptionistController(unittest.TestCase):
    def test_add_nurse(self):
        result = ReceptionistController.add_receptionist(
            user_id=1, 
            department="All Wards", 
            assigned_doctor="Admin", 
        )
        self.assertTrue(result, "Failed to add receptionist")

    def test_list_nurses(self):
        receptionists = ReceptionistController.list_receptionists()
        print(receptionists)
        self.assertIsInstance(receptionists, list, "Receptionist should be returned as a list")

    def test_delete_nurse(self):
        result = ReceptionistController.delete_receptionist(1)
        self.assertTrue(result, "Failed to delete receptionist")

if __name__ == "__main__":
    unittest.main()
    print()
