print("\n--- Phonebook App ---")
phonebook = {}
while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        phonebook[name] = number
        print("Contact saved!")
    elif choice == "2":
        print("\nContacts:")
        for name, num in phonebook.items():
            print(name, ":", num)
    elif choice == "3":
        name = input("Enter name to search: ")
        if name in phonebook:
            print("Number:", phonebook[name])
        else:
            print("Not found")
    elif choice == "4":
        break
    else:
        print("Invalid choice")