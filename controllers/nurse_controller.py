import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.db_manager import connect_db

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NurseController:
    # Adds a new nurse to the system
    @staticmethod
    def add_nurse(user_id, department, supervising_doctor):
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO nurses (user_id, department, supervising_doctor)
                VALUES (?, ?, ?)""",
                (user_id, department, supervising_doctor))
            conn.commit()
            logging.info(f"Nurse with user ID {user_id} added successfully.")
            return True
        except Exception as e:
            logging.error(f"Error adding nurse: {e}")
            return False
        finally:
            conn.close()
    
    # Retrieves a list of all nurses in the system
    @staticmethod
    def list_nurses():
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, user_id, department, supervising_doctor FROM nurses")
            nurses = cursor.fetchall()
            return nurses
        except Exception as e:
            logging.error(f"Error retrieving nurses: {e}")
            return []
        finally:
            conn.close()
    
    # Deletes a nurse from the system
    @staticmethod
    def delete_nurse(nurse_id):
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM nurses WHERE id = ?", (nurse_id,))
            conn.commit()
            logging.info(f"Nurse with ID {nurse_id} deleted successfully.")
            return True
        except Exception as e:
            logging.error(f"Error deleting nurse: {e}")
            return False
        finally:
            conn.close()
