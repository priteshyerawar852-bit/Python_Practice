n = int(input("enter a number: "))
reverse = 0

while n>0:
    digit = n %10
    reverse = digit + reverse*10
    n = n//10

print("reverse is : ", reverse)