# First Matrix
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Second Matrix
B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Result Matrix (Initially all zeros)
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Matrix Multiplication
for i in range(3):          # Rows of A
    for j in range(3):      # Columns of B
        for k in range(3):  # Multiplication
            result[i][j] += A[i][k] * B[k][j]

# Print Result
print("Result Matrix:")

for row in result:
    print(row)