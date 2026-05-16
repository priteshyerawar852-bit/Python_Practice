num = int(input("enter a 4 digit number: "))
temp = num
sum =0 

while temp>0:
    digit = temp %10
    sum = sum + digit **4
    temp = temp // 10

if num == sum:
    print("sahi hai bete ")
else:
    print("hag diya bhai ")

