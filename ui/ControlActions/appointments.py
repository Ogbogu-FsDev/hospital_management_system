from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QSizePolicy, QGridLayout
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

def appointments(dashboard_window):
    """Display Appointments content."""
    if hasattr(dashboard_window, 'current_frame'):
        dashboard_window.current_frame.deleteLater()

    dashboard_window.current_frame = QFrame(dashboard_window)
    dashboard_window.current_frame.setStyleSheet("background-color: white; border-radius: 15px; padding: 20px;")
    
    frame_layout = QVBoxLayout(dashboard_window.current_frame)
    
    title_label = QLabel("Appointments")
    title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
    title_label.setStyleSheet("color: #4CAF50; margin-bottom: 20px;")
    frame_layout.addWidget(title_label)

    # Example content for appointments could go here, e.g., a table of appointments
    # More functionality can be added to view or add appointments to the database
    
    dashboard_window.content_layout.addWidget(dashboard_window.current_frame)
