def bubble_style():
    return """
        QLineEdit {
            background-color: white;
            border-radius: 15px;
            padding: 8px;
            border: 2px solid #87CEEB;
            font-size: 14px;
        }
    """

def bubble_button_style():
    return """
        QPushButton {
            background-color: rgba(255, 255, 255, 0.6); /* Semi-transparent background */
            border-radius: 10px;
            padding: 15px;
            font-size: 16px;
            font-weight: bold;
            color: black;
            border: 2px solid #87CEEB; /* Light blue border */
        }
        QPushButton:hover {
            background-color: rgba(173, 216, 230, 0.8); /* Light blue on hover */
        }
        QPushButton:pressed {
            background-color: rgba(70, 130, 180, 0.9); /* Darker blue when pressed */
        }
    """
    
def button_style():
    return """
        QPushButton {
            background-color: #00BFFF;
            color: white;
            border-radius: 15px;
            padding: 10px;
            font-size: 14px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #1E90FF;
        }
    """
