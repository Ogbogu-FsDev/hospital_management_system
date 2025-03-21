from PyQt6.QtWidgets import (
    QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QHBoxLayout, QFrame, QGridLayout, QProgressBar
)
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtCore import Qt, QSize

from ui.styles import home_button_style, bubble_button_style

def home(dashboard_window):
    """Updated Hospital Management Dashboard with key stats and quick actions."""
    if hasattr(dashboard_window, 'current_frame'):
        dashboard_window.current_frame.deleteLater()

    dashboard_window.current_frame = QFrame(dashboard_window)
    dashboard_window.current_frame.setStyleSheet(home_button_style())
    frame_layout = QVBoxLayout(dashboard_window.current_frame)

    # Header - Welcome Message & Logo
    header_layout = QHBoxLayout()
    welcome_label = QLabel(f"Welcome, {dashboard_window.username}!")
    welcome_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
    welcome_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

    hospital_logo = QLabel()
    logo_pixmap = QPixmap("/hospital_management_system/ui/assets/HMS-Logo.png")
    hospital_logo.setPixmap(logo_pixmap.scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio))
    hospital_logo.setAlignment(Qt.AlignmentFlag.AlignRight)

    header_layout.addWidget(welcome_label)
    header_layout.addWidget(hospital_logo)
    frame_layout.addLayout(header_layout)

    # Key Statistics Section
    stats_layout = QGridLayout()
    stats_data = {
        "Active Patients": "120",
        "Upcoming Appointments": "35",
        "Emergency Cases": "5",
        "Available Beds": "22",
        "Pending Lab Results": "18",
        "Pharmacy Stock Alerts": "3"
    }

    for i, (title, value) in enumerate(stats_data.items()):
        stat_card = QLabel(f"{title}\n{value}")
        stat_card.setStyleSheet("""
            background-color: #E0F7FA;
            border-radius: 10px;
            padding: 10px;
            font-size: 14px;
            font-weight: bold;
            color: #00796B;
            text-align: center;
        """)
        stat_card.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        stat_card.setAlignment(Qt.AlignmentFlag.AlignCenter)
        stats_layout.addWidget(stat_card, i // 3, i % 3)

    frame_layout.addLayout(stats_layout)

    # Progress Indicator for Appointments
    progress_layout = QHBoxLayout()
    appointment_label = QLabel("Daily Appointments Progress:")
    appointment_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
    progress_bar = QProgressBar()
    progress_bar.setValue(65)  # Example value for completed appointments
    progress_layout.addWidget(appointment_label)
    progress_layout.addWidget(progress_bar)
    frame_layout.addLayout(progress_layout)

    # Quick Actions Grid (Replaces simple 3x3 bubble buttons)
    grid_layout = QGridLayout()
    quick_actions = {
        "New Patient": "add_patient.png",
        "Schedule Visit": "calendar.png",
        "View Reports": "report.png",
        "Billing": "billing.png",
        "Lab Tests": "lab.png",
        "Pharmacy": "pharmacy.png"
    }

    for i, (action, icon) in enumerate(quick_actions.items()):
        button = QPushButton(action)
        button.setFixedSize(150, 60)
        button.setStyleSheet(bubble_button_style())

        icon_path = f"/hospital_management_system/ui/assets/{icon}"
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(24, 24))  # Fixed incorrect Qt.QSize usage

        grid_layout.addWidget(button, i // 3, i % 3)

    frame_layout.addLayout(grid_layout)

    dashboard_window.content_layout.addWidget(dashboard_window.current_frame)
