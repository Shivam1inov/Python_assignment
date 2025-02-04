# Python Program to Add Two Matrices 
a = [[2, 3, 4],
     [4, 5, 4],
     [7, 7, 8]]

b = [[6, 8, 5],
     [3, 4, 8],
     [4, 9, 4]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j] = a[i][j] + b[i][j]
for r in result:
    print(r)