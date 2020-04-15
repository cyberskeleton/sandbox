#20.14
from tkinter import *
from tkinter.messagebox import *

class DoubleList:
    def __init__(self, master, list_all):
        self.top = master
        self._list_all = list(set(list_all))
        self._list_all.sort()
        self._cancel = False
        self._make_widgets()

    def _make_widgets(self):


    def _fill_list(self, items, lst):
        lst.delete(0, END)  # очистити список на екрані
        for item in items:
            lst.insert(END, item)

    def _right_handler(self, ev=None):
        '''Обробити натиснення кнопки ">>".'''
        try:
            # отримати вибраний елемент списку
            cur_sel = self._l_all.curselection()
            elem = self._l_all.get(cur_sel)
            if not elem:
                return
            index = cur_sel[0]
            # оновити список
            self._l_all.delete(index)
            del self._list_all[index]
        except TclError:
            # пропустити помилку curselection, якщо під час
            # подвійного натиснення лівої клавіші миші список порожній
            pass
        except Exception as e:
            # якщо інша помилка, то видати повідомлення
            showwarning('Помилка', e)

    def _left_handler(self, ev=None):
        '''Обробити натиснення кнопки "<<".'''
        try:
            # отримати вибраний елемент списку
            if not elem:
                return
            index = cur_sel[0]
            # оновити список
        except TclError:
            # пропустити помилку curselection, якщо під час
            # подвійного натиснення лівої клавіші миші список порожній
            pass
        except Exception as e:
            # якщо інша помилка, то видати повідомлення
            showwarning('Помилка', e)

    def ok_handler(self, ev=None):
        '''Обробити натиснення кнопки "Ok".'''
        self.top.destroy()  # закрити вікно self.top

    def cancel_handler(self, ev=None):
        '''Обробити натиснення кнопки "Відмінити".'''
        # відмінити усі зміни
        self._cancel = True
        self.ok_handler(ev)

    def get(self):
        '''Повернути cписок вибраних елементів.

           Якщо каталог не вибрано, то повертається порожній рядок.
        '''
        return result


def main():
    '''Функція для тестування.'''
    root = Tk()
    d = DoubleList(root, 'currency.txt')
    mainloop()
    sel = d.get()

if __name__ == '__main__':
    main()
