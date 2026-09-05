matrix_a = [
    [1, 2],
    [3, 4]
]

matrix_b = [
    [5, 6],
    [7, 8]
]

result = [
    [0, 0],
    [0, 0]
]

for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += matrix_a[i][k] * matrix_b[k][j]


print("Matrix A:")
for row in matrix_a:
    print(row)

print("\nMatrix B:")
for row in matrix_b:
    print(row)

print("\nResult:")
for row in result:
    print(row)
