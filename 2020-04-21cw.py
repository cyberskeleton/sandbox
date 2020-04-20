

from tkinter import *
from tkinter.messagebox import *

class Entity:
    def __init__(self, param_1='', param_2=0.0, param_3=0, param_4=99):
        self.param_1 = param_1
        self.param_2 = param_2
        self.param_3 = param_3
        self.param_4 = param_4

    def get_param_1(self):
        return self.param_2

    def set_param_1(self, param_1):
        self.param_1 = param_1

    def get_param_2(self):
        return float(self.param_2)

    def set_param_2(self, param_2):
        self.param_2 = float(param_2)
    
    def get_param_3(self):
        return int(self.param_3)

    def set_param_3(self, param_3):
        self.param_3 = int(param_3)

    def get_param_4(self):
        return int(self.param_4)

    def set_param_4(self, param_4):
        self.param_4 = int(param_4)

    def to_string(self):
        string = self.param_1 + ", " + str(self.param_2) + ", " + str(self.param_3) + ", " + str(self.param_4)
        print(string)
        return string

class Service:
    def __init__(self, filename):
        self.filename = filename

    def save(self, entity):
        f = open(self.filename, 'a')
        data = entity.to_string() + "\n"
        f.write(data)
        f.close()

    def find_all(self):
        entities = []
        f = open(self.filename, 'r')
        data = f.read().split('\n')
        if len(data) > 0:
            for entry in data:
                params = entry.split(", ")
                if len(params) == 4:
                    entity = Entity(params[0], float(params[1]), int(params[2]), int(params[3]))
                    entities.append(entity)
                    # print("Add: " + entity.to_string())
        f.close()
        return entities

    def filter_by_param_2(self, param_2):
        entities = self.find_all()
        result = []
        for entity in entities:
            if entity.get_param_2() <= float(param_2):
                result.append(entity)
        return result

    def filter_by_param_34(self, param_34):
        entities = self.find_all()
        result = []
        for entity in entities:
            if entity.get_param_3() <= int(param_34) and entity.get_param_4() >= int(param_34):
                result.append(entity)
        return result

class Controller:
    def __init__(self, root, filename):
        self.root = root
        self.service = Service(filename)
        self.txt_param_2 = "Filter by param_2:"
        self.txt_param_34 = "Filter by param_34:"
        self.txt_n_param_1 = "param_1:"
        self.txt_n_param_2 = "param_2:"
        self.txt_n_param_3 = "param_3:"
        self.txt_n_param_4 = "param_4:"

        self.default_param_2 = 999999.99 # a big number enough to show all values at start
        self.default_param_34 = -1
        self.param_2 = self.default_param_2
        self.param_34 = self.default_param_34
        self.n_param_1 = ''
        self.n_param_2 = -1.0
        self.n_param_3 = -1
        self.n_param_4 = -1

        self._load_data()
        self.__create_widgets__()

    # Graphic

    def __create_widgets__(self):
        # top frame start
        self._frame_top = Frame(self.root)
        # param_2
        self._frame_param_2 = Frame(self._frame_top)
        self._lbl_param_2 = Label(self._frame_param_2, width=16, text=self.txt_param_2, font="Arial 12")
        self._lbl_param_2.pack(side = LEFT, anchor = NW, padx = 5)
        self._entry_param_2 = Entry(self._frame_param_2, width=8, justify='right', font="Arial 12", textvariable = self.param_2)
        self._entry_param_2.pack(side = RIGHT, anchor = E, padx = 5)
        self._frame_param_2.pack(side=TOP, anchor = NW, fill=Y, expand=NO)
        # param_34
        self._frame_param_34 = Frame(self._frame_top)
        self._lbl_param_34 = Label(self._frame_param_34, width=16, text=self.txt_param_34, font="Arial 12")
        self._lbl_param_34.pack(side = LEFT, anchor = NW, padx = 5)
        self._entry_param_34 = Entry(self._frame_param_34, width=8, justify='right', font="Arial 12", textvariable = self.param_34)
        self._entry_param_34.pack(side = RIGHT, anchor = E, padx = 5)
        self._frame_param_34.pack(side=TOP, anchor = SW, fill=Y, expand=NO)

        self._btn_ok = Button(self._frame_top, width=8, justify='center', text='Filter', command=self.filter_entities)
        self._btn_ok.pack(side=TOP, anchor = NE, padx=5, pady=5)

        # new
        self._frame_new = Frame(self._frame_top)

        self._frame_n_param_1 = Frame(self._frame_new)
        self._lbl_n_param_1 = Label(self._frame_n_param_1, width=12, text=self.txt_n_param_1, font="Arial 12")
        self._lbl_n_param_1.pack(side = LEFT, anchor = W, padx = 5)
        self._entry_n_param_1 = Entry(self._frame_n_param_1, width=12, justify='right', font="Arial 12", textvariable = self.n_param_1)
        self._entry_n_param_1.pack(side = RIGHT, anchor = E, padx = 5)
        self._frame_n_param_1.pack(side=TOP, fill=Y, expand=NO)

        self._frame_n_param_2 = Frame(self._frame_new)
        self._lbl_n_param_2 = Label(self._frame_n_param_2, width=16, text=self.txt_n_param_2, font="Arial 12")
        self._lbl_n_param_2.pack(side = LEFT, anchor = W, padx = 5)
        self._entry_n_param_2 = Entry(self._frame_n_param_2, width=8, justify='right', font="Arial 12", textvariable = self.n_param_2)
        self._entry_n_param_2.pack(side = RIGHT, anchor = E, padx = 5)
        self._frame_n_param_2.pack(side=TOP, fill=Y, expand=NO)

        self._frame_n_param_3 = Frame(self._frame_new)
        self._lbl_n_param_3 = Label(self._frame_n_param_3, width=16, text=self.txt_n_param_3, font="Arial 12")
        self._lbl_n_param_3.pack(side = LEFT, anchor = W, padx = 5)
        self._entry_n_param_3 = Entry(self._frame_n_param_3, width=8, justify='right', font="Arial 12", textvariable = self.n_param_3)
        self._entry_n_param_3.pack(side = RIGHT, anchor = E, padx = 5)
        self._frame_n_param_3.pack(side=TOP, fill=Y, expand=NO)

        self._frame_n_param_4 = Frame(self._frame_new)
        self._lbl_n_param_4 = Label(self._frame_n_param_4, width=16, text=self.txt_n_param_4, font="Arial 12")
        self._lbl_n_param_4.pack(side = LEFT, anchor = W, padx = 5)
        self._entry_n_param_4 = Entry(self._frame_n_param_4, width=8, justify='right', font="Arial 12", textvariable = self.n_param_4)
        self._entry_n_param_4.pack(side = RIGHT, anchor = E, padx = 5)
        self._frame_n_param_4.pack(side=TOP, fill=Y, expand=NO)

        self._frame_new.pack(side=TOP, fill=Y, expand=NO)

        self._btn_cancel = Button(self._frame_top, width=8, justify='center', text='Add new', command=self.add_entity)
        self._btn_cancel.pack(side=BOTTOM, anchor = SE, padx=5, pady=5)

        self._frame_top.pack(side=TOP, fill=Y, expand=NO)
        # top frame end

        # bottom frame start
        self._frame_bottom = Frame(self.root)
        self._sbar_entities = Scrollbar(self._frame_bottom)
        self._sbar_entities.pack(side=RIGHT, fill=Y)
        self._lbox_entities = Listbox(self._frame_bottom, height=12, width=30, yscrollcommand=self._sbar_entities.set)
        self._sbar_entities.config(command=self._lbox_entities.yview)
        self._lbox_entities.pack(side=RIGHT, fill=BOTH, expand=YES)
        self._frame_bottom.pack(side=BOTTOM, fill=Y, expand=YES)
        # bottom frame end

        # service
        self._fill_list(self._list_entities, self._lbox_entities)

    def _fill_list(self, items, lst):
        lst.delete(0, END)
        for item in items:
            string = item.to_string()
            lst.insert(END, string)

    def filter_entities(self):
        try:
            entry_param_2 = self._entry_param_2.get()
            entry_param_34 = self._entry_param_34.get()
            if entry_param_2 == '':
                entry_param_2 = self.default_param_2
            if entry_param_34 == '':
                entry_param_34 = self.default_param_34
            self.param_2 = float(entry_param_2)
            self.param_34 = int(entry_param_34)
            self._load_data()
            self._fill_list(self._list_entities, self._lbox_entities)
        except Exception as e:
            showwarning('Error:', e)

    def add_entity(self):
        try:
            entry_param_1 = self._entry_n_param_1.get()
            if entry_param_1 == '':
                showwarning(message='Enter param_1!')
                return
            entry_param_2 = self._entry_n_param_2.get()
            if entry_param_2 == '' or float(entry_param_2) <= 0.0:
                showwarning(message='param_2 must by more that 0.0!')
                return
            entry_param_3 = self._entry_n_param_3.get()
            entry_param_4 = self._entry_n_param_4.get()
            if entry_param_3 == '' or int(entry_param_3) < 0 or \
                    entry_param_4 == '' or int(entry_param_4) < 0:
                showwarning(message='param_34 must be 0 or above!')
                return
            self.n_param_1 = entry_param_1
            self.n_param_2 = float(entry_param_2)
            self.n_param_3 = int(entry_param_3)
            self.n_param_4 = int(entry_param_4)
            entity = Entity(self.n_param_1, self.n_param_2, self.n_param_3, self.n_param_4)
            print(entity.to_string())
            self.service.save(entity)
            self._load_data()
            self._fill_list(self._list_entities, self._lbox_entities)
        except Exception as e:
            showwarning('Error:', e)

    # Service
    def _load_data(self):
        self._list_entities = self.find_entities()

    def find_entities(self):
        if self.param_2 == self.default_param_2:
            by_param_2 = self.service.find_all()
        else:
            by_param_2 = self.service.filter_by_param_2(self.param_2)
        if self.param_34 == self.default_param_34:
            return by_param_2
        else:
            by_param_34 = self.service.filter_by_param_34(self.param_34)
            return list(set(by_param_2) and set(by_param_34))

def main():
    root = Tk()
    d = Controller(root, 'test_file.txt')
    mainloop()

if __name__ == '__main__':
    main()
