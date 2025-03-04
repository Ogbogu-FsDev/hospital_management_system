import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.db_manager import connect_db  # Ensure db_manager.py exists and connects to the correct DB

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class AppointmentController:
    """Handles appointment scheduling, retrieval, and deletion."""

    @staticmethod
    def add_appointment(patient_id, doctor_id, date, time, reason, status="Scheduled"):
        """Adds a new appointment to the system."""
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO appointments (patient_id, doctor_id, date, time, reason, status)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (patient_id, doctor_id, date, time, reason, status))
            conn.commit()
            logging.info(f"Appointment scheduled for patient {patient_id} with doctor {doctor_id} on {date} at {time}.")
            return True
        except Exception as e:
            logging.error(f"Error scheduling appointment: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def list_appointments():
        """Retrieves all appointments."""
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, patient_id, doctor_id, date, time, reason, status FROM appointments")
            appointments = cursor.fetchall()
            return appointments
        except Exception as e:
            logging.error(f"Error retrieving appointments: {e}")
            return []
        finally:
            conn.close()

    @staticmethod
    def delete_appointment(appointment_id):
        """Deletes an appointment."""
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM appointments WHERE id = ?", (appointment_id,))
            conn.commit()
            logging.info(f"Appointment ID {appointment_id} deleted successfully.")
            return True
        except Exception as e:
            logging.error(f"Error deleting appointment: {e}")
            return False
        finally:
            conn.close()
