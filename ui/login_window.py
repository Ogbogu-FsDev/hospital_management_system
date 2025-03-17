from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6 import QtCore
import sqlite3
from ui.dashboard_window import DashboardWindow
from ui.styles import bubble_style, button_style

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hospital Management System - Login")
        self.setGeometry(500, 250, 400, 250)
        self.setStyleSheet("background-color: #ADD8E6;")  # Light Blue

        self.setMaximumSize(400, 250)  # Set maximum size for the window
        self.setMinimumSize(400, 250)  # Set minimum size for the window

        layout = QVBoxLayout()

        # Add the logo above the window title
        self.logo_label = QLabel(self)
        logo_pixmap = QPixmap("/hospital_management_system/ui/assets/images/HMS-Logo.png")  # Provide the path to your logo image
        scaled_logo = logo_pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)  # Scale the logo to 100x100 pixels
        self.logo_label.setPixmap(scaled_logo)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.logo_label)

        self.label = QLabel("User Login")
        self.label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("color: #333;")
        layout.addWidget(self.label)

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter Username")
        self.username_input.setStyleSheet(bubble_style())
        layout.addWidget(self.username_input)

        # Layout for password field and toggle button
        password_layout = QHBoxLayout()

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(bubble_style())
        self.password_input.returnPressed.connect(self.handle_login)  # Login on "Enter"
        password_layout.addWidget(self.password_input)

        # Show/Hide password toggle button with rounded style and icon
        self.show_password_button = QPushButton(self)
        self.show_password_button.setIcon(QIcon("/hospital_management_system/ui/assets/images/hide-password-icon.png"))  # Initially show the eye icon for password visibility
        self.show_password_button.setIconSize(QtCore.QSize(20, 20))  # Adjust icon size
        self.show_password_button.setStyleSheet("""
            QPushButton {
                background-color: #fff;
                border-radius: 12px;
                padding: 5px;
                border: 2px solid #ADD8E6;
            }
            QPushButton:hover {
                background-color: #ADD8E6;
            }
        """)
        self.show_password_button.clicked.connect(self.toggle_password_visibility)
        password_layout.addWidget(self.show_password_button)

        layout.addLayout(password_layout)

        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet(button_style())
        self.login_button.clicked.connect(self.handle_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def toggle_password_visibility(self):
        # Toggle the echo mode and icon
        if self.password_input.echoMode() == QLineEdit.EchoMode.Password:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.show_password_button.setIcon(QIcon("/hospital_management_system/ui/assets/images/hide-password-icon.png"))  # Change to eye-slash for hide
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.show_password_button.setIcon(QIcon("/hospital_management_system/ui/assets/images/show-password-icon.png"))  # Change to eye for show

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
