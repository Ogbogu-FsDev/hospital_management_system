import unittest
import sqlite3
import sys
import os
# Add the root directory to sys.path so Python can locate the 'controllers' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.appointment_controller import AppointmentController
from database.db_manager import connect_db

class TestAppointmentController(unittest.TestCase):

    def setUp(self):
        """Set up an in-memory database for testing"""
        self.db_name = ":memory:"  # In-memory database for testing purposes
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        # Set up the appointments table (if not already created)
        self.cursor.execute('''
            CREATE TABLE appointments (
                id INTEGER PRIMARY KEY,
                patient_id INTEGER,
                doctor_id INTEGER,
                date TEXT,
                time TEXT,
                reason TEXT
            )
        ''')
        self.conn.commit()

    def tearDown(self):
        """Clean up the database after each test"""
        self.cursor.execute("DROP TABLE appointments")
        self.conn.commit()
        self.conn.close()

    def test_add_appointment(self):
        """Test adding a new appointment to the database"""
        success = AppointmentController.add_appointment(
            patient_id=1, doctor_id=1, date="2025-03-01", time="10:00 AM", reason="Routine Checkup"
        )

        # After adding, check if the appointment is in the database
        self.cursor.execute("SELECT COUNT(*) FROM appointments WHERE reason = 'Routine Checkup'")
        count = self.cursor.fetchone()[0]

        # Assert the appointment was added successfully (count should be 1)
        self.assertEqual(count, 1)
        print("Add Appointment Test: Passed")

    def test_list_appointments(self):
        """Test retrieving appointments from the database"""
        # Add a test appointment to the appointments table
        self.cursor.execute('''
            INSERT INTO appointments (patient_id, doctor_id, date, time, reason)
            VALUES (1, 1, '2025-03-01', '10:00 AM', 'Routine Checkup')
        ''')
        self.conn.commit()

        # Call the method to list appointments
        appointments = AppointmentController.list_appointments()

        # Assert that appointments are returned and match the inserted data
        self.assertGreater(len(appointments), 0)
        self.assertEqual(appointments[0]['reason'], 'Routine Checkup')
        print("List Appointments Test: Passed")

    def test_delete_appointment(self):
        """Test deleting an appointment from the database"""
        # Insert a test appointment
        self.cursor.execute('''
            INSERT INTO appointments (patient_id, doctor_id, date, time, reason)
            VALUES (1, 1, '2025-03-01', '10:00 AM', 'Routine Checkup')
        ''')
        self.conn.commit()

        # Get the ID of the inserted appointment
        self.cursor.execute("SELECT id FROM appointments WHERE reason = 'Routine Checkup'")
        appointment_id = self.cursor.fetchone()[0]

        # Call the delete method
        success = AppointmentController.delete_appointment(appointment_id)

        # Assert the appointment was deleted (it should no longer exist)
        self.cursor.execute("SELECT COUNT(*) FROM appointments WHERE id = ?", (appointment_id,))
        count = self.cursor.fetchone()[0]

        self.assertEqual(count, 0)
        print("Delete Appointment Test: Passed")


if __name__ == "__main__":
    unittest.main()
