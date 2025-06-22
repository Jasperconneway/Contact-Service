"""
Jasper Conneway
CS 499 Category One: Software Design and Engineering
Original Project from CS 320
Completed: 06/22/2025
"""

import unittest
from src.ContactService import ContactService

class ContactServiceTest(unittest.TestCase):

    # Ensure a new contact gets added to the contact list
    def test_add_contact(self):
        contacts = ContactService.get_instance()
        contacts.add_contact("10111", "Jasper", "Conneway", "1232356914", "123 Gully Rd 4801")
        self.assertTrue(contacts.find_contact("10111").first_name == "Jasper")

    # Ensure a current contact is updated
    def test_update_contact(self):
        contacts = ContactService.get_instance()
        contacts.add_contact("10222", "Hillary", "Waffle", "1232357878", "476 Gully Rd 4801")
        contacts.update_contact("10222", "Test", "Waffle", "1232357878", "476 Gully Rd 4801")

        self.assertTrue(contacts.find_contact("10222").first_name == "Test")

    # Ensure a current contact is deleted
    def test_delete_contact(self):
        contacts = ContactService.get_instance()
        contacts.add_contact("100424", "Marissa", "Biery", "0923759101", "672 Gully Rd 4801")
        self.assertTrue(contacts.delete_contact("100424").first_name == "Marissa")

    # Ensure a new contact is added if using the update method
    def test_add_contact_by_update(self):
        contacts = ContactService.get_instance()
        contacts.update_contact("103423", "LBDOG", "CBHOUSE", "1800OURDGS", "LIVnAT Our House")
        self.assertTrue(contacts.find_contact("103423").first_name == "LBDOG")


if __name__ == '__main__':
    unittest.main()
