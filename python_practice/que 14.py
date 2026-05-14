tem = float(input("enter a temperature: "))
h = float(input("enter a humidity: "))

if(tem>=30 and h>=90):
    print("hot and humid")
elif(tem>=30 and h<90):
    print("hot")
elif(tem<30 and h>=90):
    print("cool and humid")
else:
    print("cool")
