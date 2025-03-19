from PyQt6.QtWidgets import QFrame, QGridLayout, QPushButton, QVBoxLayout
from ui.styles import home_button_style, bubble_button_style

def home(dashboard_window):
    """Display 3x3 grid of buttons styled like bubbles"""
    if hasattr(dashboard_window, 'current_frame'):
        dashboard_window.current_frame.deleteLater()

    dashboard_window.current_frame = QFrame(dashboard_window)
    dashboard_window.current_frame.setStyleSheet(home_button_style())
    frame_layout = QVBoxLayout(dashboard_window.current_frame)

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
    
    dashboard_window.content_layout.addWidget(dashboard_window.current_frame)
