x = int(input("enter a x : "))
total = (x-1)/x

for i in range(2,8):
    
    total = total + 1/2*((x-1)/x)**i

print(total)