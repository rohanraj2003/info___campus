class CRMSystem:
    def __init__(self):
        self.customers=[]
        
    def add_customer(self):
        id=int(input("ID:"))
        name=input("Name:")
        email=input("Email:")
        status=input("Status:")
        customer={
            "id":id,
            "name":name,
            "email":email,
            "status":status
        }
        self.customers.append(customer)
        print("Customer added successfully")


    def display_all(self):
        for i in self.customers:
            print(i)

    def search_customer(self):
        s=input("Enter email or ID to search:")
        for i in self.customers:
            if str(i["id"])==s or i["email"]==s:
                print(i)

    def update_customer(self):
        p=int(input("Enter id to update"))
        for i in self.customers:
            if i["id"] == p:
                if i["status"] == "Lead":
                    i["status"] = "Customer"
                    print(i)
                elif i["status"] == "Customer":
                    i["status"] = "Client"
                    print(i)
                else:
                    print("cannot be Downgrade")
                    print(i)

    def delete_customer(self):
        k = int(input("Enter the id want to delete: "))
        for i in self.customers:
            if i["id"] == k:

                if i["status"] == "Lead":
                    self.customers.remove(i)
                    print("Customer delete")
                else:
                    print("Cannot possible to delete this customer")
                return
            
    def count_status(self):

        Lead = 0
        Customer = 0
        Client = 0

        for i in self.customers:
            if i["status"] == "Lead":
                Lead += 1

            elif i["status"] == "Customer":
                Customer += 1

            elif i["status"] == "Client":
                Client += 1

        print("\n Count of the Status")

        print("Lead",Lead)
        print("Customer",Customer)
        print("Cleint",Client)
            
crm = CRMSystem()

while True:
  
    print("1. Add Customer")
    print("2. Display All Customers")
    print("3. Search Customer")
    print("4. Update Customer Status")
    print("5. Delete Customer")
    print("6. Count Customers by Status")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        crm.add_customer()
    elif choice == 2:
        crm.display_all()
    elif choice == 3:
        crm.search_customer()
    elif choice == 4:
        crm.update_customer()
    elif choice == 5:
        crm.delete_customer()
    elif choice == 6:
        crm.count_status()
    elif choice == 7:
        print("Exiting CRM System...")
        break
    else:
        print("Invalid choice! Try again.")