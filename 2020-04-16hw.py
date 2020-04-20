# T20.11 Скласти програму з графічним інтерфейсом для розв’язання задачі.
# Дано файл, який містить відомості про іграшки: вказується назва іграшки
# (наприклад: м’яч, лялька, конструктор і т.д.), її вартість в гривнях та вікові
# границі дітей, для яких іграшка призначається (наприклад, для дітей від двох
# до п’яти років). Підібрати усі іграшки за заданим віком дитини та/або
# обмеженням вартості.
# Вводити відомості про іграшки треба у окремому вікні. У головному вікні
# вводити обмеження та показувати відібрані іграшки у віджеті список.

from tkinter import *
from tkinter.messagebox import *

class Toy:
    def __init__(self, name='', price=0.0, age_min=0, age_max=99):
        self.name = name
        self.price = price
        self.age_min = age_min
        self.age_max = age_max

    def get_name(self):
        return self.price

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return float(self.price)

    def set_price(self, price):
        self.price = float(price)
    
    def get_age_min(self):
        return int(self.age_min)

    def set_age_min(self, age_min):
        self.age_min = int(age_min)

    def get_age_max(self):
        return int(self.age_max)

    def set_age_max(self, age_max):
        self.age_max = int(age_max)

    def to_string(self):
        string = self.name + ", " + str(self.price) + ", " + str(self.age_min) + ", " + str(self.age_max)
        print(string)
        return string

class Service:
    def __init__(self, filename):
        self.filename = filename

    def save(self, toy):
        f = open(self.filename, 'a')
        data = toy.to_string() + "\n"
        f.write(data)
        f.close()

    def find_all(self):
        toys = []
        f = open(self.filename, 'r')
        data = f.read().split('\n')
        if len(data) > 0:
            for entry in data:
                params = entry.split(", ")
                if len(params) == 4:
                    toy = Toy(params[0], float(params[1]), int(params[2]), int(params[3]))
                    toys.append(toy)
                    # print("Add: " + toy.to_string())
        f.close()
        return toys

    def filter_by_price(self, price):
        toys = self.find_all()
        result = []
        for toy in toys:
            if toy.get_price() <= float(price):
                result.append(toy)
        return result

    def filter_by_age(self, age):
        toys = self.find_all()
        result = []
        for toy in toys:
            if toy.get_age_min() <= int(age) and toy.get_age_max() >= int(age):
                result.append(toy)
        return result

class Controller:
    def __init__(self, root, filename):
        self.root = root
        self.service = Service(filename)
        self.txt_price = "Filter by PRICE:"
        self.txt_age = "Filter by AGE:"
        self.txt_n_descript = "Description:"
        self.txt_n_price = "Price:"
        self.txt_n_min_age = "Min age:"
        self.txt_n_max_age = "Max age:"

        self.default_price = 999999.99 # a big number enough to show all values at start
        self.default_age = -1
        self.price = self.default_price
        self.age = self.default_age
        self.n_descript = ''
        self.n_price = -1.0
        self.n_min_age = -1
        self.n_max_age = -1

        self._load_data()
        self.__create_widgets__()

    # Graphic

    def __create_widgets__(self):
        # top frame start
        self._frame_top = Frame(self.root)
        # price
        self._frame_price = Frame(self._frame_top)
        self._lbl_price = Label(self._frame_price, width=16, text=self.txt_price, font="Arial 12")
        self._lbl_price.pack(side = LEFT, anchor = NW, padx = 5)
        self._entry_price = Entry(self._frame_price, width=8, justify='right', font="Arial 12", textvariable = self.price)
        self._entry_price.pack(side = RIGHT, anchor = E, padx = 5)
        self._frame_price.pack(side=TOP, anchor = NW, fill=Y, expand=NO)
        # age
        self._frame_age = Frame(self._frame_top)
        self._lbl_age = Label(self._frame_age, width=16, text=self.txt_age, font="Arial 12")
        self._lbl_age.pack(side = LEFT, anchor = NW, padx = 5)
        self._entry_age = Entry(self._frame_age, width=8, justify='right', font="Arial 12", textvariable = self.age)
        self._entry_age.pack(side = RIGHT, anchor = E, padx = 5)
        self._frame_age.pack(side=TOP, anchor = SW, fill=Y, expand=NO)

        self._btn_ok = Button(self._frame_top, width=8, justify='center', text='Filter', command=self.filter_toys)
        self._btn_ok.pack(side=TOP, anchor = NE, padx=5, pady=5)

        # new
        self._frame_new = Frame(self._frame_top)

        self._frame_n_descript = Frame(self._frame_new)
        self._lbl_n_descript = Label(self._frame_n_descript, width=12, text=self.txt_n_descript, font="Arial 12")
        self._lbl_n_descript.pack(side = LEFT, anchor = W, padx = 5)
        self._entry_n_descript = Entry(self._frame_n_descript, width=12, justify='right', font="Arial 12", textvariable = self.n_descript)
        self._entry_n_descript.pack(side = RIGHT, anchor = E, padx = 5)
        self._frame_n_descript.pack(side=TOP, fill=Y, expand=NO)

        self._frame_n_price = Frame(self._frame_new)
        self._lbl_n_price = Label(self._frame_n_price, width=16, text=self.txt_n_price, font="Arial 12")
        self._lbl_n_price.pack(side = LEFT, anchor = W, padx = 5)
        self._entry_n_price = Entry(self._frame_n_price, width=8, justify='right', font="Arial 12", textvariable = self.n_price)
        self._entry_n_price.pack(side = RIGHT, anchor = E, padx = 5)
        self._frame_n_price.pack(side=TOP, fill=Y, expand=NO)

        self._frame_n_min_age = Frame(self._frame_new)
        self._lbl_n_min_age = Label(self._frame_n_min_age, width=16, text=self.txt_n_min_age, font="Arial 12")
        self._lbl_n_min_age.pack(side = LEFT, anchor = W, padx = 5)
        self._entry_n_min_age = Entry(self._frame_n_min_age, width=8, justify='right', font="Arial 12", textvariable = self.n_min_age)
        self._entry_n_min_age.pack(side = RIGHT, anchor = E, padx = 5)
        self._frame_n_min_age.pack(side=TOP, fill=Y, expand=NO)

        self._frame_n_max_age = Frame(self._frame_new)
        self._lbl_n_max_age = Label(self._frame_n_max_age, width=16, text=self.txt_n_max_age, font="Arial 12")
        self._lbl_n_max_age.pack(side = LEFT, anchor = W, padx = 5)
        self._entry_n_max_age = Entry(self._frame_n_max_age, width=8, justify='right', font="Arial 12", textvariable = self.n_max_age)
        self._entry_n_max_age.pack(side = RIGHT, anchor = E, padx = 5)
        self._frame_n_max_age.pack(side=TOP, fill=Y, expand=NO)

        self._frame_new.pack(side=TOP, fill=Y, expand=NO)

        self._btn_cancel = Button(self._frame_top, width=8, justify='center', text='Add new', command=self.add_toy)
        self._btn_cancel.pack(side=BOTTOM, anchor = SE, padx=5, pady=5)

        self._frame_top.pack(side=TOP, fill=Y, expand=NO)
        # top frame end

        # bottom frame start
        self._frame_bottom = Frame(self.root)
        self._sbar_toys = Scrollbar(self._frame_bottom)
        self._sbar_toys.pack(side=RIGHT, fill=Y)
        self._lbox_toys = Listbox(self._frame_bottom, height=12, width=30, yscrollcommand=self._sbar_toys.set)
        self._sbar_toys.config(command=self._lbox_toys.yview)
        self._lbox_toys.pack(side=RIGHT, fill=BOTH, expand=YES)
        self._frame_bottom.pack(side=BOTTOM, fill=Y, expand=YES)
        # bottom frame end

        # service
        self._fill_list(self._list_toys, self._lbox_toys)

    def _fill_list(self, items, lst):
        lst.delete(0, END)
        for item in items:
            string = item.to_string()
            lst.insert(END, string)

    def filter_toys(self):
        try:
            entry_price = self._entry_price.get()
            entry_age = self._entry_age.get()
            if entry_price == '':
                entry_price = self.default_price
            if entry_age == '':
                entry_age = self.default_age
            self.price = float(entry_price)
            self.age = int(entry_age)
            self._load_data()
            self._fill_list(self._list_toys, self._lbox_toys)
        except Exception as e:
            showwarning('Error:', e)

    def add_toy(self):
        try:
            entry_descript = self._entry_n_descript.get()
            if entry_descript == '':
                showwarning(message='Enter description!')
                return
            entry_price = self._entry_n_price.get()
            if entry_price == '' or float(entry_price) <= 0.0:
                showwarning(message='Price must by more that 0.0!')
                return
            entry_min_age = self._entry_n_min_age.get()
            entry_max_age = self._entry_n_max_age.get()
            if entry_min_age == '' or int(entry_min_age) < 0 or entry_max_age == '' or int(entry_max_age) < 0:
                showwarning(message='Age must be 0 or above!')
                return
            self.n_descript = entry_descript
            self.n_price = float(entry_price)
            self.n_min_age = int(entry_min_age)
            self.n_max_age = int(entry_max_age)
            toy = Toy(self.n_descript, self.n_price, self.n_min_age, self.n_max_age)
            print(toy.to_string())
            self.service.save(toy)
            self._load_data()
            self._fill_list(self._list_toys, self._lbox_toys)
        except Exception as e:
            showwarning('Error:', e)

    # Service
    def _load_data(self):
        self._list_toys = self.find_toys()

    def find_toys(self):
        if self.price == self.default_price:
            by_price = self.service.find_all()
        else:
            by_price = self.service.filter_by_price(self.price)
        if self.age == self.default_age:
            return by_price
        else:
            by_age = self.service.filter_by_age(self.age)
            return list(set(by_price) and set(by_age))

def main():
    root = Tk()
    d = Controller(root, 'toy_store.txt')
    mainloop()

if __name__ == '__main__':
    main()
