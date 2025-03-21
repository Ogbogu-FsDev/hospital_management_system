from PyQt6.QtWidgets import (
    QFrame, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QFormLayout,
    QComboBox, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QDateEdit,
    QSpacerItem, QSizePolicy, QScrollArea
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QDate

from ui.styles import bubble_card_style, bubble_button_style 

from controllers.admin_controller import AdminController

def user_management(dashboard_window):
    """User Management Interface - Add, Edit, Delete Users with Bubble UI"""
    if hasattr(dashboard_window, 'current_frame'):
        dashboard_window.current_frame.deleteLater()

    dashboard_window.current_frame = QFrame(dashboard_window)
    dashboard_window.current_frame.setStyleSheet(
        "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #B0E0E6, stop:1 #87CEFA);"
        "border-radius: 15px; padding: 15px;"
    )
    layout = QVBoxLayout(dashboard_window.current_frame)

    # Title
    title_label = QLabel("User Management")
    title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
    title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title_label.setStyleSheet("color: #003366; padding: 5px;")
    layout.addWidget(title_label)

    # User Table with Bubble Theme
    user_table = QTableWidget()
    user_table.setColumnCount(14)  # We have 9 columns
    
    user_table.setHorizontalHeaderLabels([ 
        "ID", "User", "Title", "Name", "Gender", "DOB", 
        "Email", "Phone", "Address", "Role", 
        "Spec", "Dept.", "Status", "Start Date"
    ])
    user_table.setStyleSheet(""" 
        QHeaderView::section { 
            font-size: 20px; 
            font-weight: bold; 
            padding: 6px; 
            background-color: #f0f0f0; 
        } 
        """ + bubble_card_style())
    layout.addWidget(user_table)

    # Load Users from AdminController
    def load_users():
        user_table.setRowCount(0)
        admin_controller = AdminController()
        users = admin_controller.list_users()

        for user in users:
            row_position = user_table.rowCount()
            user_table.insertRow(row_position)

            user_table.setItem(row_position, 0, QTableWidgetItem(str(user[0])))  # ID
            user_table.setItem(row_position, 1, QTableWidgetItem(user[1]))  # Username
            user_table.setItem(row_position, 2, QTableWidgetItem(user[4]))  # Title
            user_table.setItem(row_position, 3, QTableWidgetItem(user[5]))  # Name
            user_table.setItem(row_position, 4, QTableWidgetItem(user[7]))  # Gender
            user_table.setItem(row_position, 5, QTableWidgetItem(user[6]))  # DOB
            user_table.setItem(row_position, 6, QTableWidgetItem(user[9]))  # Email
            user_table.setItem(row_position, 7, QTableWidgetItem(user[8]))  # Phone
            user_table.setItem(row_position, 8, QTableWidgetItem(user[10])) # Address
            user_table.setItem(row_position, 9, QTableWidgetItem(user[3]))  # Role
            user_table.setItem(row_position, 10, QTableWidgetItem(user[12])) # Spec
            user_table.setItem(row_position, 11, QTableWidgetItem(user[11])) # Dept
            user_table.setItem(row_position, 12, QTableWidgetItem(user[14])) # Status
            user_table.setItem(row_position, 13, QTableWidgetItem(user[13])) # Employment Date

    load_users()

    # Main layout for input fields
    input_layout = QFormLayout()  # Use QFormLayout to align labels and input fields

    # Title Input
    title_input = QComboBox()
    title_input.addItems(["Dr.", "Mr.", "Ms.", "Mrs.", "Prof."])
    title_input.setStyleSheet(bubble_card_style())
    input_layout.addRow(QLabel("Title:"), title_input)

    # Full Name Input
    full_name_input = QLineEdit()
    full_name_input.setPlaceholderText("Enter Full Name")
    full_name_input.setStyleSheet(bubble_card_style())
    input_layout.addRow(QLabel("Full Name:"), full_name_input)

    # Username Input
    username_input = QLineEdit()
    username_input.setPlaceholderText("Enter Username")
    username_input.setStyleSheet(bubble_card_style())
    input_layout.addRow(QLabel("Username:"), username_input)

    # Password Input
    password_input = QLineEdit()
    password_input.setPlaceholderText("Enter Password")
    password_input.setEchoMode(QLineEdit.EchoMode.Password)
    password_input.setStyleSheet(bubble_card_style())
    input_layout.addRow(QLabel("Password:"), password_input)

    # Gender Input
    gender_input = QComboBox()
    gender_input.addItems(["Male", "Female", "Other", "Prefer not to say"])
    gender_input.setStyleSheet(bubble_card_style())
    input_layout.addRow(QLabel("Gender:"), gender_input)

    # Date of Birth Input
    dob_input = QDateEdit()
    dob_input.setCalendarPopup(True)
    dob_input.setDate(QDate.currentDate())  # Default to current date
    dob_input.setDisplayFormat("dd-MM-yyyy")  # Set date format to dd-MM-yyyy
    dob_input.setStyleSheet(bubble_card_style())
    input_layout.addRow(QLabel("Date of Birth:"), dob_input)

    # Email Input
    email_input = QLineEdit()
    email_input.setPlaceholderText("Enter Email Address")
    email_input.setStyleSheet(bubble_card_style())
    input_layout.addRow(QLabel("Email:"), email_input)

    # Phone Number Input
    phone_input = QLineEdit()
    phone_input.setPlaceholderText("Enter Phone Number")
    phone_input.setStyleSheet(bubble_card_style())
    input_layout.addRow(QLabel("Phone:"), phone_input)

    # Address Input
    address_input = QLineEdit()
    address_input.setPlaceholderText("Enter Address")
    address_input.setStyleSheet(bubble_card_style())
    input_layout.addRow(QLabel("Address:"), address_input)

    # Role Dropdown
    role_dropdown = QComboBox()
    role_dropdown.addItems(["Admin", "Doctor", "Nurse", "Receptionist"])
    role_dropdown.setStyleSheet(bubble_card_style())
    input_layout.addRow(QLabel("Role:"), role_dropdown)

    # Specialization Input
    specialization_input = QLineEdit()
    specialization_input.setPlaceholderText("Enter Specialization")
    specialization_input.setStyleSheet(bubble_card_style())
    input_layout.addRow(QLabel("Specialization:"), specialization_input)

    # **Department Label and Dropdown Input**
    department_input = QComboBox()
    department_input.addItems(["Dept.", "General", "Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Surgery", "Radiology"])  # Example departments
    department_input.setStyleSheet(bubble_card_style()) 
    input_layout.addRow(QLabel("Department:"), department_input)

    # Employment Date (Non-editable)
    employment_date_input = QLineEdit()
    employment_date_input.setText(QDate.currentDate().toString("dd-MM-yyyy"))
    employment_date_input.setReadOnly(True)  # Make it non-editable
    employment_date_input.setStyleSheet(bubble_card_style())
    input_layout.addRow(QLabel("Employment Date:"), employment_date_input)

    # Add the input layout to the main layout
    layout.addLayout(input_layout)

    # Buttons Layout
    button_layout = QHBoxLayout()

    # Add User Button
    add_button = QPushButton("Add User")
    add_button.setStyleSheet(bubble_button_style())
    button_layout.addWidget(add_button)

    # Edit User Button
    edit_button = QPushButton("Edit User")
    edit_button.setStyleSheet(bubble_button_style())
    button_layout.addWidget(edit_button)

    # Delete User Button
    delete_button = QPushButton("Delete User")
    delete_button.setStyleSheet(bubble_button_style())
    button_layout.addWidget(delete_button)

    # Add the button layout to the main layout
    layout.addLayout(button_layout)

    def add_user():
        # Retrieve user input from the fields
        username = username_input.text()
        password = password_input.text()
        role = role_dropdown.currentText()
        name = full_name_input.text()
        phone = phone_input.text()
        email = email_input.text()
        address = address_input.text()
        title = title_input.currentText()

        # New input fields
        date_of_birth = dob_input.text()  # Get the date of birth from the QDateEdit input
        gender = gender_input.currentText()  # Get gender from the dropdown
        department = department_input.currentText()  # Get department from the dropdown
        specialization = specialization_input.text()  # Get specialization
        employment_date = employment_date_input.text()  # The employment date is static (non-editable)
        status = "Active"  # Assuming the default status is "Active"

        # Validate required fields
        if not username or not password or not name or not email:
            QMessageBox.warning(dashboard_window, "Error", "All fields must be filled!")
            return
        try:
            # Add user to the database using AdminController
            success = AdminController.add_user(
                username, password, role, title, name, date_of_birth, gender,
                phone, email, address, department, specialization, employment_date, status
            )
            if success:
                # Refresh the user list and show success message
                load_users()  # Refresh the user list in the table
                QMessageBox.information(dashboard_window, "Success", f"{role} added successfully!")
            else:
                QMessageBox.critical(dashboard_window, "Error", "There was an issue adding the user.")
        except Exception as e:
            QMessageBox.critical(dashboard_window, "Error", f"Error: {e}")

    def delete_user():
        # Get the selected row in the user table
        selected_row = user_table.currentRow()
        if selected_row >= 0:
            # Get the user ID from the first column (index 0)
            user_id = user_table.item(selected_row, 0)
            try:
                # Delete the user from the database using the AdminController
                success = AdminController.delete_user(user_id)
                if success:
                    # Remove the selected row from the table in the UI
                    user_table.removeRow(selected_row) 
                    # Refresh the user list to ensure it's up to date
                    load_users()  # This will reload the updated list from the database
                    # Show success message
                    QMessageBox.information(dashboard_window, "Success", "User deleted successfully!")
                else:
                    QMessageBox.critical(dashboard_window, "Error", "There was an issue deleting the user.")
            except Exception as e:
                QMessageBox.critical(dashboard_window, "Error", f"Error: {e}")

    # Connect Buttons to Functions
    add_button.clicked.connect(add_user)
    delete_button.clicked.connect(delete_user)

    dashboard_window.content_layout.addWidget(dashboard_window.current_frame)

