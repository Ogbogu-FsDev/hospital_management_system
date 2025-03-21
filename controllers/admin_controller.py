import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import logging  # Import the logging module to keep track of admin actions in a log file
from database.db_manager import connect_db, hash_password  # Import database connection and password hashing functions

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AdminController:
    # Adds a new user to the system
    @staticmethod
    def add_user(username, password, role, title, name, date_of_birth, gender, phone, email, address, department, specialization, employment_date, status):
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users (username, password, role, title, name, date_of_birth, gender, phone, email, address, department, specialization, employment_date, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (username, hash_password(password), role, title, name, date_of_birth, gender, phone, email, address, department, specialization, employment_date, status))
            conn.commit()
            logging.info(f"User {username} added successfully.")
            return True
        except Exception as e:
            logging.error(f"Error adding user: {e}")
            return False
        finally:
            conn.close()
    
    # Deletes a user from the system
    @staticmethod
    def delete_user(user_id):
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            logging.info(f"User {user_id} deleted successfully.")
            return True
        except Exception as e:
            logging.error(f"Error deleting user {user_id}: {e}")
            return False
        finally:
            conn.close()

    
    # Retrieves a list of all users in the system
    @staticmethod
    def list_users():
        conn = connect_db()
        if conn is None:
            logging.error("Database connection failed.")
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")  # Get all columns from the users table
            users = cursor.fetchall()
            return users
        except Exception as e:
            logging.error(f"Error retrieving users: {e}")
            return []
        finally:
            conn.close()

    # Retrieves system logs for admin review
    @staticmethod
    def view_logs():
        try:
            with open("/hospital_management_system/logs/database.log", "r") as log_file:
                return log_file.readlines()
        except FileNotFoundError:
            logging.error("Log file not found.")
            return []
