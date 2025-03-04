import sqlite3
import hashlib
import os
import logging
import re

# Sets up logging
log_folder = "D:/hospital_management_system/logs/"
os.makedirs(log_folder, exist_ok=True)
log_file = os.path.join(log_folder, "database.log")
logging.basicConfig(filename=log_file, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Establishes a connection to the SQLite database and returns the connection object
def connect_db():
    try:
        return sqlite3.connect("D:/hospital_management_system/database/hospital.db")
    except sqlite3.Error as e:
        logging.error(f"Database connection error: {e}")
        return None

# Validates password strength
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        return False
    return True

# Hashes a password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest() # type: ignore

# Authenticates a user
def authenticate_user(username, password):
    conn = connect_db()
    if conn is None:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT password, role FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if user and user[0] == hash_password(password):
            logging.info(f"User {username} authenticated successfully.")
            return user[1]  # Return the role of the user if authentication is successful
        logging.warning(f"Failed authentication attempt for user: {username}")
        return None
    except sqlite3.Error as e:
        logging.error(f"Error during authentication: {e}")
        return None
    finally:
        conn.close()

# Creates necessary tables in the database if they do not already exist
def initialize_db():
    conn = connect_db()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        
        # Table for all users
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL,
                title TEXT NOT NULL,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT UNIQUE NOT NULL,
                address TEXT
            )
        ''')
        
        # Insert default admin account
        cursor.execute('''
            INSERT OR IGNORE INTO users (username, password, role, title, name, phone, email, address)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
            ("Admin", hash_password("7f-Ge&2RS-a0"), "admin", "Mr.", "Admin User", "", "admin@example.com", "")
        )
        
        # Table for doctors
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS doctors (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                specialization TEXT NOT NULL,
                years_of_experience INTEGER,
                qualification TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        
        # Table for nurses
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS nurses (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                department TEXT NOT NULL,
                supervising_doctor TEXT,
                status TEXT DEFAULT 'Active',
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(supervising_doctor) REFERENCES doctors(id)
            )
        ''')
        
        # Table for receptionists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS receptionists (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                department TEXT NOT NULL,
                assigned_doctor TEXT,
                status TEXT DEFAULT 'Active',
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(assigned_doctor) REFERENCES doctors(id)
            )
        ''')
        
        # Table for patients
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                name TEXT NOT NULL,
                age INTEGER,
                gender TEXT,
                phone TEXT,
                email TEXT UNIQUE NOT NULL,
                address TEXT,
                registered_by INTEGER,
                FOREIGN KEY(registered_by) REFERENCES receptionists(id)
            )
        ''')
        
        # Table for medical records
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS medical_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                doctor_id INTEGER NOT NULL,
                diagnosis TEXT NOT NULL,
                treatment TEXT NOT NULL,
                date TEXT NOT NULL,
                FOREIGN KEY(patient_id) REFERENCES patients(id),
                FOREIGN KEY(doctor_id) REFERENCES doctors(id)
            )
        ''')
        
        # Table for prescriptions
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prescriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                doctor_id INTEGER NOT NULL,
                medication_id INTEGER NOT NULL,
                dosage TEXT NOT NULL,
                date TEXT NOT NULL,
                FOREIGN KEY(patient_id) REFERENCES patients(id),
                FOREIGN KEY(doctor_id) REFERENCES doctors(id),
                FOREIGN KEY(medication_id) REFERENCES medications(id)
            )
        ''')
        
        # Table for medications
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS medications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                image_path TEXT NOT NULL
            )
        ''')
        
        # Table for appointments
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                doctor_id INTEGER NOT NULL,
                nurse_id INTEGER,
                appointment_date TEXT NOT NULL,
                status TEXT DEFAULT 'Scheduled',
                FOREIGN KEY(patient_id) REFERENCES patients(id),
                FOREIGN KEY(doctor_id) REFERENCES doctors(id),
                FOREIGN KEY(nurse_id) REFERENCES nurses(id)
            )
        ''')
        
        conn.commit()
        logging.info("Database initialized successfully.")
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error initializing database: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    initialize_db()
