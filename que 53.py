numbers = input("enter a number: ")

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num 
print("largest is: ",largest)
