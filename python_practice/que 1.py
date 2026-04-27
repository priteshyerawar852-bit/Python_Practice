
age1 = int(input("enter age 1: "))
age2 = int(input("enter age 2: "))
age3 = int(input("enter age 3: "))

if age1 >= age2 and age1 >= age3:
    print("age1 is oldest:",age1)
elif age2 >= age1 and age2 >= age3:
    print("age2 is oldest",age2)
else:
    print("age3 is oldest:",age3)


