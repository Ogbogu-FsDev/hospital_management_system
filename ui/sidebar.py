from PyQt6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QSizePolicy, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from ui.styles import button_style

class Sidebar(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedWidth(250)
        self.setStyleSheet("background-color: #1E90FF; border-radius: 15px;")

        sidebar_layout = QVBoxLayout(self)
        sidebar_title = QLabel("MENU")
        sidebar_title.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        sidebar_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sidebar_title.setStyleSheet("color: white; padding: 10px;")
        sidebar_layout.addWidget(sidebar_title)

        buttons = {
            "Home": parent.home,
            "Personal Details": parent.personal_details,
            "Patient Records": parent.patient_records,
            "Appointments": parent.appointments,
            "Billing": parent.billing,
            "Reports": parent.reports,
            "Inventory": parent.inventory,
            "Staff Board": parent.staff_board
        }

        for text, func in buttons.items():
            button = QPushButton(text)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            button.setFixedHeight(40)
            button.setStyleSheet(button_style())
            button.clicked.connect(func)
            sidebar_layout.addWidget(button)

        sidebar_layout.addStretch()
        logout_button = QPushButton("Logout")
        logout_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        logout_button.setFixedHeight(40)
        logout_button.setStyleSheet(button_style())
        logout_button.clicked.connect(parent.logout)
        sidebar_layout.addWidget(logout_button)
