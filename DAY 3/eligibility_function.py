def eligible(age):
    if age >= 18:
        return "eligible"
    else:
        return " Not eligible"
    
age=int(input("enter your age :"))

print(eligible(age))