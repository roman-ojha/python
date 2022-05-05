def multiplyMatrix(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(0, 2):
        for j in range(0, 2):
            for k in range(0, 2):
                C[i][j] += A[i][k] * B[k][j]
    return C


A = [[0, 0], [0, 0]]
B = [[0, 0], [0, 0]]

print("Enter Value of Two matrix:\n")
print("Enter value for Matrix A: ")
for i in range(0, 2):
    for j in range(0, 2):
        A[i][j] = int(input(f"A[{i}][{j}]: "))
print("Enter Value for Matrix B: ")
for i in range(0, 2):
    for j in range(0, 2):
        B[i][j] = int(input(f"B[{i}][{j}]: "))


C: list[list[int]] = multiplyMatrix(A, B)
print(C)
