import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.doctor_controller import DoctorController

class TestDoctorController(unittest.TestCase):
    def test_add_doctor(self):
        result = DoctorController.add_doctor(
            user_id=1, 
            specialization="Cardiology", 
            years_of_experience=10, 
            qualification="MD"
        )
        self.assertTrue(result, "Failed to add doctor")

    def test_list_doctors(self):
        doctors = DoctorController.list_doctors()
        self.assertIsInstance(doctors, list, "Doctors should be returned as a list")

    def test_delete_doctor(self):
        result = DoctorController.delete_doctor(1)
        self.assertTrue(result, "Failed to delete doctor")

if __name__ == "__main__":
    unittest.main()
