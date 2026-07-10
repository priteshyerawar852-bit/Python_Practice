l1= [1,2,3,4,5]
l2= [3,4,5,6,7]

intersection_list = []
unioun_list = []

for i in l1:
    unioun_list.append(i)

for i in l2:
    if i not in unioun_list:
        unioun_list.append(i)

print(unioun_list)
for i in l1:
    if i in l2:
        intersection_list.append(i)

print(intersection_list)

