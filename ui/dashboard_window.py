import sqlite3
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QSizePolicy, QGridLayout
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from ui.styles import button_style, bubble_button_style, bubble_style


class DashboardWindow(QMainWindow):
    def __init__(self, user_role):
        super().__init__()
        self.setWindowTitle("Hospital Management Dashboard")
        self.showFullScreen()
        self.setStyleSheet("background-color: #ADD8E6;")

        self.user_role = user_role
        main_layout = QHBoxLayout()

        # Sidebar
        self.create_sidebar()

        # Main Content Area
        self.create_content_area()

        # Central Widget Setup
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.show_welcome_content()

    def create_sidebar(self):
        """Set up the sidebar layout with buttons and styling."""
        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(250)  # Ensure consistent width
        self.sidebar.setStyleSheet("background-color: #1E90FF; border-radius: 15px;")  

        sidebar_layout = QVBoxLayout()
        sidebar_layout.setSpacing(10)  # Reduce spacing between buttons
        sidebar_layout.setContentsMargins(20, 20, 20, 20)  # Adjust padding inside sidebar

        # Sidebar Title (Menu Label)
        self.create_sidebar_title(sidebar_layout)

        # Menu Buttons
        self.create_sidebar_buttons(sidebar_layout)

        # Logout Button
        self.create_logout_button(sidebar_layout)

        self.sidebar.setLayout(sidebar_layout)

    def create_sidebar_title(self, layout):
        """Create the title at the top of the sidebar."""
        sidebar_title = QLabel("MENU")
        sidebar_title.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        sidebar_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sidebar_title.setStyleSheet("color: white; padding: 10px;")
        layout.addWidget(sidebar_title)

    def create_sidebar_buttons(self, layout):
        """Create the buttons in the sidebar."""
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

        for text, func in self.buttons.items():
            button = QPushButton(text)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            button.setFixedHeight(40)
            button.setStyleSheet(button_style())
            button.clicked.connect(func)
            layout.addWidget(button)

    def create_logout_button(self, layout):
        """Create the logout button and place it at the bottom of the sidebar."""
        self.logout_button = QPushButton("Logout")
        self.logout_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.logout_button.setFixedHeight(40)
        self.logout_button.setStyleSheet(button_style())
        self.logout_button.clicked.connect(self.logout)
        layout.addWidget(self.logout_button)

    def create_content_area(self):
        """Set up the main content area."""
        self.content_layout = QVBoxLayout()
        container = QWidget()
        container.setLayout(self.content_layout)

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

    # Home (Dashboard)
    def home(self):
        """Display 3x3 grid of buttons styled like bubbles"""
        self.create_bubble_grid()

    def create_bubble_grid(self):
        """Create a 3x3 grid of bubble-styled buttons"""
        if hasattr(self, 'current_frame'):
            self.current_frame.deleteLater()

        self.current_frame = QFrame(self)
        self.current_frame.setStyleSheet("""background-color: rgba(255, 255, 255, 0.2); border-radius: 15px; padding: 20px;""")
        frame_layout = QVBoxLayout(self.current_frame)

        grid_layout = QGridLayout()
        button_labels = [str(i) for i in range(1, 10)]  # Button labels 1-9
        for i, label in enumerate(button_labels):
            button = QPushButton(label)
            button.setFixedSize(100, 100)
            button.setStyleSheet(bubble_button_style())
            grid_layout.addWidget(button, i // 3, i % 3)

        frame_layout.addLayout(grid_layout)
        self.content_layout.addWidget(self.current_frame)

    # Personal Details
    def personal_details(self):
        """Fetch user details from database and display them with professional styling."""
        user_id = 1  # Example user ID; you can modify this dynamically
        user = self.fetch_user_details(user_id)

        # Create or update the frame for personal details
        self.create_personal_details_frame(user)

    def fetch_user_details(self, user_id):
        """Fetch user details from the database."""
        try:
            conn = sqlite3.connect("/hospital_management_system/database/hospital.db")
            cursor = conn.cursor()
            cursor.execute("SELECT title, name, role, phone, email, address FROM users WHERE id = ?", (user_id,))
            user = cursor.fetchone()
            conn.close()

            if user:
                return user
            else:
                return ("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")
        except Exception as e:
            return ("Error", "Error", "Error", "Error", "Error", str(e))

    def create_personal_details_frame(self, user):
        """Create and display the personal details frame."""
        if hasattr(self, 'current_frame'):
            self.current_frame.deleteLater()

        self.current_frame = QFrame(self)
        self.current_frame.setStyleSheet("background-color: white; border-radius: 15px; padding: 20px;")
        frame_layout = QVBoxLayout(self.current_frame)
        frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        self.add_personal_details_header(frame_layout)
        self.add_personal_details_content(frame_layout, user)

        self.content_layout.addWidget(self.current_frame)

    def add_personal_details_header(self, layout):
        """Add the header to the personal details frame."""
        title_label = QLabel("Personal Details")
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title_label.setStyleSheet("color: #4CAF50; margin-bottom: 20px;")
        layout.addWidget(title_label)

    def add_personal_details_content(self, layout, user):
        """Add the content to the personal details frame."""
        grid_layout = QGridLayout()
        grid_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        labels = ["Title:", "Name:", "Role:", "Phone:", "Email:", "Address:"]
        for i, (label_text, value_text) in enumerate(zip(labels, user)):
            label = QLabel(label_text)
            label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
            label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            label.setStyleSheet("color: #333; margin-right: 20px;")

            value = QLabel(value_text)
            value.setFont(QFont("Arial", 14))
            value.setAlignment(Qt.AlignmentFlag.AlignLeft)
            value.setStyleSheet(self.bubble_style())

            grid_layout.addWidget(label, i, 0)
            grid_layout.addWidget(value, i, 1)

        layout.addLayout(grid_layout)

    def bubble_style(self):
        """Return the style for bubble widgets."""
        return """
        background-color: #ffffff;
        border-radius: 20px;
        padding: 10px;
        color: #333;
        font-size: 14px;
        border: 2px solid #66b3ff;
        margin-left: 10px;
        margin-right: 10px;
        transition: all 0.3s ease;
        """

    def hover_bubble_style(self):
        """Optional hover effect style for the bubble widget."""
        return """
        background-color: #e1f5fe;
        border: 2px solid #4caf50;
        color: #388e3c;
        """

    # Placeholder Methods
    def patient_records(self): self.create_new_frame("Patient Records content goes here.")
    def appointments(self): self.create_new_frame("Appointments content goes here.")
    def billing(self): self.create_new_frame("Billing content goes here.")
    def reports(self): self.create_new_frame("Reports content goes here.")
    def inventory(self): self.create_new_frame("Inventory content goes here.")
    def staff_board(self): self.create_new_frame("Staff Board content goes here.")
    
    def logout(self):
        """Logout and return to login screen."""
        from ui.login_window import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
