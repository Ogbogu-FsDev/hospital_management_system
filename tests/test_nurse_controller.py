import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.nurse_controller import NurseController
from database.db_manager import connect_db

# Set up logging for test output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_add_nurse():
    print("Testing add_nurse...")
    success = NurseController.add_nurse(user_id=2, department="ICU", supervising_doctor=1)
    print("Add Nurse Test:", "Passed" if success else "Failed")

def test_list_nurses():
    print("Testing list_nurses...")
    nurses = NurseController.list_nurses()
    if nurses:
        print("List Nurses Test: Passed")
        for nurse in nurses:
            print(nurse)
    else:
        print("List Nurses Test: Failed - No nurses found")

def test_delete_nurse():
    print("Testing delete_nurse...")
    success = NurseController.delete_nurse(nurse_id=1)  # Change ID based on existing records
    print("Delete Nurse Test:", "Passed" if success else "Failed")

if __name__ == "__main__":
    test_add_nurse()
    test_list_nurses()
    test_delete_nurse()
