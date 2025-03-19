from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QSizePolicy, QGridLayout
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from ui.styles import button_style

class Sidebar(QFrame):
    def __init__(self, dashboard_window):
        super().__init__(dashboard_window)
        self.setFixedWidth(250)  # Ensure consistent width
        self.setStyleSheet("background-color: #1E90FF; border-radius: 15px;")  

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
            "Home": dashboard_window.home,
            "Personal Details": dashboard_window.personal_details,
            "Patient Records": dashboard_window.patient_records,
            "Appointments": dashboard_window.appointments,
            "Billing": dashboard_window.billing,
            "Reports": dashboard_window.reports,
            "Inventory": dashboard_window.inventory,
            "Staff Board": dashboard_window.staff_board
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
        self.logout_button.clicked.connect(dashboard_window.logout)
        sidebar_layout.addWidget(self.logout_button)

        self.setLayout(sidebar_layout)
