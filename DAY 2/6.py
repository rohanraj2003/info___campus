
print(" 1.ADD\n 2.MULTIPLY\n 3.SUBSTRACT\n 4.EXIT\n")
choice = int(input("Enter a choice:"))

if choice == 4:
    print("Exiting")
else:    
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))

if choice == 1:
    print(a+b)

elif choice == 2:
    print(a*b)
    
elif choice == 3:
    print(a-b)


else:
    print("Invalid choice")



