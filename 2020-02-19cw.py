import numpy as np
class Matrix(np.matrix):

    def input(self):
        matrix = []
        self.height = int(input('input matrix height: '))
        for i in range(self.height):
            line = input('input line: ')
            line_str = line.split(' ')
            row = []
            for s in line_str:
                row.append(int(s))
            matrix.append(row)
            # print(matrix)
        return Matrix(matrix)

    def print(self):
        print(self)

    def mul(self, other):
        return super().__mul__(other)


    # def __str__(self):
    #     return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    # def __add__(self, other):
    #     if self.height == other.height:
    #         result = []
    #         res = []
    #         for i, j in range(self.height):
    #             sum = self.line[i][j] + other.line[i][j]
    #             res.append(sum)
    #         result.append(res)
    #     return
m = Matrix([[1,2,3],[2,3,4]])
m.print()

# n = Matrix([])
n = Matrix([]).input()
n.print()

o = n.mul(m)
o.print()

