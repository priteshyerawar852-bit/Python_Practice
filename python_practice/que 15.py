a,b,c = map(int , input("enter a 3 digits:" ).split())
sq1 = a**2
sq2 = b**2
sq3 = c**2

result = sq1 +sq2 +sq3
print("answer is ",result)
                   
num = int(input("Enter a three digit number: "))

a = num % 10
num = num // 10

b = num % 10
num = num // 10

c = num % 10

result = a**2 + b**2 + c**2

print("Sum of squares of digits is:", result)