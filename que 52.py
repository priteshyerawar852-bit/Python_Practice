s = input("enter a string: ")
words = s.split()

for word in words:
    print(word[0].upper() + word[1:].lower(),end=" ")



