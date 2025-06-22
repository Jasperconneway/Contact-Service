package contact;

import java.util.ArrayList;
import java.util.List;
/*
 * @author Jasper Conneway
 * CS 320 ContactService class
 */
public class ContactService {
	// Contact List
	private List<Contact> contacts = new ArrayList<Contact>();

	// Contact Service object
	private static ContactService service;

	// Hidden constructor
	private ContactService() {
	}

	// Create a unique instance for Contact List
	public static ContactService getInstance() {
		if (service == null) {
			service = new ContactService();
		}

		return service;
	}

	/*
	 * Add contact to the contact list
	 */
	public Contact addContact(String id, String firstName, String lastName, String number, String address) {
		// Create a new contact
		Contact newContact = null;

		// If contact exists, set to new contact
		newContact = findContact(id);

		// If contact does not exist, create a new contact
		if (newContact == null) {
			newContact = new Contact(id, firstName, lastName, number, address);
			contacts.add(newContact);
		}

		// return the contact
		return newContact;
	}

	/*
	 * Delete contact by contact id
	 */
	public Contact deleteContact(String id) {
		// local variable to store contact
		Contact delete = null;
		
		// find contact
		delete = findContact(id);
		
		// if contact is found, delete it
		if (delete != null) {
			contacts.remove(delete);
		}
		
		// return contact or null
		return delete;
	}

	/*
	 * Update contact or add to contact list
	 */
	public Contact updateContact(String id, String firstName, String lastName, String number, String address) {
		Contact contact = null;
		
		// Find contact
		contact = findContact(id);

		// If contact is not found
		if (contact == null) {
			// add contact to list
			addContact(id, firstName, lastName, number, address);
		} else {
			// contact is found, update contact
			contact.setFirstName(firstName);
			contact.setLastName(lastName);
			contact.setPhone(number);
			contact.setAddress(address);

		}

		// return contact
		return contact;
	}

	/*
	 * Find contact in contact list by contact id
	 */
	public Contact findContact(String id) {
		Contact contact = null;
		
		// loop through list until contact is found or reach end of list
		for (int i = 0; i < contacts.size(); ++i) {
			if (contacts.get(i).getId().equals(id)) {
				contact = contacts.get(i);
			}
		}
		
		// return contact or null
		return contact;
	}

}
