x =int(input("enter a x: "))
n=int(input("enter a n: "))
total =1
for i in range(1,n+1 ):
        total = total + (x**i)/i


print(total)
