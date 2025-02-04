#  Python Program to Transpose a Matrix 
A = [[2, 3, 4],
     [4, 5, 4],
     [7, 7, 8]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[j][i] = A[i][j]
for r in result:
    print(r)