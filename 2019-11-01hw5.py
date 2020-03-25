#в) k-ий рядок матриці симетричний;
matrix = [[1, 33, 45], [23, 66, 7], [11, 99, 4], [22, 1, 22], [6, 6, 6], [0, 2, 4]]
lines_number = len(matrix)
columns_number = len(matrix[0])
result = [0 for x in range(0, lines_number)]
for i in range(0, lines_number):
    line = matrix[i]
    is_symmetric = 1
    for forward in range(0, columns_number // 2):
        backward = columns_number - 1 - forward
        if line[forward] != line[backward]:
            is_symmetric = 0
            break
    result[i] = is_symmetric
print(result)
