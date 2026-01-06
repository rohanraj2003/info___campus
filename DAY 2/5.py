n= int(input("enter a number:"))

odd_count = 0
even_count = 0

for i in range (1,n+1):
    if i % 2 ==0:
        even_count +=1
    else:
        odd_count +=1

print("Count of even numbers:" ,even_count)
print("Count of odd numbers:" ,odd_count)                                                                                                                       
