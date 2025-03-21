from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame
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
from ui.ControlActions.user_management import user_management

class DashboardWindow(QMainWindow):
    def __init__(self, user_role, username):
        super().__init__()
        self.setWindowTitle("Hospital Management Dashboard")
        self.showFullScreen()
        self.setStyleSheet("background-color: #ADD8E6;")

        self.user_role = user_role
        self.username = username
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
        """Display an enhanced Welcome Page with styling, user details, and an advertisement banner."""
        if hasattr(self, 'current_frame'):
            self.current_frame.deleteLater()

        # Create main frame for the welcome page
        self.current_frame = QFrame(self)
        self.current_frame.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #87CEEB, stop:1 #1E90FF);"
                                        "border-radius: 15px; padding: 20px;")

        frame_layout = QVBoxLayout(self.current_frame)
        frame_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Welcome Message with Bubbly Font
        welcome_label = QLabel("Welcome to the Hospital Management System")
        welcome_label.setFont(QFont("Comic Sans MS", 22, QFont.Weight.Bold))  # Bubbly Font
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("color: white; margin-bottom: 15px;")
        frame_layout.addWidget(welcome_label)

        # User Info (User Role & Department)
        user_label = QLabel(f"Logged in as: <b>{self.user_role}</b>")
        user_label.setFont(QFont("Arial", 16))
        user_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        user_label.setStyleSheet("color: #ffffff; background: rgba(255, 255, 255, 0.2); padding: 10px; border-radius: 10px;")
        frame_layout.addWidget(user_label)

        # Current Task & Department
        department = "Emergency"  # Placeholder: Fetch from database/user session
        current_task = "Reviewing Patient Records"  # Placeholder: Fetch dynamically

        task_label = QLabel(f"Current Task: <b>{current_task}</b>\n Department: <b>{department}</b>")
        task_label.setFont(QFont("Arial", 14))
        task_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        task_label.setStyleSheet("color: #ffffff; background: rgba(255, 255, 255, 0.2); padding: 10px; border-radius: 10px; margin-top: 10px;")
        frame_layout.addWidget(task_label)

        # Advertisement Banner
        banner = QLabel("Hospital Announcement: Free Health Check-ups Every Friday!")
        banner.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        banner.setAlignment(Qt.AlignmentFlag.AlignCenter)
        banner.setStyleSheet("color: #FFD700; background: rgba(0, 0, 0, 0.6); padding: 10px; border-radius: 10px; margin-top: 20px;")
        frame_layout.addWidget(banner)

        # Add to content layout
        self.content_layout.addWidget(self.current_frame)

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
    def user_management(self): user_management(self)
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

