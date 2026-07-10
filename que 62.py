l =[1,2,3,4,5,6]

search = int(input("enter a number: "))
replace = int(input("enter a number : "))

for i in range(len(l)):
    if l[i] == search:
        l[i]= replace
        break

print(l)