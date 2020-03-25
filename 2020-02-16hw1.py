import collections
class Matrix():
    def __init__(self):
        self.default_dict = collections.defaultdict()

    def input(self):
        self.height = int(input('input matrix non-zero elements number: '))
        for i in range(self.height):
            line = input('input element as col row value: ')
            line_str = line.split(' ')
            els = []
            for e in line_str:
                els.append(int(e))
            self.default_dict[(els[0], els[1])] = els[2]
        print(self.default_dict)

    def is_triangle(self):
        for i in self.default_dict.keys():
            if i[0] >= i[1]:
                return False
        return True
m = Matrix()
m.input()
print(m.is_triangle())
