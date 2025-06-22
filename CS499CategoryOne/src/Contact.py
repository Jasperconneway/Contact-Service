"""
Jasper Conneway
CS 499 Category One: Software Design and Engineering
Original Project from CS 320
Completed: 06/22/2025
"""

class Contact:
    def __init__(self, id, first_name, last_name, phone, address):
        # Constructor initializes the attributes for a contact

        # contact id cannot be empty or longer than 10 digits
        if id is None or len(id) > 10:
            raise ValueError('Invalid Contact ID.')

        # set the contact id, then call setter methods
        self._id = id # private attribute -> no setter required
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address


    @property
    def id(self):
        return self._id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if value is None or len(value) > 10:
            raise ValueError('First Name cannot be blank or longer than 10 characters')
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value is None or len(value) > 10:
            raise ValueError('Last Name cannot be blank or longer than 10 characters')
        self._last_name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if value is None or len(value) != 10:
            raise ValueError('Phone Number cannot be blank and has to be 10 characters')
        self._phone = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if value is None or len(value) > 30:
            raise ValueError('Address cannot be blank or longer than 30 characters')
        self._address = value

