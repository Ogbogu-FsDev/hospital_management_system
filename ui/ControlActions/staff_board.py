from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QSizePolicy, QGridLayout
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

def staff_board(dashboard_window):
    """Display Staff Board content."""
    if hasattr(dashboard_window, 'current_frame'):
        dashboard_window.current_frame.deleteLater()

    dashboard_window.current_frame = QFrame(dashboard_window)
    dashboard_window.current_frame.setStyleSheet("background-color: white; border-radius: 15px; padding: 20px;")
    
    frame_layout = QVBoxLayout(dashboard_window.current_frame)
    
    title_label = QLabel("Staff Board")
    title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
    title_label.setStyleSheet("color: #4CAF50; margin-bottom: 20px;")
    frame_layout.addWidget(title_label)

    # Staff management features could go here, like listing staff or updating staff information
    
    dashboard_window.content_layout.addWidget(dashboard_window.current_frame)
