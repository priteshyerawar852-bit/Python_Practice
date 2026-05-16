import math
sal = float(input("enter a salary : "))

HRA =sal*0.1

DA = sal*0.05

PF = sal*0.03

if sal >= 5 and sal<= 10 :
    tax = sal*0.1
elif sal >= 11  and sal < 20:
    tax = sal*0.2
else: 
    sal >= 20 
    tax = sal*0.3

final_amount = sal - (HRA+DA+tax)

print("asli rakkam hai itna : ",final_amount)


    

