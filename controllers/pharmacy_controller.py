import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.db_manager import connect_db

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MedicalRecordController:
    # Adds a new medical record for a patient
    @staticmethod
    def add_medical_record(patient_id, doctor_id, diagnosis, treatment, notes):
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO medical_records (patient_id, doctor_id, diagnosis, treatment, notes)
                VALUES (?, ?, ?, ?, ?)""",
                (patient_id, doctor_id, diagnosis, treatment, notes))
            conn.commit()
            logging.info(f"Medical record for patient ID {patient_id} added successfully.")
            return True
        except Exception as e:
            logging.error(f"Error adding medical record: {e}")
            return False
        finally:
            conn.close()

    # Retrieves a patient's medical records
    @staticmethod
    def get_medical_records(patient_id):
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, doctor_id, diagnosis, treatment, notes FROM medical_records WHERE patient_id = ?", (patient_id,))
            records = cursor.fetchall()
            return records
        except Exception as e:
            logging.error(f"Error retrieving medical records: {e}")
            return []
        finally:
            conn.close()
    
    # Deletes a medical record by ID
    @staticmethod
    def delete_medical_record(record_id):
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM medical_records WHERE id = ?", (record_id,))
            conn.commit()
            logging.info(f"Medical record with ID {record_id} deleted successfully.")
            return True
        except Exception as e:
            logging.error(f"Error deleting medical record: {e}")
            return False
        finally:
            conn.close()
