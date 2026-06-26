s = input("enter a string: ")

reverse = "" 

for ch in s:
    reverse = ch +reverse

if s==reverse:
    print("it's palindrome")
else:
    print("it's not palindrome ")
    
    

