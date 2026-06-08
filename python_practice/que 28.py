digits = [1,2,3,4]

for i in digits:
    for j in digits:
        if j!=i:
            for k in digits:
                if j != k and j != i:
                    for l in digits:
                        if l!= k and l != j and l != i:
                            print(i,j,k,l)