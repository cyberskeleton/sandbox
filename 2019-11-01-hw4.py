# г) перестановки заданого рядка матриці з заданим її стовпчиком;

matrix = [[1, 33, 45], [23, 66, 7], [11, 99, 4]]
row = int(input("line (0-2): "))
col = int(input("column (0-2): "))
replacement = [matrix[0][col], matrix[1][col], matrix[2][col]]
for i in range(0, 3):
    matrix[row][i] = replacement[i]
print(matrix)
