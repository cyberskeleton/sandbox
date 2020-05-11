
from tkinter import *
from tkinter.messagebox import *

class WrongBracketsException(Exception):
    def __str__(self):
     print('Wrong brackets! ')

def check_brackets(func):
    def do_it(*args, **kwargs):
        opener = input('input open ')
        closer = input('input closer ')
        f = func(*args, **kwargs)
        stack = []
        open_list = ['(', '[', opener]
        close_list = [')', ']', closer]
        for line in f:
            for i in line:
                if i in open_list:
                    stack.append(i)
                elif i in close_list:
                    pos = close_list.index(i)
                    if ((len(stack) > 0) and
                        (open_list[pos] == stack[len(stack)-1])):
                        stack.pop()
                    else:
                        raise WrongBracketsException
            if len(stack) == 0:
                print('all good')
    return do_it



class Service:
    @check_brackets
    def find_all(self, filename):
        f = open(filename, 'r')
        data = f.read()
        f.close()
        return data

class Controller:
    def __init__(self, root):
        self.root = root
        self.service = Service()

        self.txt_n_param_1 = "filename:"
        self.txt_n_param_2 = "left parenthesis:"
        self.txt_n_param_3 = "right parenthesis:"

        self.n_filename = 'test_file.txt'
        self.n_left = ''
        self.n_right = ''

        self._load_data()
        self.__create_widgets__()

    # Graphic

    def __create_widgets__(self):
        # top frame start
        self._frame_top = Frame(self.root)

        self._frame_new = Frame(self._frame_top)

        self._frame_n_param_1 = Frame(self._frame_new)
        self._lbl_n_param_1 = Label(self._frame_n_param_1, width=12, text=self.txt_n_param_1, font="Arial 12")
        self._lbl_n_param_1.pack(side = LEFT, anchor = W, padx = 5)
        self._entry_n_param_1 = Entry(self._frame_n_param_1, width=12, justify='right', font="Arial 12", textvariable = self.n_filename)
        self._entry_n_param_1.pack(side = RIGHT, anchor = E, padx = 5)
        self._frame_n_param_1.pack(side=TOP, fill=Y, expand=NO)

        self._frame_n_param_2 = Frame(self._frame_new)
        self._lbl_n_param_2 = Label(self._frame_n_param_2, width=16, text=self.txt_n_param_2, font="Arial 12")
        self._lbl_n_param_2.pack(side = LEFT, anchor = W, padx = 5)
        self._entry_n_param_2 = Entry(self._frame_n_param_2, width=8, justify='right', font="Arial 12", textvariable = self.n_left)
        self._entry_n_param_2.pack(side = RIGHT, anchor = E, padx = 5)
        self._frame_n_param_2.pack(side=TOP, fill=Y, expand=NO)

        self._frame_n_param_3 = Frame(self._frame_new)
        self._lbl_n_param_3 = Label(self._frame_n_param_3, width=16, text=self.txt_n_param_3, font="Arial 12")
        self._lbl_n_param_3.pack(side = LEFT, anchor = W, padx = 5)
        self._entry_n_param_3 = Entry(self._frame_n_param_3, width=8, justify='right', font="Arial 12", textvariable = self.n_right)
        self._entry_n_param_3.pack(side = RIGHT, anchor = E, padx = 5)
        self._frame_n_param_3.pack(side=TOP, fill=Y, expand=NO)

        self._frame_new.pack(side=TOP, fill=Y, expand=NO)

        self._btn_cancel = Button(self._frame_top, width=8, justify='center', text='Check text', command=self.check_text)
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

    def check_text(self):
        try:
            entry_param_1 = self._entry_n_param_1.get()
            if entry_param_1 == '':
                showwarning(message='filename required!')
                return
            entry_param_2 = self._entry_n_param_2.get()
            if entry_param_2 == '':
                showwarning(message='left parenthesis required!')
                return
            entry_param_3 = self._entry_n_param_3.get()
            if entry_param_3 == '':
                showwarning(message='right parenthesis required!')
                return
            self.n_filename = entry_param_1
            self.n_left = entry_param_2
            self.n_right = entry_param_3

            # print(entity.to_string())
            # self.service.save(entity)
            self._load_data()
            self._fill_list(self._list_entities, self._lbox_entities)

        except Exception as e:
            showwarning('Error:', e)

    # Service
    def _load_data(self):
        self._list_entities = self.service.find_all(self.n_filename)

def main():
    root = Tk()
    d = Controller(root)
    mainloop()

if __name__ == '__main__':
    main()
