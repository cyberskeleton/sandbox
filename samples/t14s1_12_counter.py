#T14s1_12
#Лічилка з використанням черги

from t14s1_11_queue import *

class Player:
    '''Реалізує клас Гравець

    n - номер гравця
    '''
    def __init__(self, n):
        self.n = n

    def show(self):
        print(self.n)

def count_counter():
    '''Функція розв'язує задачу "лічилка"
    '''
    q = Queue()                                 #створити чергу q
    n = int(input('Кількість гравців: '))
    m = int(input('Кількість слів: '))

    for i in range(n):
        pl = Player(i+1)                        #створити гравця з номером на 1 більше i
        q.add(pl)                               #додати гравця до кінця черги

    print('\nПослідовність номерів, що вибувають')
    while not q.isempty():
        for i in range(m-1):                    #m-1 раз перекласти гравця з початку до кінця черги
            q.add(q.take())
        pl = q.take()                           #узяти m-го гравця з початку черги
        pl.show()                               #та показати його номер

#оформили розв'язок задачі окремою функцією, щоб показати, коли викликається
#деструктор для об'єкту q
count_counter()