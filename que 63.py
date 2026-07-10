l=[
    [1,2,3],
    [4,5,6],
    [3,5,7]
]

new_list = []

for row in l:
    for item in row:
        new_list.append(item)

print(new_list)