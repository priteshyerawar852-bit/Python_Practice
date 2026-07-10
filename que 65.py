l=[
    [1,2,3],
    [4,5,6],
    [3,5,7]
]
largest =l[0][0]
for row in l:
    for i in row:
        if i > largest:
            largest = i

print("largest= ",largest)
