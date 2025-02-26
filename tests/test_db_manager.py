import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from  database.db_manager import connect_db, authenticate_user, hash_password

def test_db_setup():
    conn = connect_db()
    if not conn:
        print("Database connection failed.")
        return
    
    cursor = conn.cursor()
    
    # Check if tables exist
    tables = [
        "users", "doctors", "nurses", "receptionists", "patients",
        "medical_records", "prescriptions", "medications", "appointments",
        "nurse_assignments"
    ]
    
    for table in tables:
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
        result = cursor.fetchone()
        if result:
            print(f"Table '{table}' exists.")
        else:
            print(f"Table '{table}' is missing!")

    # Check if admin account exists
    cursor.execute("SELECT username FROM users WHERE username = 'Admin'")
    admin = cursor.fetchone()
    if admin:
        print("Admin account exists.")
    else:
        print("Admin account is missing!")

    conn.close()

def test_authentication():
    role = authenticate_user("Admin", "7f-Ge&2RS-a0")
    if role:
        print(f"Authentication successful. Role: {role}")
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    print("Testing database setup...")
    test_db_setup()
    
    print("\nTesting authentication...")
    test_authentication()
