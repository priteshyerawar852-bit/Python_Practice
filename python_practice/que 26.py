
for i in range(100,1000):

    sum =0

    temp= i

    while temp >0:

     digit = temp %10

     sum = sum + digit **3

     temp = temp // 10

    if sum == i:

        print(i)