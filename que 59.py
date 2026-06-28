l = [1,2,3,4,5]
ascending = True

for i in range(len(l)-1):

    if l[i] > l[i+1]:
        ascending = False
        break

if ascending:
    print("Ascending")
else:
    print("not ascending")


