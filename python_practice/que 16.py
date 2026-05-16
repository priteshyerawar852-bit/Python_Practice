num =int(input("enter a num :"))

temp = num
sum= 0
while temp>0:
    digits = temp %10
    sum = sum + digits**3
    temp = temp // 10

if num == sum:
 print("yes you got it!!")
else:
        print("no sorry u are unlucky ")
