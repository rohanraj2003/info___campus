def login_validate(username,password):
    correct_username="admin"
    correct_password="1234"

    if username == correct_username and password == correct_password:
        return True
    else:
        return False
    


user = input("Enter user name : ")
pwd = input ("Enter password :")

if login_validate(user,pwd):
    print("login successful")

else:
    print("login failed")