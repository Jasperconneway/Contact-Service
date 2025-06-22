package contact;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
/*
 * @author Jasper Conneway
 * CS 320 ContactTest class
 */
class ContactTest {

	@Test
	void testContact() {
		Contact contact = new Contact("10111", "Jasper", "Conneway", "1232356914", "123 Gully Rd 4801");
		assertTrue(contact.getId().equals("10111"));
		assertTrue(contact.getFirstName().equals("Jasper"));
		assertTrue(contact.getLastName().equals("Conneway"));
		assertTrue(contact.getPhone().equals("1232356914"));
		assertTrue(contact.getAddress().equals("123 Gully Rd 4801"));
	}

	@Test 
	void testContactIdTooLong() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("10111095689", "Jasper", "Conneway", "1232356914", "123 Gully Rd 4801");
		});
	}
	
	@Test 
	void testContactFirstNameTooLong() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("10111", "Jasper Arys", "Conneway", "1232356914", "123 Gully Rd 4801");
		});
	}
	
	@Test 
	void testContactLastNameTooLong() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("10111", "Willow", "Silverstein", "1232356914", "123 Gully Rd 4801");
		});
	}
	
	@Test 
	void testContactPhoneNotTenDigits() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("10111", "Jasper Arys", "Conneway", "1232356914", "123 Gully Rd 4801");
		});
	}
	
	@Test 
	void testContactAddressTooLong() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("10111", "Jasper", "Conneway", "1232356914", "123 Gullison Rd Norston DZ 20932");
		});
	}
	
	@Test 
	void testContactIdIsNull() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact(null, "Jasper", "Conneway", "1232356914", "123 Gully Rd 4801");
		});
	}
	
	@Test 
	void testContactFirstNameIsNull() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("10111", null, "Conneway", "1232356914", "123 Gully Rd 4801");
		});
	}
	
	@Test 
	void testContactLastNameIsNull() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("10111", "Jasper", null, "1232356914", "123 Gully Rd 4801");
		});
	}
	
	@Test 
	void testContactPhoneIsNull() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("10111", "Jasper", "Conneway", null, "123 Gully Rd 4801");
		});
	}
	
	@Test 
	void testContactAddresssIsNull() {
		Assertions.assertThrows(IllegalArgumentException.class, () -> {
			new Contact("10111", "Jasper", "Conneway", "1232356914", null);
		});
	}
	
}
