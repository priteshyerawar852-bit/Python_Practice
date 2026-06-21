import math


n = int(input("enter a numerator: "))
m = int(input("enter a denominator: "))

gcd = math.gcd(n,m)

n = n//gcd
m= m//gcd

print("simplified is: ",n,"/",m)


