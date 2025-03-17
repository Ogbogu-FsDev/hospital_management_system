import sqlite3

class UIDatabaseManager:
    def __init__(self, db_path="hospital_management_system/database/hospital.db"):
        self.db_path = db_path

    def connect(self):
        """Establish a database connection."""
        return sqlite3.connect(self.db_path)

    def get_user_details(self, user_id):
        """Fetch user details for UI display."""
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT title, name, role, phone, email, address FROM users WHERE id = ?", (user_id,))
            user = cursor.fetchone()
            conn.close()
            return user if user else ("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")
        except Exception as e:
            return "Error", "Error", "Error", "Error", "Error", str(e)

    def get_dashboard_stats(self):
        """Fetch patient and appointment counts for the dashboard."""
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM patients")
            patient_count = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM appointments")
            appointment_count = cursor.fetchone()[0]

            conn.close()
            return {"patients": patient_count, "appointments": appointment_count}
        except Exception as e:
            return {"error": str(e)}
