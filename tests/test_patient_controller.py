import sys
import os
import sqlite3
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.patient_controller import PatientController
from database.db_manager import connect_db

class TestPatientController(unittest.TestCase):
    def test_add_patient(self):
        result = PatientController.add_patient(
            title="Mr", 
            name="Test Admin Test", 
            age=100, 
            gender="Mr.", 
            phone="00000 000000", 
            email="testadmin@example.com", 
            address="123 Admin Street",
            registered_by=1
        )
        self.assertTrue(result, "Failed to add patient")

    def test_list_patients(self):
        patients = PatientController.list_patients()
        print(patients)
        self.assertIsInstance(patients, list, "Patient should be returned as a list")

    def test_delete_patient(self):
        result = PatientController.delete_patient(1)
        self.assertTrue(result, "Failed to delete patient")

if __name__ == "__main__":
    unittest.main()
    print()