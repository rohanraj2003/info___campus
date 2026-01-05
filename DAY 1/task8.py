balance = 10000

withdraw =int(input("Enter the amount to withdraw"))

if withdraw<=balance:
    print("Transaction Successfull")

else:
    print("insufficient balance")