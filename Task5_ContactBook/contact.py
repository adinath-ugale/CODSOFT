contacts = []

def add_contact():
    name = input("Enter name:: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found!")
        return
    for i, c in enumerate(contacts, 1):
        print(f"\nContact {i}")
        print("Name:", c["name"])
        print("Phone:", c["phone"])

def search_contact():
    search = input("Enter name or phone to search: ").lower()
    found = False
    for c in contacts:
        if search in c["name"].lower() or search in c["phone"]:
            print("\nFound Contact:")
            print(c)
            found = True
    if not found:
        print("Contact not found!")

def update_contact():
    name = input("Enter name to update: ").lower()
    for c in contacts:
        if c["name"].lower() == name:
            c["phone"] = input("Enter new phone: ")
            c["email"] = input("Enter new email: ")
            c["address"] = input("Enter new address: ")
            print("Contact updated!")
            return
    print("Contact not found!")

def delete_contact():
    name = input("Enter name to delete: ").lower()
    for c in contacts:
        if c["name"].lower() == name:
            contacts.remove(c)
            print("Contact deleted!")
            return
    print("Contact not found!")

while True:
    print("\n---- CONTACT BOOK ----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: : ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Thank you visiting Goodbye!")
        break
    else:
        print("Invalid choice!")
