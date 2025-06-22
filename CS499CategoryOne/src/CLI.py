"""
Jasper Conneway
CS 499 Category One: Software Design and Engineering
Original Project from CS 320
Completed: 06/22/2025
"""

from src.ContactService import ContactService

def display_menu():
    print("\n======= Contact Service Menu =======")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Delete Contact")
    print("4. View Contact")
    print("5. Exit")

def main():
    service = ContactService.get_instance()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                id = input("Enter Contact ID: ").strip()
                first_name = input("Enter Contact First Name: ").strip()
                last_name = input("Enter Contact Last Name: ").strip()
                phone = input("Enter Contact Phone Number (10 digits): ").strip()
                address = input("Enter Contact Address: ").strip()

                service.add_contact(id, first_name, last_name, phone, address)
                print("Contact was successfully added.")

            except Exception as e:
                print(e)

        elif choice == "2":
            try:
                id = input("Enter Contact ID: ").strip()
                first_name = input("Enter Contact First Name: ").strip()
                last_name = input("Enter Contact Last Name: ").strip()
                phone = input("Enter Contact Phone Number (10 digits): ").strip()
                address = input("Enter Contact Address: ").strip()

                service.update_contact(id, first_name, last_name, phone, address)
                print("Contact was successfully updated.")

            except Exception as e:
                print(e)

        elif choice == "3":
            try:
                id = input("Enter Contact ID: ").strip()

                service.delete_contact(id)
                print("Contact was successfully deleted.")

            except Exception as e:
                print(e)

        elif choice == "4":
            try:
                id = input("Enter Contact ID: ").strip()

                contact = service.find_contact(id)
                print("Contact was successfully found.")
                print("Contact Name: " + contact.first_name + " " + contact.last_name)
                print("Contact Phone Number: " + contact.phone)
                print("Contact Address: " + contact.address)


            except Exception as e:
                print(e)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()



