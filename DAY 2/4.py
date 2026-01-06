attempts=3
while attempts>0:
    user=input("Enter Username:")
    password=input("Enter password:")


    if user=="admin" and password=="123":
            print("Login Successfull")
            break

    else:
            attempts-=1
            print("invalid,","Attempt left:" ,attempts)
             
if attempts==0:
    print("No attempts left")
