from crm.customer import Customer
from crm.utils import valid_email,valid_status

cid= int(input("Enter the ID :"))
name = input("Name :")
email = input("Email :")
status = input("Enter a status (Lead,Customer,Client)")


if valid_email(email) and valid_status(status):
    c = Customer(cid,name, email,status)
    print(c.cid,c.name,c.email,status)
    print("Customer Added Successfully")

else:
    print("Invalid Email or Status")