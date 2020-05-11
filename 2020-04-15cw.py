#20.14
from tkinter import *
from tkinter.messagebox import *

class Converter:

    def __init__(self, master, file_curr, file_rates):
        self.root = master
        self.file_curr = file_curr
        self.file_rates = file_rates
        self.txt_from = "amount:"
        self.txt_to = "sum to get:"
        self.txt_sum = "0.0"
        self._load_data()
        self._make_widgets()

    def _load_data(self):
        self._list_selected = []
        self._cancel = False
        self.amount = 0.0

        self._read_currencies()
        self._read_rates()

    def _read_currencies(self):
        with open(self.file_curr) as f:
            self._list_currencies = f.read().splitlines()
        print(self._list_currencies)

    def _read_rates(self):
        self._dict_rates = {}
        with open(self.file_rates) as f:
            for line in f:
                (key, val) = line.split()
                self._dict_rates[key] = float(val)
        print(self._dict_rates)

    def _make_widgets(self):
        self._frame_left = Frame(self.root)
        self._sbar_currencies = Scrollbar(self._frame_left)
        self._sbar_currencies.pack(side=RIGHT, fill=Y)
        self._lbox_currencies = Listbox(self._frame_left, height=12, width=10, yscrollcommand=self._sbar_currencies.set)
        self._sbar_currencies.config(command=self._lbox_currencies.yview)
        self._lbox_currencies.pack(side=RIGHT, fill=BOTH, expand=YES)
        self._frame_left.pack(side=LEFT, fill=Y, expand=YES)
        self._lbox_currencies.bind('<Double-1>', self._add_currency)
        self._fill_list(self._list_currencies, self._lbox_currencies)

        self._frame_right = Frame(self.root)

        self._frame_top = Frame(self._frame_right)
        self._lbl_from = Label(self._frame_top, text=self.txt_from, font="Arial 16")
        self._lbl_from.pack(side = LEFT, padx = 5)
        self._entry = Entry(self._frame_top, width=7, justify='center', font="Arial 16", textvariable = self.amount)
        self._entry.pack(side = RIGHT, padx = 5)
        self._frame_top.pack(side=TOP, fill=Y, expand=NO)

        self._frame_center = Frame(self._frame_right)
        self._lbl_to = Label(self._frame_center, text=self.txt_to, font="Arial 16")
        self._lbl_to.pack(side = LEFT, padx = 5)
        self._lbl_sum = Label(self._frame_center, text=self.txt_sum, font="Arial 16")
        self._lbl_sum.pack(side = RIGHT, padx = 5)
        self._frame_center.pack(side=TOP, fill=Y, expand=NO)

        self._frame_btm = Frame(self._frame_right)
        self._btn_ok = Button(self._frame_btm, width=8, justify='center', text='Ok', command=self.ok_handler)
        self._btn_ok.pack(side=TOP, padx=5, pady=5)
        self._btn_cancel = Button(self._frame_btm, width=8, justify='center', text='Cancel', command=self.cancel_handler)
        self._btn_cancel.pack(side=TOP, padx=5, pady=5)
        self._frame_btm.pack(side=TOP, fill=Y, expand=NO)

        self._frame_right.pack(side=LEFT, fill=Y, expand=YES)
        menubar = Menu(self.root, tearoff=0)
        menubar.add_command(label='Load data', command=self._load_data)
        menubar.add_command(label='Refresh', command=self._refresh)
        menubar.add_command(label='Cancel', command=self.root.quit)

        frame = Frame(self.root)
        frame.pack()

        def popup(event):
            menubar.post(event.x_root, event.y_root)

        frame.bind("<Button-3>", popup)

        self.check = Checkbutton( justify='center',text='Calculate', command=self.ok_handler)
        self.check.pack(side=TOP, expand=YES)

        self.read_curr_but = Button(text='Currency file', command=self._read_currencies).pack(fill=X)
        self.read_rate_but = Button(text='Rate file', command=self._read_rates).pack(fill=X)
        askquestion('Continue?')

        self.root.config(menu=menubar)

    def _fill_list(self, items, lst):
        lst.delete(0, END)
        for item in items:
            lst.insert(END, item)

    def _add_currency(self, ev=None):
        try:
            count = len(self._list_selected)
            if count >= 2:
                showwarning(message='Currencies already selected!')
                return
            cur_sel = self._lbox_currencies.curselection()
            elem = self._lbox_currencies.get(cur_sel)
            if not elem:
                return
            index = cur_sel[0]
            self._lbox_currencies.delete(index)
            value = self._list_currencies[index]
            self._list_selected.append(value)
            if count == 0:
                self._lbl_from.config(text=value)
            else:
                self._lbl_to.config(text=value)
            del self._list_currencies[index]

        except TclError:
            pass
        except Exception as e:
            showwarning('Error: ', e)

    def _convert(self):
        try:
            key = self._list_selected[1] + "_" + self._list_selected[0]
            value = round(self._dict_rates[key] * self.amount, 2)
            print(key, value)
            self._lbl_sum.config(text=value)
        except TclError:
            pass
        except Exception as e:
            showwarning('Помилка', e)

    def ok_handler(self, ev=None):
        count = len(self._list_selected)
        if count < 2:
            showwarning(message='Currencies not selected!')
            return
        if not self._entry.get():
            showwarning(message='Enter amount!')
            return
        self.amount = float(self._entry.get())
        print("Amount: ", self.amount)
        self._convert()

    def cancel_handler(self, ev=None):
        self._cancel = True
        self._load_data()
        self._refresh()

    def _refresh(self):
        self._entry.delete(0, END)
        self._fill_list(self._list_currencies, self._lbox_currencies)
        self._lbl_from.config(text=self.txt_from)
        self._lbl_to.config(text=self.txt_to)
        self._lbl_sum.config(text=self.txt_sum)

    def get(self):
        result = self.txt_sum if not self._cancel else None
        return result


def main():
    top = Tk()
    d = Converter(top, 'converter_curr.txt', 'converter_rate.txt')
    mainloop()
    val = d.get()

if __name__ == '__main__':
    main()
