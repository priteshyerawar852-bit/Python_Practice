s = input("sentence: ")

words = s.split()
count=0
for word in words:
    if word[0].lower()=='p':
        count = count+1
    
print(count)