package contact;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
/*
 * @author Jasper Conneway
 * CS 320 ContactServiceTest class
 */
class ContactServiceTest {

	@Test
	void testAddContact() {
		ContactService contacts = ContactService.getInstance();
		contacts.addContact("10111", "Jasper", "Conneway", "1232356914", "123 Gully Rd 4801");
		assertTrue(contacts.findContact("10111").getFirstName().equals("Jasper"));
		
	}

	@Test
	void testUpdateContact() {
		ContactService contacts = ContactService.getInstance();
		contacts.addContact("10222", "Hillary", "Waffle", "1232357878", "476 Gully Rd 4801");
		contacts.updateContact("10222", "Test", "Waffle", "1232357878", "476 Gully Rd 4801");
		
		assertTrue(contacts.findContact("10222").getFirstName().equals("Test"));
	}
	
	@Test
	void testDeleteContact() {
		ContactService contacts = ContactService.getInstance();
		contacts.addContact("100424", "Marissa", "Biery", "0923759101", "672 Gully Rd 4801");
		assertTrue(contacts.deleteContact("100424").getFirstName().equals("Marissa"));
		
	}
	
	@Test
	void testAddContactByUpdate() {
		ContactService contacts = ContactService.getInstance();
		contacts.updateContact("103423", "LBDOG", "CBHOUSE", "1800OURDGS", "LIVnAT Our House");
		assertTrue(contacts.findContact("103423").getFirstName().equals("LBDOG"));
	}
}
