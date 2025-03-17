from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sqlite3
from ui.dashboard_window import DashboardWindow
from ui.styles import bubble_style, button_style

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hospital Management System - Login")
        self.setGeometry(500, 250, 400, 250)
        self.setStyleSheet("background-color: #ADD8E6;")  # Light Blue

        layout = QVBoxLayout()

        self.label = QLabel("User Login")
        self.label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("color: #333;")
        layout.addWidget(self.label)

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter Username")
        self.username_input.setStyleSheet(bubble_style())
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(bubble_style())
        self.password_input.returnPressed.connect(self.handle_login)  # Login on "Enter"
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet(button_style())
        self.login_button.clicked.connect(self.handle_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if self.authenticate_user(username, password):
            self.open_dashboard()
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid username or password!")

    def authenticate_user(self, username, password):
        try:
            conn = sqlite3.connect("/hospital_management_system/database/hospital.db")
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
        self.dashboard = DashboardWindow(self.user_role)
        self.dashboard.show()
        self.close()
