import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.db_manager import connect_db, hash_password, authenticate_user

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DoctorController:
    # Adds a new doctor to the system
    @staticmethod
    def add_doctor(user_id, specialization, years_of_experience, qualification):
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO doctors (user_id, specialization, years_of_experience, qualification)
                VALUES (?, ?, ?, ?)""",
                (user_id, specialization, years_of_experience, qualification))
            conn.commit()
            logging.info(f"Doctor with user ID {user_id} added successfully.")
            return True
        except Exception as e:
            logging.error(f"Error adding doctor: {e}")
            return False
        finally:
            conn.close()
    
    # Retrieves a list of all doctors in the system
    @staticmethod
    def list_doctors():
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, user_id, specialization, years_of_experience, qualification FROM doctors")
            doctors = cursor.fetchall()
            return doctors
        except Exception as e:
            logging.error(f"Error retrieving doctors: {e}")
            return []
        finally:
            conn.close()
    
    # Deletes a doctor from the system
    @staticmethod
    def delete_doctor(doctor_id):
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM doctors WHERE id = ?", (doctor_id,))
            conn.commit()
            logging.info(f"Doctor with ID {doctor_id} deleted successfully.")
            return True
        except Exception as e:
            logging.error(f"Error deleting doctor: {e}")
            return False
        finally:
            conn.close()
