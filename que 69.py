song = input("enter a song : ")



words =song.split()
max_count = 0

for word in words:
    count = words.count(word)
    max_count = count
    most_used= word

print("most used word is : ",word)
print("it appeared ",max_count,"times")