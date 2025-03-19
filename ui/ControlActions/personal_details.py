import sqlite3

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QSizePolicy, QGridLayout
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from ui.styles import empty_bubble_style

def personal_details(dashboard_window):
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
    
    if hasattr(dashboard_window, 'current_frame'):
        dashboard_window.current_frame.deleteLater()

    dashboard_window.current_frame = QFrame(dashboard_window)
    dashboard_window.current_frame.setStyleSheet("background-color: white; border-radius: 15px; padding: 20px;")
    
    frame_layout = QVBoxLayout(dashboard_window.current_frame)
    frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)  # Align to top-left

    title_label = QLabel("Personal Details")
    title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
    title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
    title_label.setStyleSheet("color: #4CAF50; margin-bottom: 20px;")
    frame_layout.addWidget(title_label)

    grid_layout = QGridLayout()
    grid_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
    
    labels = ["Title:", "Name:", "Role:", "Phone:", "Email:", "Address:"]
    values = [title, name, role, phone, email, address]
    
    for i, (label_text, value_text) in enumerate(zip(labels, values)):
        label = QLabel(label_text)
        label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label.setStyleSheet("color: #333; margin-right: 20px;")

        value = QLabel(value_text)
        value.setFont(QFont("Arial", 14))
        value.setAlignment(Qt.AlignmentFlag.AlignLeft)
        value.setStyleSheet(empty_bubble_style())
        
        grid_layout.addWidget(label, i, 0)
        grid_layout.addWidget(value, i, 1)
    
    frame_layout.addLayout(grid_layout)
    dashboard_window.content_layout.addWidget(dashboard_window.current_frame)
