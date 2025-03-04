import sys
import os
import logging
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.billing_controller import BillingController

# Set up logging for test output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestBillingController(unittest.TestCase):
    
    def test_add_bill(self):
        """Test adding a new bill"""
        success = BillingController.add_bill(patient_id=1, amount=250.00, status="Pending")
        self.assertTrue(success, "Failed to add bill")
    
    def test_list_bills(self):
        """Test retrieving all bills"""
        bills = BillingController.list_bills()
        self.assertIsInstance(bills, list, "Bills should be a list")
        
    def test_update_bill_status(self):
        """Test updating a bill's status"""
        success = BillingController.update_bill_status(bill_id=1, new_status="Paid")
        self.assertTrue(success, "Failed to update bill status")
    
    def test_delete_bill(self):
        """Test deleting a bill"""
        success = BillingController.delete_bill(bill_id=1)
        self.assertTrue(success, "Failed to delete bill")

if __name__ == "__main__":
    unittest.main()
