import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.db_manager import connect_db

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BillingController:
    """Handles patient billing operations"""
    
    @staticmethod
    def add_bill(patient_id, amount, status="Pending"):
        """Adds a new bill for a patient"""
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO billing (patient_id, amount, status)
                VALUES (?, ?, ?)
            """, (patient_id, amount, status))
            conn.commit()
            logging.info(f"Bill of ${amount} added for patient ID {patient_id}.")
            return True
        except Exception as e:
            logging.error(f"Error adding bill: {e}")
            return False
        finally:
            conn.close()
    
    @staticmethod
    def list_bills():
        """Retrieves all bills from the system"""
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, patient_id, amount, status FROM billing")
            bills = cursor.fetchall()
            return bills
        except Exception as e:
            logging.error(f"Error retrieving bills: {e}")
            return []
        finally:
            conn.close()
    
    @staticmethod
    def update_bill_status(bill_id, new_status):
        """Updates the status of a bill (e.g., Paid, Pending)"""
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE billing SET status = ? WHERE id = ?", (new_status, bill_id))
            conn.commit()
            logging.info(f"Bill ID {bill_id} updated to {new_status}.")
            return True
        except Exception as e:
            logging.error(f"Error updating bill status: {e}")
            return False
        finally:
            conn.close()
    
    @staticmethod
    def delete_bill(bill_id):
        """Deletes a bill from the system"""
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM billing WHERE id = ?", (bill_id,))
            conn.commit()
            logging.info(f"Bill ID {bill_id} deleted successfully.")
            return True
        except Exception as e:
            logging.error(f"Error deleting bill: {e}")
            return False
        finally:
            conn.close()
