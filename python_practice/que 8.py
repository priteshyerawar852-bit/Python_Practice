import math

x1=int(input("enter point 1 :"))
y1=int(input("enter point 2 :"))

x2=int(input("enter a point 3: "))
y2=int(input("enter a point 3: "))

distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

print("distance between two points is: ",distance)