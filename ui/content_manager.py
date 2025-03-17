from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class ContentManager:
    @staticmethod
    def create_new_frame(parent, text):
        if hasattr(parent, 'current_frame'):
            parent.current_frame.deleteLater()

        parent.current_frame = QFrame(parent)
        parent.current_frame.setStyleSheet("background-color: white; border-radius: 15px; padding: 10px;")
        frame_layout = QVBoxLayout(parent.current_frame)

        label = QLabel(text)
        label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: #333;")
        frame_layout.addWidget(label)

        parent.content_layout.addWidget(parent.current_frame)
