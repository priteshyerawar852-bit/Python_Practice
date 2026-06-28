s = [23,45,56,67,64]

for i in range(len(s)-1,-1,-1):
    print(s[i],end =" ")

    numbers = [10, 20, 30, 40, 50]

new_list = []

for i in range(len(numbers)-1, -1, -1):
    new_list.append(numbers[i])

print(new_list)