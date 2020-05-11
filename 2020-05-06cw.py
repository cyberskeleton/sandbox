# t24_41_grid_canvas.pyw
# Клас GridCanvas для зображення поля у клітинку заданого розміру rows x cols

from tkinter import *

class GridCanvas(Canvas):
    '''Клас для зображення поля у клітинку заданого розміру rows x cols.

       Клас є нащадком Canvas.
       self.rows - кільксть рядків поля
       self.cols - кількість стовпчиків поля
       self.selection_handler - функція, що буде викликатись при виборі
                                клітинки поля
       self.bordercolor - колір границі між клітинками
       self.evenbg - колір заповнення клітинок з парними номерами
                      (якщо відрізняється для парних та непарних номерів).
                      Перша клітинка має номер 0
       self.highlightbg - колір заповнення вибраної клітинки
       self.ratio - відсоток заповнення площі клітинки зв'язаним об'єктом
       self.cellwidth - ширина клітинки
       self.cellheight - висота клітинки
       self.grid - матриця, що складається зі зв'язаних об'єктів
                    для всіх клітинок. Якщо до клітинки не први'язано
                    об'єкт, то значення відповідного елемента - None.
       self.moved - змінна tkinter для контролю завершення переміщення
    '''

    def __init__(self, master, rows, cols, selection_handler, *args,
                 bordercolor='black', evenbg='', ratio=0.85,
                 highlightbg='green', **kwargs):
        Canvas.__init__(self, master, *args, **kwargs)
        self.rows = rows
        self.cols = cols
        self.selection_handler = selection_handler
        self.bordercolor = bordercolor
        self.evenbg = evenbg
        self.highlightbg = highlightbg
        self.ratio = ratio
        self.cellwidth = int(self['width']) // self.cols
        self.cellheight = int(self['height']) // self.rows
        # заповнити матрицю зв'язаних об'єктів значенням None
        self.grid = []
        for row in range(rows):
            self.grid.append([])
            for col in range(cols):
                self.grid[row].append(None)
        # зобразити поле
        self._drawgrid()
        # прив'язати подію натиснення лівої клавіші миші над клітинкою поля
        self.bind('<Button-1>', self.on_click)
        self.moved = IntVar()
        self.moved.set(1)

    def _tagstr(self, row, col):
        '''Побудувати рядок з тегом для клітинки (row, col).

           Наприклад: 't001002'
        '''
        return 't{:0>3}{:0>3}'.format(row, col)

    def _drawgrid(self):
        '''Зобразити поле з прямокутників.
        '''
        for row in range(self.rows):
            for col in range(self.cols):
                # визначити границі прямокутника
                # для клітинки (row, col)
                xstart = col * self.cellwidth
                ystart = row * self.cellheight
                xend = xstart + self.cellwidth + 1
                yend = ystart + self.cellheight + 1
                # визначити колір заповнення
                if self.evenbg and (row + col) % 2 == 0:
                    bg = self.evenbg
                else:
                    bg = self['bg']
                # зобразити прямокутник та встановити його тег
                self.create_rectangle(xstart, ystart, xend, yend,
                                      width=self['bd'], fill=bg,
                                      outline=self.bordercolor,
                                      tags=self._tagstr(row, col))

    def create_bound(self, row, col, obj, fill='black', outline='white',
                     **features):
        '''Створити та зобразити зв'язаний об'єкт для row, col.

           obj - об'єкт, що буде зображено
           fill, outline - кольори заповнення та границі
           features - додаткові характеристики об'єкту
        '''
        self.grid[row][col].draw(self.cellwidth,
                                 self.cellheight, self.ratio)

    def delete_bound(self, row, col):
        '''Видалити зв'язаний об'єкт для row, col.'''
        bo = self.grid[row][col]
        if bo:
            self.delete(bo.id)
            self.grid[row][col] = None

    def _movestep(self, id, ddx, ddy, xfinal, yfinal):
        '''Зробити 1 крок для "повільного" пересування об'єкту.

           id - номер об'єкту,
           ddx, ddy - кроки по x, y,
           xfinal, yfinal - кінцеві координати лівого верхнього кута
        '''
        x, y, mx, my = self.coords(id)  # отримати поточні координати
        # обчислити нові значення ddx, ddy
        if x == xfinal:
            ddx = 0
        if y == yfinal:
            ddy = 0
        if ddx or ddy:  # якщо не дійшли до кінця
            self.move(id, ddx, ddy)  # перемістити об'єкт
            # встановити виклик переміщення на наступний крок
            # через 5 мілісекунд
            self.after(5, self._movestep, id, ddx, ddy, xfinal, yfinal)
        else:
            # змінити self.moved, щоб зафіксувати завершення переміщення
            self.moved.set(1)

    def move_bound(self, fromrow, fromcol, torow, tocol, slow=False):
        '''Пересування об'єкту.

           fromrow, fromcol - початкова клітинка,
           torow, tocol - кінцева клітинка,
           slow - пересувати повільно
        '''
        # визначити зсув по x, y
        dx = (tocol - fromcol) * self.cellwidth
        dy = (torow - fromrow) * self.cellheight
        bo = self.grid[fromrow][fromcol]  # отримати зв'язаний об'єкт
        if bo and (dx != 0 or dy != 0):  # є що і куди переміщувати
            if slow:  # якщо пересувати повільно
                # встановити зсув на 1 крок рівним 1, 0 або -1
                # у залежності від dx, dy
                ddx = _sign(dx)
                ddy = _sign(dy)
                # обчислити фінальні координати
                xfinal = tocol * self.cellwidth + \
                         int(self.cellwidth * (1 - self.ratio) / 2)
                yfinal = torow * self.cellheight + \
                         int(self.cellheight * (1 - self.ratio) / 2)
                # запустити анімацію пересування
                self.moved.set(0)
                self._movestep(bo.id, ddx, ddy, xfinal, yfinal)
                # очікувати зміни значення self.moved
                self.wait_variable(self.moved)
            else:
                # пересунути одразу на dx, dy
                self.move(bo.id, dx, dy)
            # переприв'язати об'єкт
            self.grid[fromrow][fromcol] = None
            self.grid[torow][tocol] = bo

    def select_cell(self, row, col):
        '''Вибрати (підсвітити) клітинку row, col.'''
        self.itemconfigure(self._tagstr(row, col), fill=self.highlightbg)

    #def deselect_cell(self, row, col):
        #'''Зняти вибір (підсвітчення) клітинки row, col.'''
        #if self.evenbg and (row + col) % 2 == 0:
            #bg = self.evenbg
        #else:
            #bg = self['bg']
        #self.itemconfigure(self._tagstr(row, col), fill=bg)

    def on_click(self, ev):
        '''Обробка натиснення лівої клавіші миші.'''
        # дозволити обробку подій тільки коли об'єкт не переміщується
        if self.moved.get():
            # визначити клітинку, де знаходиться миша
            x = self.canvasx(ev.x)  # перевести координати вікна
            y = self.canvasy(ev.y)  # у координати canvas
            row = min(int(y) // self.cellheight, self.rows - 1)
            col = min(int(x) // self.cellwidth, self.cols - 1)
            # викликати функцію обробки вибору клітинки
            self.selection_handler(self, row, col)


def _sign(val):
    "signum(val)"
    if val > 0:
        sign = 1
    elif val == 0:
        sign = 0
    else:
        sign = -1
    return sign


# тест модуля
lastrow = 6
lastcol = 6


def sel_handler(gc, row, col):
    '''Приклад функції обробки вибору клітинки.'''
    global lastrow, lastcol
    #gc.deselect_cell(lastrow, lastcol)
    gc.move_bound(lastrow, lastcol, row, col, slow=True)
    gc.select_cell(row, col)
    lastrow = row
    lastcol = col


def main():
    '''Функція для тестування.

       Працює, коли модуль є головним
    '''
    top = Tk()
    gc = GridCanvas(top, 8, 8, sel_handler, bordercolor='grey',
                    evenbg='white',
                    width=350, height=350, bg='white', bd=2)
    gc.pack()

    mainloop()


if __name__ == '__main__':
    main()
