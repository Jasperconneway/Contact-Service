"""
Jasper Conneway
CS 499 Category One: Software Design and Engineering
Original Project from CS 320
Completed: 06/22/2025
"""

import unittest
from src.Contact import Contact

class ContactTest(unittest.TestCase):

    def test_contact(self):
        # Create test contact that passes setter method arguments
        contact = Contact("10111", "Jasper", "Conneway", "1232356914", "123 Gully Rd 4801")

        # Test each getter method returns the correct parameter
        self.assertEqual(contact.id, "10111")
        self.assertEqual(contact.first_name, "Jasper")
        self.assertEqual(contact.last_name, "Conneway")
        self.assertEqual(contact.phone, "1232356914")
        self.assertEqual(contact.address, "123 Gully Rd 4801")

    # Test if error is raised when id is too long
    def test_contact_id_too_long(self):
        with self.assertRaises(ValueError):
            Contact("10111095689", "Jasper", "Conneway", "1232356914", "123 Gully Rd 4801")

    # Test if error is raised when first name is too long
    def test_contact_first_name_too_long(self):
        with self.assertRaises(ValueError):
            Contact("10111", "Jasper Arys", "Conneway", "1232356914", "123 Gully Rd 4801")

    # Test if error is raised when last name is too long
    def test_contact_last_name_too_long(self):
        with self.assertRaises(ValueError):
            Contact("10111", "Willow", "Silverstein", "1232356914", "123 Gully Rd 4801")

    # Test if error is raised when phone number is not 10 digits
    def test_contact_phone_not_ten_digits(self):
        with self.assertRaises(ValueError):
            Contact("10111", "Jasper Arys", "Conneway", "1232356914", "123 Gully Rd 4801")

    # Test if error is raised when address is too long
    def test_contact_address_too_long(self):
        with self.assertRaises(ValueError):
            Contact("10111", "Jasper", "Conneway", "1232356914", "123 Gullison Rd Norston DZ 20932")

    # Test if error is raised when id is empty
    def test_contact_id_is_none(self):
        with self.assertRaises(ValueError):
            Contact(None, "Jasper", "Conneway", "1232356914", "123 Gully Rd 4801")

    # Test if error is raised when first name is empty
    def test_contact_first_name_is_none(self):
        with self.assertRaises(ValueError):
            Contact("10111", None, "Conneway", "1232356914", "123 Gully Rd 4801")

    # Test if error is raised when last name is empty
    def test_contact_last_name_is_none(self):
        with self.assertRaises(ValueError):
            Contact("10111", "Jasper", None, "1232356914", "123 Gully Rd 4801")

    # Test if error is raised when phone number is empty
    def test_contact_phone_is_none(self):
        with self.assertRaises(ValueError):
            Contact("10111", "Jasper", "Conneway", None, "123 Gully Rd 4801")

    # Test if error is raised when address is empty
    def test_contact_address_is_none(self):
        with self.assertRaises(ValueError):
            Contact("10111", "Jasper", "Conneway", "1232356914", None)

if __name__ == '__main__':
    unittest.main()

