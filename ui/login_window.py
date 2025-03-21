from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6 import QtCore
import sqlite3
from ui.dashboard_window import DashboardWindow
from ui.styles import bubble_style, button_style, toggle_button

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hospital Management System - Login")
        self.setGeometry(500, 250, 400, 300)
        self.setStyleSheet("background-color: #ADD8E6;")  # Light Blue Background

        self.setMaximumSize(400, 300)
        self.setMinimumSize(400, 300)

        layout = QVBoxLayout()

        # Add Logo Above Title
        self.logo_label = QLabel(self)
        logo_pixmap = QPixmap("/hospital_management_system/ui/assets/HMS-Logo.png")
        scaled_logo = logo_pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
        self.logo_label.setPixmap(scaled_logo)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.logo_label)

        # Login Title
        self.label = QLabel("User Login")
        self.label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("color: #333;")
        layout.addWidget(self.label)

        # Username Input
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter Username")
        self.username_input.setStyleSheet(bubble_style())
        layout.addWidget(self.username_input)

        # Password Input & Toggle Button
        password_layout = QHBoxLayout()

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(bubble_style())
        self.password_input.returnPressed.connect(self.handle_login)
        password_layout.addWidget(self.password_input)

        self.show_password_button = QPushButton(self)
        self.show_password_button.setIcon(QIcon("/hospital_management_system/ui/assets/hide-password-icon.png"))
        self.show_password_button.setIconSize(QtCore.QSize(20, 20))
        self.show_password_button.setStyleSheet(toggle_button())
        self.show_password_button.clicked.connect(self.toggle_password_visibility)
        password_layout.addWidget(self.show_password_button)

        layout.addLayout(password_layout)

        # Buttons Layout
        button_layout = QHBoxLayout()

        # Login Button
        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet(button_style())
        self.login_button.clicked.connect(self.handle_login)
        button_layout.addWidget(self.login_button)

        # Forgot Password Button
        self.forgot_password_button = QPushButton("Forgot Password?")
        self.forgot_password_button.setStyleSheet("background-color: #FF4500; color: white; padding: 8px; border-radius: 10px;")
        self.forgot_password_button.clicked.connect(self.handle_forgot_password)
        button_layout.addWidget(self.forgot_password_button)

        # Admin Assistance Button
        self.admin_assist_button = QPushButton("Call Admin Assistance")
        self.admin_assist_button.setStyleSheet("background-color: #FFD700; color: black; padding: 8px; border-radius: 10px;")
        self.admin_assist_button.clicked.connect(self.handle_admin_assistance)
        button_layout.addWidget(self.admin_assist_button)

        layout.addLayout(button_layout)

        # Face Recognition Login Button
        self.face_recog_button = QPushButton("Face Recognition Login")
        self.face_recog_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.face_recog_button.setStyleSheet("background-color: #1E90FF; color: white; padding: 10px; border-radius: 10px; margin-top: 10px;")
        self.face_recog_button.clicked.connect(self.handle_face_recognition)
        layout.addWidget(self.face_recog_button)

        self.setLayout(layout)

    def toggle_password_visibility(self):
        if self.password_input.echoMode() == QLineEdit.EchoMode.Password:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.show_password_button.setIcon(QIcon("/hospital_management_system/ui/assets/hide-password-icon.png"))
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.show_password_button.setIcon(QIcon("/hospital_management_system/ui/assets/show-password-icon.png"))

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if self.authenticate_user(username, password):
            self.open_dashboard(username)
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid username or password!")

    def handle_forgot_password(self):
        QMessageBox.information(self, "Forgot Password", "Contact IT Support to reset your password.")

    def handle_admin_assistance(self):
        QMessageBox.warning(self, "Admin Assistance", "Calling admin for assistance...")

    def handle_face_recognition(self):
        QMessageBox.information(self, "Face Recognition", "Face recognition login triggered!")

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

    def open_dashboard(self, username):
        self.dashboard = DashboardWindow(self.user_role, username)
        self.dashboard.show()
        self.close()
