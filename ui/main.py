import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox, QHBoxLayout, QFrame, QGridLayout
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hospital Management System - Login")
        self.setGeometry(500, 250, 400, 250)

        # Set Background Color
        self.setStyleSheet("background-color: #ADD8E6;")  # Light Blue

        layout = QVBoxLayout()

        # Title Label
        self.label = QLabel("User Login")
        self.label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("color: #333;")  # Dark text
        layout.addWidget(self.label)

        # Username Input
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter Username")
        self.username_input.setStyleSheet(self.bubble_style())
        layout.addWidget(self.username_input)

        # Password Input
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)  # Hide password
        self.password_input.setStyleSheet(self.bubble_style())

        # Trigger login on "Enter" press
        self.password_input.returnPressed.connect(self.handle_login)

        layout.addWidget(self.password_input)

        # Login Button
        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet(self.button_style())
        self.login_button.clicked.connect(self.handle_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def bubble_style(self):
        """Style for input fields (bubble theme)."""
        return """
            QLineEdit {
                background-color: white;
                border-radius: 15px;
                padding: 8px;
                border: 2px solid #87CEEB;
                font-size: 14px;
            }
        """

    def button_style(self):
        """Style for buttons (bubble theme)."""
        return """
            QPushButton {
                background-color: #00BFFF;
                color: white;
                border-radius: 15px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1E90FF;
            }
        """

    def handle_login(self):
        """Authenticate user and open dashboard if successful."""
        username = self.username_input.text()
        password = self.password_input.text()

        if self.authenticate_user(username, password):
            self.open_dashboard()
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid username or password!")

    def authenticate_user(self, username, password):
        """Check user credentials from the database."""
        try:
            conn = sqlite3.connect("D:/hospital_management_system/database/hospital.db")
            cursor = conn.cursor()
            cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
            result = cursor.fetchone()
            conn.close()

            if result:
                self.user_role = result[0]
                return True
            else:
                return False
        except sqlite3.Error as e:
            print("Database Error:", e)
            return False

    def open_dashboard(self):
        """Close login and open the main dashboard."""
        self.dashboard = DashboardWindow(self.user_role)
        self.dashboard.show()
        self.close()  # Close the login window


class DashboardWindow(QMainWindow):
    def __init__(self, user_role):
        super().__init__()
        self.setWindowTitle("Hospital Management Dashboard")

        # Open the window in fullscreen mode
        self.showFullScreen()  # This will open the window in fullscreen mode

        # Set Background Color
        self.setStyleSheet("background-color: #ADD8E6;")  # Light Blue

        self.user_role = user_role

        # Create main layout
        main_layout = QHBoxLayout()

        # Sidebar (Left)
        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(220)
        self.sidebar.setStyleSheet("background-color: #1E90FF; border-radius: 100px;")

        sidebar_layout = QVBoxLayout()
        sidebar_layout.setSpacing(20)  # Add spacing for clean layout

        # Sidebar Title (Menu Label inside Sidebar)
        sidebar_title = QLabel("MENU")
        sidebar_title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        sidebar_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sidebar_title.setStyleSheet("color: white; padding: 10px; margin-top: 50px;")  # Adjust margin-top as needed
        sidebar_layout.addWidget(sidebar_title)

        # Buttons for each menu item
        self.buttons = {
            "Home": self.home,
            "Personal Details": self.personal_details,
            "Patient Records": self.patient_records,
            "Appointments": self.appointments,
            "Billing": self.billing,
            "Reports": self.reports,
            "Inventory": self.inventory,
            "Staff Board": self.staff_board
        }

        # Add buttons to the sidebar layout
        for text, func in self.buttons.items():
            button = QPushButton(text)
            button.setStyleSheet(self.button_style())
            button.clicked.connect(func)
            sidebar_layout.addWidget(button)

        # Logout Button
        self.logout_button = QPushButton("Logout")
        self.logout_button.setStyleSheet(self.button_style())
        self.logout_button.clicked.connect(self.logout)
        sidebar_layout.addWidget(self.logout_button)

        sidebar_layout.setContentsMargins(10, 10, 10, 10)  # Adjust margins if necessary
        self.sidebar.setLayout(sidebar_layout)
        main_layout.addWidget(self.sidebar)

        # Main Content Area
        self.content_layout = QVBoxLayout()

        # Container for Content Layout
        container = QWidget()
        container.setLayout(self.content_layout)

        main_layout.addWidget(container)

        # Set Central Widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Initially show the home content
        self.show_welcome_content()

    def button_style(self):
        """Style for sidebar buttons."""
        return """
            QPushButton {
                background-color: white;
                color: #1E90FF;
                border-radius: 10px;
                padding: 12px;
                font-size: 16px;
                font-weight: bold;
                margin: 20px;
            }
            QPushButton:hover {
                background-color: #87CEFA;
            }
        """

    def show_welcome_content(self):
        """Create and display the Home content frame."""
        self.create_new_frame("Welcome to the Hospital Management System\nLogged in as: " + self.user_role)

    def create_new_frame(self, text):
        """Create a new frame with the given text and add it to the content layout."""
        if hasattr(self, 'current_frame'):
            self.current_frame.deleteLater()

        # Create a new frame
        self.current_frame = QFrame(self)
        self.current_frame.setStyleSheet("background-color: white; border-radius: 15px; padding: 10px;")
        frame_layout = QVBoxLayout(self.current_frame)

        # Create a label for the frame
        label = QLabel(text)
        label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: #333;")
        frame_layout.addWidget(label)

        # Add the new frame to the content layout
        self.content_layout.addWidget(self.current_frame)

    def home(self):
        """Handle Home button press."""
        self.create_new_frame("Home content goes here.")

    def personal_details(self):
        """Handle Personal Details button press."""
        self.create_new_frame("Personal Details content goes here.")

    def patient_records(self):
        """Handle Patient Records button press."""
        self.create_new_frame("Patient Records content goes here.")

    def appointments(self):
        """Handle Appointments button press."""
        self.create_new_frame("Appointments content goes here.")

    def billing(self):
        """Handle Billing button press."""
        self.create_new_frame("Billing content goes here.")

    def reports(self):
        """Handle Reports button press."""
        self.create_new_frame("Reports content goes here.")

    def inventory(self):
        """Handle Inventory button press."""
        self.create_new_frame("Inventory content goes here.")

    def staff_board(self):
        """Handle Staff Board button press."""
        self.create_new_frame("Staff Board content goes here.")

    def logout(self):
        """Close dashboard and return to login screen."""
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec())
