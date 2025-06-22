"""
Jasper Conneway
CS 499 Category One: Software Design and Engineering
Original Project from CS 320
Completed: 06/22/2025
"""

from src.Contact import Contact


class ContactService:
    # Contact List
    _contacts = []
    # Contact Service object
    _service = None

    # Hidden constructor
    def __init__(self):
        pass

    # Create a unique instance for Contact List
    @classmethod
    def get_instance(cls):
        if cls._service is None:
            cls._service = cls()
        # return the ContactService instance
        return cls._service

    """
    Add a contact to the contact list
    """
    def add_contact(self, id, first_name, last_name, phone, address):
        # Create a new contact
        new_contact = None

        # If contact exists, set to new contact
        new_contact = self.find_contact(id)

        if new_contact is None:
            new_contact = Contact(id, first_name, last_name, phone, address)
            self._contacts.append(new_contact)

        # return the contact
        return new_contact

    """
    Delete a contact from the contact list
    """
    def delete_contact(self, id):
        # local variable to store contact
        delete = None

        # find contact
        delete = self.find_contact(id)

        #if contact is found, delete it
        if delete is not None:
            self._contacts.remove(delete)

        # return contact or None
        return delete

    """
    Update a contact from the contact list
    """
    def update_contact(self, id, first_name, last_name, phone, address):
        # Find contact
        contact = self.find_contact(id)

        # if contact is not found
        if contact is None:
            # add contact to list
            self.add_contact(id, first_name, last_name, phone, address)
        else:
            # contact is found, update the contact
            contact.first_name = first_name
            contact.last_name = last_name
            contact.phone = phone
            contact.address = address

        # return contact
        return contact

    """
    Find a contact in contact list by contact id
    """
    def find_contact(self, id):
        # loop through list until contact is found or reach end of list
        for contact in self._contacts:
            if contact.id == id:
                # return contact if found
                return contact

        # return None if contact not found
        return None
