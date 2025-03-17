from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from ui.sidebar import Sidebar
from ui.content_manager import ContentManager
from ui.ui_database_manager import UIDatabaseManager  # Import from ui/

class DashboardWindow(QMainWindow):
    def __init__(self, user_role):
        super().__init__()
        self.setWindowTitle("Hospital Management Dashboard")
        self.showFullScreen()
        self.setStyleSheet("background-color: #ADD8E6;")
        self.user_role = user_role
        self.db_manager = UIDatabaseManager()  # Initialize database manager

        main_layout = QHBoxLayout()
        self.sidebar = Sidebar(self)
        main_layout.addWidget(self.sidebar)

        self.content_layout = QVBoxLayout()
        container = QWidget()
        container.setLayout(self.content_layout)
        main_layout.addWidget(container)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.show_welcome_content()

    def show_welcome_content(self):
        """Display a welcome message with live stats from the database."""
        stats = self.db_manager.get_dashboard_stats()
        if "error" in stats:
            message = f"Welcome to the Hospital Management System\nLogged in as: {self.user_role}\nError fetching stats."
        else:
            message = f"Welcome to the Hospital Management System\nLogged in as: {self.user_role}\nTotal Patients: {stats['patients']}\nTotal Appointments: {stats['appointments']}"

        ContentManager.create_new_frame(self, message)
