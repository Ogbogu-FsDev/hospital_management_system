import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.db_manager import connect_db, authenticate_user

class TestDatabaseSetup(unittest.TestCase):
    def setUp(self):
        """Set up a test database connection before each test."""
        self.conn = connect_db()
        self.cursor = self.conn.cursor() # type: ignore

    def tearDown(self):
        """Close the database connection after each test."""
        self.conn.close() # type: ignore

    def test_db_connection(self):
        """Test if the database connection is established."""
        self.assertIsNotNone(self.conn, "Failed to connect to the database")

    def test_table_existence(self):
        """Check if the required tables exist in the database."""
        tables = [
            "users", "doctors", "nurses", "receptionists", "patients",
            "medical_records", "prescriptions", "medications", "appointments",
            "nurse_assignments"
        ]
        for table in tables:
            self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,))
            result = self.cursor.fetchone()
            self.assertIsNotNone(result, f"Table '{table}' is missing!")

    def test_admin_account(self):
        """Verify if an admin account exists in the database."""
        self.cursor.execute("SELECT username FROM users WHERE username = 'Admin'")
        admin = self.cursor.fetchone()
        self.assertIsNotNone(admin, "Admin account is missing!")

    def test_authentication(self):
        """Test the authentication function."""
        # Test with a correct username & password
        role = authenticate_user("Admin", "7f-Ge&2RS-a0")  # Ensure this password matches the test DB
        self.assertIsNotNone(role, "Authentication failed for valid credentials")

        # Test with incorrect credentials
        role = authenticate_user("Admin", "wrong_password")
        self.assertIsNone(role, "Authentication should fail for incorrect credentials")

if __name__ == '__main__':
    unittest.main()
