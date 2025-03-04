import sys
import os
import unittest
import sqlite3
# Add the root directory to sys.path so Python can locate the 'controllers' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.pharmacy_controller import MedicalRecordController
from database.db_manager import connect_db

class TestMedicalRecordController(unittest.TestCase):

    def setUp(self):
        """Set up an in-memory database for testing"""
        self.db_name = ":memory:"  # In-memory database for testing purposes
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        # Set up necessary tables (if not already created)
        self.cursor.execute('''
            CREATE TABLE medical_records (
                id INTEGER PRIMARY KEY,
                patient_id INTEGER,
                doctor_id INTEGER,
                diagnosis TEXT,
                treatment TEXT,
                notes TEXT
            )
        ''')
        self.conn.commit()

    def tearDown(self):
        """Clean up the database after each test"""
        self.cursor.execute("DROP TABLE medical_records")
        self.conn.commit()
        self.conn.close()

    def test_add_medical_record(self):
        """Test adding a medical record to the database"""
        success = MedicalRecordController.add_medical_record(
            patient_id=1, doctor_id=1, diagnosis="Flu", treatment="Rest & Hydration", notes="Patient should rest for 3 days."
        )

        # After adding, check if the record is in the database
        self.cursor.execute("SELECT COUNT(*) FROM medical_records WHERE diagnosis = 'Flu'")
        count = self.cursor.fetchone()[0]

        # Assert the record was added successfully (count should be 1)
        self.assertEqual(count, 1)
        print("Add Medical Record Test: Passed")

    def test_list_medical_records(self):
        """Test listing medical records from the database"""
        # Add test data to the medical_records table
        self.cursor.execute('''
            INSERT INTO medical_records (patient_id, doctor_id, diagnosis, treatment, notes)
            VALUES (1, 1, 'Flu', 'Rest & Hydration', 'Patient should rest for 3 days.')
        ''')
        self.conn.commit()

        # Call the method to list medical records
        records = MedicalRecordController.get_medical_records(patient_id=1)

        # Check if the returned records match what we inserted
        self.assertGreater(len(records), 0)
        self.assertEqual(records[0]['diagnosis'], 'Flu')
        print("List Medical Records Test: Passed")

    def test_delete_medical_record(self):
        """Test deleting a medical record from the database"""
        # Insert a medical record to be deleted
        self.cursor.execute('''
            INSERT INTO medical_records (patient_id, doctor_id, diagnosis, treatment, notes)
            VALUES (1, 1, 'Flu', 'Rest & Hydration', 'Patient should rest for 3 days.')
        ''')
        self.conn.commit()

        # Get the ID of the inserted record
        self.cursor.execute("SELECT id FROM medical_records WHERE diagnosis = 'Flu'")
        record_id = self.cursor.fetchone()[0]

        # Call the delete method
        success = MedicalRecordController.delete_medical_record(record_id)

        # Assert the deletion was successful (record should not exist now)
        self.cursor.execute("SELECT COUNT(*) FROM medical_records WHERE id = ?", (record_id,))
        count = self.cursor.fetchone()[0]

        self.assertEqual(count, 0)
        print("Delete Medical Record Test: Passed")

if __name__ == "__main__":
    unittest.main()
