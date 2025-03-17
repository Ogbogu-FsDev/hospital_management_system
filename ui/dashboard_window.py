import sqlite3
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QSizePolicy, QGridLayout
)
from PyQt6.QtGui import QFont, QPixmap
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

        # Sidebar Styling
        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(250)  # Ensure consistent width
        self.sidebar.setStyleSheet("background-color: #1E90FF; border-radius: 15px;")  

        sidebar_layout = QVBoxLayout()
        sidebar_layout.setSpacing(10)  # Reduce spacing between buttons
        sidebar_layout.setContentsMargins(20, 20, 20, 20)  # Adjust padding inside sidebar

        # Sidebar Title (Menu Label)
        sidebar_title = QLabel("MENU")
        sidebar_title.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        sidebar_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sidebar_title.setStyleSheet("color: white; padding: 10px;")
        sidebar_layout.addWidget(sidebar_title)

        # Menu Buttons
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
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)  # Ensure button width matches sidebar
            button.setFixedHeight(40)  # Set a fixed height for consistency
            button.setStyleSheet(button_style())
            button.clicked.connect(func)
            sidebar_layout.addWidget(button)

        sidebar_layout.addStretch()  # Pushes Logout to the bottom

        # Logout Button (Always at the Bottom)
        self.logout_button = QPushButton("Logout")
        self.logout_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.logout_button.setFixedHeight(40)
        self.logout_button.setStyleSheet(button_style())
        self.logout_button.clicked.connect(self.logout)
        sidebar_layout.addWidget(self.logout_button)

        self.sidebar.setLayout(sidebar_layout)
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

    # Button Functions
    def home(self):
        """Display 3x3 grid of buttons styled like bubbles"""
        self.create_bubble_grid()

    def create_bubble_grid(self):
        """Create a 3x3 grid of bubble-styled buttons"""
        if hasattr(self, 'current_frame'):
            self.current_frame.deleteLater()

        self.current_frame = QFrame(self)
        self.current_frame.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.2); 
            border-radius: 15px; 
            padding: 20px;
        """)
        frame_layout = QVBoxLayout(self.current_frame)

        # Create a 3x3 grid layout for buttons
        grid_layout = QGridLayout()

        # Create 9 buttons with bubble style
        button_labels = [str(i) for i in range(1, 10)]  # Button labels 1-9
        for i, label in enumerate(button_labels):
            button = QPushButton(label)
            button.setFixedSize(100, 100)  # Set a fixed size for each button
            button.setStyleSheet(bubble_button_style())
            grid_layout.addWidget(button, i // 3, i % 3)  # Place button in grid

        # Add grid to the frame layout
        frame_layout.addLayout(grid_layout)
        
        self.content_layout.addWidget(self.current_frame)

    # Modify personal_details function to fetch and display user details from hospital.db
    def personal_details(self):
        """Fetch user details from database and display them with professional styling."""
        user_id = 1  # Example user ID; you can modify this dynamically
        
        try:
            conn = sqlite3.connect("/hospital_management_system/database/hospital.db")
            cursor = conn.cursor()
            
            cursor.execute("SELECT title, name, role, phone, email, address FROM users WHERE id = ?", (user_id,))
            user = cursor.fetchone()
            conn.close()
            
            if user:
                title, name, role, phone, email, address = user
            else:
                title, name, role, phone, email, address = "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"
        except Exception as e:
            title, name, role, phone, email, address = "Error", "Error", "Error", "Error", "Error", str(e)
        
        # Remove previous frame if exists
        if hasattr(self, 'current_frame'):
            self.current_frame.deleteLater()
        
        # Create the main frame for personal details
        self.current_frame = QFrame(self)
        self.current_frame.setStyleSheet("background-color: white; border-radius: 15px; padding: 20px;")
        
        # Create a vertical layout for the main frame
        frame_layout = QVBoxLayout(self.current_frame)
        frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)  # Align to top-left
        
        # Title for the section (aligned left)
        title_label = QLabel("Personal Details")
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title_label.setStyleSheet("color: #4CAF50; margin-bottom: 20px;")
        frame_layout.addWidget(title_label)
        
        # Create a grid layout for structured display (aligned left)
        grid_layout = QGridLayout()
        grid_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)  # Align grid layout to left
        
        labels = ["Title:", "Name:", "Role:", "Phone:", "Email:", "Address:"]
        values = [title, name, role, phone, email, address]
        
        for i, (label_text, value_text) in enumerate(zip(labels, values)):
            # Label with bold font, aligned left
            label = QLabel(label_text)
            label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
            label.setAlignment(Qt.AlignmentFlag.AlignLeft)  # Align the label to the left
            label.setStyleSheet("color: #333; margin-right: 20px;")

            # Value displayed in bubble style
            value = QLabel(value_text)
            value.setFont(QFont("Arial", 14))
            value.setAlignment(Qt.AlignmentFlag.AlignLeft)  # Align the value to the left
            value.setStyleSheet(self.bubble_style())
            
            # Add label and value to the grid layout
            grid_layout.addWidget(label, i, 0)
            grid_layout.addWidget(value, i, 1)
        
        # Add the grid layout to the main frame layout
        frame_layout.addLayout(grid_layout)
        
        # Add the frame to the content layout of the parent widget
        self.content_layout.addWidget(self.current_frame)

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
