'''s = input("enter a string : ")
ch =input("enter ch : ")
new_string=""
for i in s:
    if i != ch:
        new_string = new_string+i

print(new_string)'''

s = input("enter a string : ")
ch =input("enter ch : ")

print(s.replace(ch,""))
