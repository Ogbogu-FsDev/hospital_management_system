import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.db_manager import connect_db

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReceptionistController:
    # Adds a new receptionist to the system
    @staticmethod
    def add_receptionist(user_id, department, assigned_doctor):
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute(""" 
                INSERT INTO receptionists (user_id, department, assigned_doctor) 
                VALUES (?, ?, ?)""", 
                (user_id, department, assigned_doctor))
            conn.commit()
            logging.info(f"Receptionist with user ID {user_id} added successfully.")
            return True
        except Exception as e:
            logging.error(f"Error adding receptionist: {e}")
            return False
        finally:
            conn.close()

    # Retrieves a list of all receptionists in the system
    @staticmethod
    def list_receptionists():
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, user_id, department, assigned_doctor FROM receptionists")
            receptionists = cursor.fetchall()
            return receptionists
        except Exception as e:
            logging.error(f"Error retrieving receptionists: {e}")
            return []
        finally:
            conn.close()

    # Deletes a receptionist from the system
    @staticmethod
    def delete_receptionist(receptionist_id):
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM receptionists WHERE id = ?", (receptionist_id,))
            conn.commit()
            logging.info(f"Receptionist with ID {receptionist_id} deleted successfully.")
            return True
        except Exception as e:
            logging.error(f"Error deleting receptionist: {e}")
            return False
        finally:
            conn.close()
