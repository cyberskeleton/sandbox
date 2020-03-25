from math import sqrt


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __str__(self):
        return self._x, self._y


class Segment:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def __str__(self):
        return self._a, self._b

    def len(self):
        return sqrt((self._a.get_x() - self._b.get_x()) ** 2 + (self._a.get_y() - self._b.get_y()) ** 2)


class Rectangle:
    def __init__(self, a, b, c, d):
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def get_c(self):
        return self._c

    def get_d(self):
        return self._d

    def _str_(self):
        return (self._a, self._b, self._c, self._d)

    def sides(self):
        s1 = Segment(self._a, self._b).len()
        s2 = Segment(self._b, self._c).len()
        s3 = Segment(self._c, self._d).len()
        s4 = Segment(self._a, self._d).len()
        return s1, s2, s3, s4

    def perimeter(self):
        s1, s2, s3, s4 = self.sides()
        return s1 + s2 + s3 + s4

    def area(self):
        s1, s2, s3, s4 = self.sides()
        return s1*s2


def input_point(name):
    print('point name: ', name)
    input_xy = input('input x, y: ')
    input_xy_list = input_xy.split(',')
    x, y = map(float, input_xy_list)
    return Point(x, y)


def input_rectangle(rect_name):
    print('rectangle:', rect_name)
    a = input_point('a')
    b = input_point('b')
    c = input_point('c')
    d = input_point('d')
    return Rectangle(a, b, c, d)
#rectangles = []
#n = int(input('input quantity of rectangles: '))
#for i in range(n):
    #rectangles.append(input_rectangle(input('rectangle name: ')))
rect = input_rectangle('rec')
print('perim ', Rectangle.perimeter(rect))
print('ploscha ', Rectangle.area(rect))
print(Rectangle._str_(rect))
