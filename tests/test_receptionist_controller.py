import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.receptionist_controller import ReceptionistController # type: ignore
from database.db_manager import connect_db

# Set up logging for test output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_add_receptionist():
    print("Testing add_receptionist...")
    success = ReceptionistController.add_receptionist(user_id=2, department="Front Desk", assigned_doctor=1)
    print("Add Receptionist Test:", "Passed" if success else "Failed")

def test_list_receptionists():
    print("Testing list_receptionists...")
    receptionists = ReceptionistController.list_receptionists()
    if receptionists:
        print("List Receptionists Test: Passed")
        for receptionist in receptionists:
            print(receptionist)
    else:
        print("List Receptionists Test: Failed - No receptionists found")

def test_delete_receptionist():
    print("Testing delete_receptionist...")
    success = ReceptionistController.delete_receptionist(receptionist_id=1)  # Change ID based on existing records
    print("Delete Receptionist Test:", "Passed" if success else "Failed")

if __name__ == "__main__":
    test_add_receptionist()
    test_list_receptionists()
    test_delete_receptionist()
