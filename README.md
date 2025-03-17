# Hospital Management System

---

## Project Overview

The **Hospital Management System** is an all-in-one solution for managing hospital workflows, patient records, and staff coordination. It offers an intuitive user interface for doctors, nurses, and administrative staff to manage appointments, track medical records, and generate reports efficiently.

### Features

- **Patient Management:** Register, update, and manage patient records, including medical history.
- **Appointment Scheduling:** Doctors and patients can schedule, modify, or cancel appointments.
- **Billing System:** Automated billing and invoicing for patient services.
- **Pharmacy & Inventory Management:** Track medicine stock and issue prescriptions.
- **Doctor & Staff Management:** Assign duties, maintain schedules, and manage payroll.
- **Reports & Analytics:** Generate reports on hospital performance, patient history, and financial transactions.
- **User Authentication & Role-Based Access:** Secure access control for different staff roles.

---

## Technologies Used

- **Programming Language:** Python
- **GUI Framework:** PyQt6
- **Database:** SQLite3
- **Security:** User authentication with hashed passwords
- **Data Visualization:** Matplotlib & Pandas for reports

---

## Installation Guide

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/your-repo/hospital-management-system.git
   cd hospital-management-system
   ```
2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the Application:**
   ```sh
   python main.py
   ```

---

## Database Schema

The database consists of multiple tables:

- **Patients** (Patient\_ID, Name, Age, Gender, Contact, Medical History)
- **Appointments** (Appointment\_ID, Patient\_ID, Doctor\_ID, Date, Time, Status)
- **Doctors** (Doctor\_ID, Name, Specialization, Availability)
- **Billing** (Bill\_ID, Patient\_ID, Amount, Status, Date)
- **Pharmacy** (Medicine\_ID, Name, Quantity, Expiry Date)

---

## Future Enhancements

- Cloud integration for remote access
- AI-powered diagnosis assistance
- Multi-language support
- Mobile app version

---

## Testing & Quality Assurance

To ensure system stability and reliability, the Hospital Management System undergoes multiple testing phases:

1. Unit Testing
Each module (patient management, billing, appointments) is tested individually.
Automated tests using pytest to verify function outputs.
2. Integration Testing
Tests interaction between database, GUI, and backend logic.
Ensures smooth appointment scheduling and billing transactions.
3. User Acceptance Testing (UAT)
Real hospital staff test the system for usability.
Feedback is incorporated before deployment.
4. Security Testing
Role-based access is verified.
SQL injection and authentication vulnerability tests.
5. Performance Testing
Evaluates response times for database queries.
Ensures stability under heavy user loads.
Logging & Error Handling
The system includes a robust logging mechanism for debugging and tracking operations.

---

## Logging System

Logs stored in logs/system.log for debugging and monitoring.

Captures events such as:
User logins & actions
Appointment modifications
Billing transactions
Database errors & failures
Error Handling
Try-except blocks prevent crashes.
Errors are logged with timestamps for easy debugging.
Alerts are triggered for critical failures (e.g., database connection loss).
