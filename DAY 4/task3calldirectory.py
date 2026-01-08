customers = {
    "sulafa": "1234567",
    "rohan": "8137962377",
    "nivedh": "098879009",
    "shahidh": "0000000000"
}

name = input("Enter customer name: ")

if name in customers:
    print("Phone number:", customers[name])
else:
    print("Customer not found")
