numbers = list(map(int,input("enter numbers: ").split()))

bin_size = int(input("enter a bin size: "))

histogram = {}

maximum = max(numbers)

for start in range(0,maximum +1,bin_size):
    end = start + bin_size -1 
    count =0

    for num in numbers:
        if start<=num<=end:
            count+=1

    histogram[f"{start}-{end}"] = count

print(histogram)