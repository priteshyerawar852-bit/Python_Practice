num_1 = int(input("enter a num1 :"))
num_2 = int(input("enter a num2: "))

flag = 0

if num_1< num_2:
    pass
else:
    temp = num_1
    num_1 = num_2
    num_2 =temp


for i in range(1,11):
    for j in range(1,11):
        if num_1*j==num_2*i:
            print("The LCM is : ",num_1*j)
            flag=1
    if flag:
        break
