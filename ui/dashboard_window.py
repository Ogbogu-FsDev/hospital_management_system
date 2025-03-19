from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QSizePolicy, QGridLayout
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from ui.sidebar import Sidebar
from ui.ControlActions.home import home
from ui.ControlActions.personal_details import personal_details
from ui.ControlActions.patient_records import patient_records
from ui.ControlActions.appointments import appointments
from ui.ControlActions.billing import billing
from ui.ControlActions.reports import reports
from ui.ControlActions.inventory import inventory
from ui.ControlActions.staff_board import staff_board

class DashboardWindow(QMainWindow):
    def __init__(self, user_role):
        super().__init__()
        self.setWindowTitle("Hospital Management Dashboard")
        self.showFullScreen()
        self.setStyleSheet("background-color: #ADD8E6;")

        self.user_role = user_role
        main_layout = QHBoxLayout()

        # Sidebar
        self.sidebar = Sidebar(self)
        main_layout.addWidget(self.sidebar)

        # Main Content Area
        self.content_layout = QVBoxLayout()
        container = QWidget()
        container.setLayout(self.content_layout)
        main_layout.addWidget(container)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.show_welcome_content()

    def show_welcome_content(self):
        """Display Welcome Message"""
        self.create_new_frame(f"Welcome to the Hospital Management System\nLogged in as: {self.user_role}")

    def create_new_frame(self, text):
        """Create a new frame inside the content layout"""
        if hasattr(self, 'current_frame'):
            self.current_frame.deleteLater()

        self.current_frame = QFrame(self)
        self.current_frame.setStyleSheet("background-color: white; border-radius: 15px; padding: 10px;")
        frame_layout = QVBoxLayout(self.current_frame)

        label = QLabel(text)
        label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: #333;")
        frame_layout.addWidget(label)

        self.content_layout.addWidget(self.current_frame)

    # These are delegated to the separate modules
    def home(self): home(self)
    def personal_details(self): personal_details(self)
    def patient_records(self): patient_records(self)
    def appointments(self): appointments(self)
    def billing(self): billing(self)
    def reports(self): reports(self)
    def inventory(self): inventory(self)
    def staff_board(self): staff_board(self)
    def logout(self):
        """Logout and return to login screen."""
        # Cleanup: Delete current frame before switching windows
        if hasattr(self, 'current_frame'):
            self.current_frame.deleteLater()

        # Import the LoginWindow after cleanup
        from ui.login_window import LoginWindow
        
        # Create and show the LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()

        # Close the current window (DashboardWindow)
        self.close()
