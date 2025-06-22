package contact;

/*
 * @author Jasper Conneway
 * CS 320 Contact class
 */
public class Contact {

	private String id;
	private String firstName;
	private String lastName;
	private String phone;
	private String address;

	/*
	 * Constructor for a new Contact
	 * 
	 * @param id, firstName, lastName, phone, address Verify all except address are
	 * neither null nor longer than 10 digits/characters Verify address is not null
	 * nor longer than 30 characters Set each parameter if they pass each test
	 */
	public Contact(String id, String firstName, String lastName, String phone, String address) {
		// throw exception if parameter does not meet requirements

		if (id == null || id.length() > 10) {
			throw new IllegalArgumentException("Invalid Contact ID.");
		}
		
		this.id = id;
		setFirstName(firstName);
		setLastName(lastName);
		setPhone(phone);
		setAddress(address);

	}

	// Getter for id
	public String getId() {
		return id;
	}

	// Getter for first name
	public String getFirstName() {
		return firstName;
	}

	// Getter for last name
	public String getLastName() {
		return lastName;
	}

	// Getter for phone number
	public String getPhone() {
		return phone;
	}

	// Getter for address
	public String getAddress() {
		return address;
	}

	public void setFirstName(String firstName) {
		if (firstName == null || firstName.length() > 10) {
			throw new IllegalArgumentException("Invalid First Name.");
		}
		this.firstName = firstName;
	}

	public void setLastName(String lastName) {
		if (lastName == null || lastName.length() > 10) {
			throw new IllegalArgumentException("Invalid Last Name.");
		}
	}

	public void setPhone(String phone) {
		if (phone == null || phone.length() != 10) {
			throw new IllegalArgumentException("Invalid Phone Number.");
		}
	}

	public void setAddress(String address) {
		if (address == null || address.length() > 30) {
			throw new IllegalArgumentException("Invalid Address.");
		}
	}
}
