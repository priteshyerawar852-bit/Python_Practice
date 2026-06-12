p=float(input("enter principal: "))
r=float(input("enter rate: "))
t=float(input("enter time: "))

amount = p*((1+r/100)**t)

ci = amount-p
print("CI is: ",ci)
print("amount is : ",amount)
