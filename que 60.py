l = [6,5,4,3,2,1]
Descending = False

for i in range(len(l)-1):

    if l[i] > l[i+1]:
        Descending = True
        break

if Descending:
    print("Descending")
else:
    print("not  descending")


