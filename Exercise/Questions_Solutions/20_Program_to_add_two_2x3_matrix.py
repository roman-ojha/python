# Q) Create a program to multiply two matrices of size 2x3.

matrixA=[[1,2,3],[4,5,6]]
matrixB=[[7,8],[9,10],[11,12]]
mulMatrix=[]
matrix=[matrixA,matrixB]

print("Matrixs: ")
print("Matrix A:")
for p in range(0,len(matrix)):  
    print("Matrix",p,":")
    for i in range(0,len(matrix[p])):
        print("|","\t",end="")
        for j in range(0,len(matrix[p][i])):
            print(matrix[p][i][j],"\t",end=" ")
        print("|")
    

for i in range(0,len(matrixA)):
    singleMatrix=[]
    for j in range(0,len(matrixA)):
        res=0
        for k in range(0,len(matrixB)):
            res=res+matrixA[i][k]*matrixB[k][j]
        singleMatrix.append(res)
    mulMatrix.append(singleMatrix)


print("\nAfter Multiplication:")
for i in range(0,len(mulMatrix)):
        print("|","\t",end="")
        for j in range(0,len(mulMatrix[i])):
            print(mulMatrix[i][j],"\t",end=" ")
        print("|")