# class Customer:
#     def __init__(self,cid,name,email,status):
#         self.cid=cid
#         self.name=name
#         self.email=email
#         self.status=status

#     def display(self):
#         print("CID:",c1.cid,
#               "\nname:",c1.name,
#               "\nemail:",c1.email,
#               "\nstatus:",c1.status,
#               "\n------------")

#     def update_status(self):
#         if self.status.lower() == "lead":
#             self.status="Customer"
#         elif self.status.lower() == "customer":
#             self.status="Client"
#         elif self.status.lower() == "client":
#             print("Cannot downgrade")

#     def is_deletable(self):
#         if self.status.lower() == "lead":
#             return True
#         else:
#             return False
        
# cid=int(input("Enter ID:"))
# name=input("Enter Name:")
# email=input("Enter Email:")
# status=input("Enter Status:")


# c1=Customer(cid,name,email,status)
# c1.display()
# c1.update_status()
# c1.display()
# print(c1.is_deletable())