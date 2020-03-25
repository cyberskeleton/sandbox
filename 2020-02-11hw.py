import turtle
bob = turtle.Turtle()
window = turtle.Screen()

class Point:
    '''Точка екрану'''
    _count = 0
    _color = "black"

    def __init__(self, x, y):
        self._x = x             # _x - координата x точки
        self._y = y             # _y - координата y точки
        self._visible = False   # _visible - чи є точка видимою на екрані

    def getx(self):
        '''Повертає координату x точки
        '''
        return self._x

    def gety(self):
        '''Повертає координату y точки
        '''
        return self._y

    def onscreen(self):
        '''Перевіряє, чи є точка видимою на екрані
        '''
        return self._visible

    def son(self):
        if not self._visible:
            self._visible = True
            bob.up()
            bob.setpos(self._x, self._y)
            bob.down()
        return self._visible

    def switchon(self):
        '''Робить точку видимою на екрані
        '''
        if(self.son()):
            bob.dot(self._color)

    def soff(self):
        if self._visible:
            self._visible = False
            bob.up()
            bob.setpos(self._x, self._y)
            bob.down()
        return self._visible

    def switchoff(self):
        '''Робить точку невидимою на екрані
        '''
        if (not self.soff()):
            bob.dot(window.bgcolor())

    def move(self, dx, dy):
        '''Пересуває точку на екрані на dx, dy позицій
        '''
        vis = self._visible
        if vis:
            self.switchoff()
        self._x += dx
        self._y += dy
        if vis:
            self.switchon()

    def printcount(self):
        print('Кількість точок:', Point._count)

class Rectangle(Point):

    def __init__(self, x, y, height, width):
        self._x = x
        self._y = y
        self._height = height
        self._width = width
        super().__init__(self._x, self._y)

    def draw(self):
        bob.penup()
        bob.setpos(self._x, self._y)
        bob.setheading(0)
        bob.pendown()
        bob.forward(self._width)
        bob.setheading(270)
        bob.forward(self._height)
        bob.setheading(180)
        bob.forward(self._width)
        bob.setheading(90)
        bob.forward(self._height)
        bob.penup()

    def switchoff(self):
        if(not super().soff()):
            bob.pencolor(window.bgcolor())
            self.draw()

    def switchon(self):
        if(super().son()):
            bob.pencolor("black")
            self.draw()

class Demo():
    _rectangles = []

    def __init__(self):
        self._n = 0
        if self._n < 1 or self._n > 50 :
            self._n = int(input('input number of rectangles 0-50: '))
        bob.speed(10-round(self._n/5))
        self._x = int(input('input x: '))
        self._y = int(input('input y: '))
        self._height = int(input('input height: '))
        self._width = int(input('input width: '))
        self._skew = int(input('input skew: '))
        for i in range(0, self._n*self._skew, self._skew):
            rect = Rectangle(self._x + i, self._y + i, self._height, self._width)
            self._rectangles.append(rect)

    def draw(self):
        for rect in self._rectangles:
            rect.draw()
        input('hit Enter')

    def switchoff(self):
        for rect in self._rectangles:
            rect.switchoff()
        input('hit Enter')

    def switchon(self):
        for rect in self._rectangles:
            rect.switchon()
        input('hit Enter')

    def move(self):
        for rect in self._rectangles:
            rect.move(50, 50)
        input('hit Enter')

demo = Demo()
demo.draw()
demo.switchoff()
demo.switchon()
demo.move()
