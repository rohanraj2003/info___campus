customers = {
    1: {"name": "Arun", "email": "arun@gmail.com", "status": "Lead"},
    2: {"name": "Meera", "email": "meera@gmail.com", "status": "Customer"}
}

while True:
    print("\nMENU")
    print("1. Display All Customers")
    print("2. Add New Customer")
    print("3. Update Customer Status")
    print("4. Search Customer")
    print("5. Delete Customer")
    print("6. Display Customers by Status")
    print("7. Count Customers by Status")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if not customers:
            print("No customers available.")
        else:
            for cid, details in customers.items():
                print("\nID:", cid)
                print("Name:", details["name"])
                print("Email:", details["email"])
                print("Status:", details["status"])
                print("-----------------------------")

    elif choice == 2:
        cid = int(input("Enter Customer ID: "))

        if cid in customers:
            print("ID already exists!")
        else:
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            status = input("Enter Status: ")

            for c in customers:
                if customers[c]["email"] == email:
                    print("Email already exists!")
                    break
            else:
                customers[cid] = {
                    "name": name,
                    "email": email,
                    "status": status
                }
                print("Added Successfully!")





    elif choice == 3:
        cid = int(input("Enter Customer ID: "))

        if cid in customers:
            status = customers[cid]["status"]

            if status == "Lead":
                customers[cid]["status"] = "Customer"
            elif status == "Customer":
                customers[cid]["status"] = "Client"

            print("Updated Status:", customers[cid]["status"])
        else:
            print("Invalid Customer ID!")






    elif choice == 4:
        key = input("Enter Customer ID or Email: ")

        for cid in customers:
            if str(cid) == key or customers[cid]["email"] == key:
                print(customers[cid])
                break
        else:
            print("Customer not found!")


    
    elif choice == 5:
        cid = int(input("Enter customer id to Delete : "))

        if cid in customers:
            if customers[cid]["status"] == "Lead":
                del customers[cid]
                print("Customer deleted successfully")

            else:
                ("cannot delete active customer : ")

        else:

            print("Invalid customer ID ! ")


    elif choice == 6:
        status = input("Enter status (Lead/Customer/Client :)")


        for cid, d in customers.items():
            if d["status"] == status:
                print(cid,d["name"],d["email"],d["status"]) 


    elif choice == 7:
        lead = customer = client = 0

        for d in customers.values():
            if d["status"] =="Lead":
                lead += 1

            if d["status"] =="Customer":
                customer += 1

            if d["status"] =="Client":
                client += 1


        print("Lead:",lead)
        print("Customer:",customer)
        print("Client:",client)


    

    elif choice == 8:
        print("Exit")
        break

    else:
        print("Invalid choice!")
