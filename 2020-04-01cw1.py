import turtle as t
from abc import ABCMeta, abstractmethod
turtle = t.Turtle()
window = t.Screen()

class Drawable(metaclass = ABCMeta):
    """Абстрактний клас для зображення точок та кіл заданих розмірів та кольору"""
    @property
    @abstractmethod
    def color(self):
        """Властивість, що повертає/встановлює колір переднього плану."""
        pass

    @color.setter
    @abstractmethod
    def color(self, cl):
        pass

    @property
    @abstractmethod
    def bgcolor(self):
        """Властивість, що повертає/встановлює колір фону."""
        pass

    @bgcolor.setter
    @abstractmethod
    def bgcolor(self, cl):
        pass

    @abstractmethod
    def draw_point(self, x, y, cl):
        """Зобразити точку з координатами x, y кольором cl."""
        pass

    @abstractmethod
    def draw_circle(self, x, y, r, cl):
        """Зобразити коло з координатами цнтру x, y радіусом r кольором cl."""
        pass

    @abstractmethod
    def draw_rectangle(self, x, y, height, width, cl):
        pass

    @abstractmethod
    def onscreenclick(self, fun):
        pass

    @abstractmethod
    def mainloop(self):
        pass

class TurtleDraw(Drawable):
    """
    Клас для зображення точок та кіл заданих розмірів та кольору.
    TurtleDraw є нащадком абстрактного класу Drawable та використовує засоби
    роботи з графікою з модуля turtle.
    """
    def __init__(self, tile_size):
        pause = 50
        turtle.up()
        turtle.home()
        turtle.speed(1000)
        window.setup(tile_size * 3, tile_size * 3)

    @property
    def color(self):
        """Властивість, що повертає/встановлює колір переднього плану."""
        return turtle.pencolor()

    @color.setter
    def color(self, cl):
        turtle.pencolor(cl)

    @property
    def bgcolor(self):
        """Властивість, що повертає/встановлює колір фону."""
        return t.bgcolor()

    @bgcolor.setter
    def bgcolor(self, cl):
       t.bgcolor(cl)

    def draw_point(self, x, y, cl):
        """Зобразити точку з координатами x, y кольором cl."""
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        turtle.dot(cl)

    def draw_circle(self, x, y, r, cl):
       """Зобразити коло з координатами цнтру x, y радіусом r кольором cl."""
       c = self.color
       self.color = cl
       turtle.up()
       turtle.setpos(x + r, y) #малює починаючи знизу кола
       turtle.down()
       turtle.circle(r)
       self.color = c

    def draw_rectangle(self, x, y, height, width, cl):
        c = self.color
        self.color = cl
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        turtle.setheading(0)
        turtle.forward(height)
        turtle.setheading(270)
        turtle.forward(width)
        turtle.setheading(180)
        turtle.forward(height)
        turtle.setheading(90)
        turtle.forward(width)
        self.color = c

    def onscreenclick(self, fun):
        t.onscreenclick(fun)

    def mainloop(self):
        t.mainloop()

class CharDraw(Drawable):
    def __init__(self, tile_size):
        pause = 50
        window.setup(0, 0)
        self.tile_size = tile_size

    @property
    def color(self):
        pass

    @color.setter
    def color(self, cl):
        pass

    @property
    def bgcolor(self):
        pass

    @bgcolor.setter
    def bgcolor(self, cl):
        pass

    def draw_point(self, x, y, cl):
        pass

    def draw_circle(self, x, y, r, cl):
        pass

    def draw_rectangle(self, x, y, height, width, cl):
        pass

    def onscreenclick(self, fun):
        board = [[0,0,0],[0,0,0],[0,0,0]]
        while board != ([[1,1,1],[1,1,1],[1,1,1]] or [[2,2,2],[2,2,2],[2,2,2]]):
            coords = [-1, -1]
            while coords[0] < 0 or coords[0] > 2 or coords[1] < 0 or coords[1] > 2:
                coords[0] = int(input('Input col (0/1/2): '))
                coords[1] = int(input('Input row (0/1/2): '))
            y = coords[0] * self.tile_size - tile_size
            x = coords[1] * self.tile_size - tile_size
            board = fun(x, y)
            for i in range(0, 3):
                position = ["[ ]","[ ]","[ ]"]
                for j in range(0, 3):
                    if board[i][j] == 1:
                        position[j] = "[X]"
                    elif board[i][j] == 2:
                        position[j] = "[O]"
                print(position[0],position[1],position[2])
        return

    def mainloop(self):
        print("=== That's all folks! ===")

class TickTackToe(Drawable):
    def __init__(self, drawable, tile_size, color, bgcolor, sign_size):
        self.drawable = drawable
        self.tile_size = tile_size
        self.color = color
        self.bgcolor = bgcolor
        self.sign_size = sign_size
        self.drawable.__setattr__('bgcolor', bgcolor)
        self.turn = 0
        self.board = [[0,0,0],[0,0,0],[0,0,0]]

    def bgcolor(self):
        self.drawable.bgcolor(self.bgcolor)

    def color(self):
        self.drawable.color(self.color)

    def draw_circle(self, x, y, r, cl):
        self.color = cl
        self.sign_size = r
        self.drawable.draw_circle(x, y, self.sign_size, self.color)

    def draw_point(self, x, y, cl):
        self.color = cl
        self.drawable.draw_point(x, y, self.color)

    def draw_rectangle(self, x, y, height, width, cl):
        self.color = cl
        self.drawable.draw_rectangle(self, x, y, height, width, cl)

    def onscreenclick(self, fun):
        self.drawable.onscreenclick(fun)

    def mainloop(self):
        self.drawable.mainloop()

    def draw_board(self):
        # turtle.showturtle()
        for i in range(0, 3):
            for j in range(0, 3):
                x = i * self.tile_size - self.tile_size * 1.5
                y = j * self.tile_size - self.tile_size * 0.5
                self.drawable.draw_rectangle(x, y, self.tile_size, self.tile_size, self.color)

    def main(self):
        self.drawable.onscreenclick(self.check_move)
        self.drawable.mainloop()

    def check_move(self, x, y):
        player = self.is_moved(x, y)
        if player != 0 and self.is_finished(player):
            print("GAME OVER !!! PLAYER", player, 'WON !!!')
            self.board = [[player,player,player],[player,player,player],[player,player,player]]
        return self.board

    def is_finished(self, player):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player or \
                self.board[2][0] == self.board[1][1] == self.board[0][2] == player:
            return True
        for i in range(0, 2):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player or \
                    self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
        return False

    def is_moved(self, x, y):
        if x < self.tile_size * -0.5 and x > self.tile_size * -1.5:
            col = 0
        elif x > self.tile_size * 0.5 and x < self.tile_size * 1.5:
            col = 2
        elif x >= self.tile_size * -0.5 and x <= self.tile_size * 0.5:
            col = 1
        else:
            return 0
        if y < self.tile_size * -0.5 and y > self.tile_size * -1.5:
            row = 0
        elif y > self.tile_size * 0.5 and y < self.tile_size * 1.5:
            row = 2
        elif y >= self.tile_size * -0.5 and y <= self.tile_size * 0.5:
            row = 1
        else:
            return 0
        if self.board[col][row] == 0:
            player = self.turn % 2 + 1
            self.board[col][row] = player
            self.turn += 1

            put_x = col * self.tile_size - self.tile_size
            put_y = row * self.tile_size - self.tile_size
            if player == 1:
                self.draw_point(put_x, put_y, self.color)
            else:
                self.draw_circle(put_x, put_y, self.sign_size, self.color)
            return player
        return 0

tile_size = 100
#drawable = TurtleDraw(tile_size)
drawable = CharDraw(tile_size)
ttt = TickTackToe(drawable, tile_size, 'black', 'lightblue', 10)
ttt.draw_board()
ttt.main()
