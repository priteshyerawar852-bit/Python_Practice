a = int(input("enter a  4 digit num: "))

reverse = 0

while a > 0:
    digit = a % 10
    reverse = reverse * 10 + digit
    a = a // 10

print("reverse is : ", reverse)
