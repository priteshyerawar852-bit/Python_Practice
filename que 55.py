num = [23,345,23,123,33]

search = int(input("enter a number: "))

found = False

for i in num:
    if i == search:
        found = True
        break

if found:
    print("found")
else:
    print("not found")
    
