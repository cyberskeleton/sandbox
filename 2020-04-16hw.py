# T20.11 Скласти програму з графічним інтерфейсом для розв’язання задачі.
# Дано файл, який містить відомості про іграшки: вказується назва іграшки
# (наприклад: м’яч, лялька, конструктор і т.д.), її вартість в гривнях та вікові
# границі дітей, для яких іграшка призначається (наприклад, для дітей від двох
# до п’яти років). Підібрати усі іграшки за заданим віком дитини та/або
# обмеженням вартості.
# Вводити відомості про іграшки треба у окремому вікні. У головному вікні
# вводити обмеження та показувати відібрані іграшки у віджеті список.

from tkinter import *

root = Tk()

class Toy:
    def __init__(self, name, price, age_min, age_max):
        self.name = name
        self.price = price
        self.age_min = age_min
        self.age_max = age_max

    def get_name(self):
        return self.price

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price
    
    def get_age_min(self):
        return self.age_min

    def set_age_min(self, age_min):
        self.age_min = age_min

    def get_age_max(self):
        return self.age_max

    def set_age_max(self, age_max):
        self.age_max = age_max

    def print(self):
        print(self.name + ", " + self.price + ", " + self.age_min + ", " + self.age_max)

class Service:
    def __init__(self, filename):
        self.filename = filename

    def save(self, toy):
        f = open(self.filename, 'a')
        data = toy.get_name() + ", " + \
               toy.get_price() + ", " + \
               toy.get_age_min() + ", " + \
               toy.get_age_max() + "\n"
        f.write(data)

    def find_all(self):
        toys = []
        f = open(self.filename, 'r')
        data = f.read().split('\n')
        for entry in data:
            params = entry.split(", ")
            toys.append(Toy(params[0], params[1], params[2], params[3]))
        return toys

    def filter_by_price(self, price):
        toys = self.find_all()
        result = []
        for toy in toys:
            if toy.get_price() <= price:
                result.append(toy)
        return result

    def filter_by_age(self, age):
        toys = self.find_all()
        result = []
        for toy in toys:
            if toy.get_age_min() <= age and toy.get_age_max() >= age:
                result.append(toy)
        return result

class Controller:
    def __init__(self, root, filename):
        self.root = root
        self.service = Service(filename)

    def __create_widgets__(self):
        # 2020-04-15
        self._frame_main = Frame(self.root)

    def enter_toy(self):
        toy = Toy("name", 22, 1, 5)
        self.service.save(toy)

    def find_toys(self):
        price = 100
        age = 3
        by_price = self.service.filter_by_price(price)
        by_age = self.service.filter_by_age(age)
        return list(set(by_price) and set(by_age))
