#7.56 b

matrix = [[2, 4, 6], [1, 3, 5]]
vector = [1, 2, 3]
result = [0, 0, 0]
m = len(matrix)
n = len(vector)
for i in range(0, m):
    for j in range(0, n):
        result[i] += matrix[i][j] * vector[j]
print(result)
