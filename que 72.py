d = {'a': 1, 'b': 2, 'c': 3}

max_value = max(d.values())
min_value = min(d.values())

max_key = ""
min_key = ""

for key in d:
    if d[key] == max_value:
        max_key = key

    if d[key] == min_value:
        min_key = key

d[max_key], d[min_key] = d[min_key], d[max_key]

print(d)