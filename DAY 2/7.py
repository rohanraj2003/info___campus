pswd=(input("Enter the password : "))
leng=len(pswd)
if leng >=8:
    print("password is strong")
elif leng >=5 and leng <=7:
    print ("Password is medium ")

else:
    print("Password is weak")
