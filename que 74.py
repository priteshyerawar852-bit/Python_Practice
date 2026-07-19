def count_case(s):
    d={
        "uppercase":0,
        "lowercase":0
    }

    for ch in s:
        if ch.isupper():
            d["uppercase"]+=1
        elif ch.islower():
            d["lowercase"]+=1


    return d

text = input("enter a string: ")

print(count_case(text))