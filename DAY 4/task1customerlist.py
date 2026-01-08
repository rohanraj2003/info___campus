customer = []

while True:
    print("1.Add\n2.Remove\n3.Show\n4.Exit")
    choice = input("Enter the choice: ")

    if choice == "1":
        name = input("Enter the name of the customer: ")
        customer.append(name)
        print("Successfully added")

    elif choice == "2":
        name = input("Name to remove: ")
        if name in customer:
            customer.remove(name)
            print("Successfully removed")
        else:
            print("Customer not found")

    elif choice == "3":
        print(customer)

    elif choice == "4":
        break
