import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.db_manager import connect_db  

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class PatientController:
    """Handles operations related to patients."""

    @staticmethod
    def add_patient(title, name, age, gender, phone, email, address, registered_by):
        """Adds a new patient to the system."""
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO patients (title, name, age, gender, phone, email, address, registered_by)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (title, name, age, gender, phone, email, address, registered_by))
            conn.commit()
            logging.info(f"Patient {name} added successfully.")
            return True
        except Exception as e:
            logging.error(f"Error adding patient: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def list_patients():
        """Retrieves a list of all patients in the system."""
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, name, age, gender, phone, email, address FROM patients")
            patients = cursor.fetchall()
            return patients
        except Exception as e:
            logging.error(f"Error retrieving patients: {e}")
            return []
        finally:
            conn.close()

    @staticmethod
    def delete_patient(patient_id):
        """Deletes a patient from the system."""
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM patients WHERE id = ?", (patient_id,))
            conn.commit()
            if cursor.rowcount == 0:
                logging.warning(f"No patient found with ID {patient_id}.")
                return False
            logging.info(f"Patient with ID {patient_id} deleted successfully.")
            return True
        except Exception as e:
            logging.error(f"Error deleting patient: {e}")
            return False
        finally:
            conn.close()


if __name__ == "__main__":
    # Test the Patient Controller with sample data
    print("Adding a new patient...")
    PatientController.add_patient("Mr.", "John Doe", 30, "Male", "123-456-7890", "john.doe@example.com", "123 Main St", 1)

    print("\nRetrieving list of patients...")
    patients = PatientController.list_patients()
    for patient in patients:
        print(patient)

    print("\nDeleting patient with ID 1...")
    PatientController.delete_patient(1)
