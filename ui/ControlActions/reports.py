from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QSizePolicy, QGridLayout
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

def reports(dashboard_window):
    """Display Reports content."""
    if hasattr(dashboard_window, 'current_frame'):
        dashboard_window.current_frame.deleteLater()

    dashboard_window.current_frame = QFrame(dashboard_window)
    dashboard_window.current_frame.setStyleSheet("background-color: white; border-radius: 15px; padding: 20px;")
    
    frame_layout = QVBoxLayout(dashboard_window.current_frame)
    
    title_label = QLabel("Reports")
    title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
    title_label.setStyleSheet("color: #4CAF50; margin-bottom: 20px;")
    frame_layout.addWidget(title_label)

    # Report generation and viewing content can go here
    
    dashboard_window.content_layout.addWidget(dashboard_window.current_frame)
