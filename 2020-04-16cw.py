from tkinter import *
from tkinter.messagebox import *
from collections import defaultdict

class Polynome(defaultdict):
    def __init__(self, **kwargs):
        defaultdict.__init__(self, float, **kwargs)

    def fromstring(s):
        poly = Polynome()
        s = s.replace('+',' ')
        ls = s.split()  #розбиваємо на список одночленів
        for m in ls:
            c = m.split('*x**') #виділяємо степінь та коефіцієнт
            power = int(c[1])
            coeff = float(c[0])
            poly[power] = coeff
        return poly

    fromstring = staticmethod(fromstring)

    def add_monom(self, deg, coeff):
        if coeff != 0:
            self[deg] += coeff

    def get_degree(self):
        return max(self)

    def __str__(self):
        monomials = list(self.items())
        if not monomials:
            poly_str = "0.0*x**0"
        else:
            monomials.sort(reverse=True)
            ls = ["{}*x**{}".format(mono[1], mono[0]) for mono in monomials]
            poly_str = ' + '.join(ls)
        return poly_str

    def __call__(self, x):
        return sum([self[k]*x**k for k in self])

    def __add__(self, other):
        p = Polynome()
        keys = set(self.keys()) | set(other.keys())
        for k in keys:
            p[k] = self[k] + other[k]
        return self._delzeroes(p)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        p = Polynome()
        keys = set(self.keys()) | set(other.keys())
        for k in keys:
            p[k] = self[k] - other[k]
        return self._delzeroes(p)

    def __rsub__(self, other):
        p = Polynome()
        keys = set(self.keys()) | set(other.keys())
        for k in keys:
            p[k] = other[k] - self[k]
        return self._delzeroes(p)

    def __mul__(self, other):
        p = Polynome()
        for k1 in self:
            for k2 in other:
                p[k1 + k2] += self[k1] * other[k2]
        return self._delzeroes(p)

    def __rmul__(self, other):
        return self.__rmul__(other)

    def deriv(self, n=1):
        p = self
        for i in range(n):
            p = self._deriv(p)
        return self._delzeroes(p)

    def _deriv(self, p):
        pp = Polynome()
        for k in p:
            if k != 0:
                pp[k - 1] = p[k] * k
        return pp

    def _delzeroes(self, p):
        pp = Polynome()
        for k in p:
            if p[k] != 0:
                pp[k] = p[k]
        return pp

    def makewidgets(self):
        self.frame = Frame(self.root)

# if __name__ == '__main__':
#     p1 = Polynome.fromstring('3.7*x**3 + 0.3*x**1 + -1.2*x**0')
#     print('р1 =', p1)
#     p2 = Polynome.fromstring('2.2*x**3 + -1.3*x**2 + 0.2*x**1')
#     print('р2 =', p2)
#     print('Значення p1 у точці x=2:', p1(2))
#     print('Сума p1+p2:', p1 + p2)
#     print('Різниця p1-p2:', p1 - p2)
#     print('Добуток p1*p2:', p1 * p2)
#     p = p1.deriv(2)
#     print('2 похідна р1:', p)

class Calculator:
    def __init__(self, master):
        self.root = master
        self.first = ""
        self.second = ""
        self.result = ""
        self.n = 0
        self._make_widgets()
        self._calculate()

    def _calculate(self):
        pass

    def _make_widgets(self):
        self._frame_top = Frame(self.root)

        self._lbl_n = Label(self._frame_top, text="Enter n:", font="Arial 16")
        self._lbl_n.pack(side = LEFT, padx = 5)
        self._entry_n = Entry(self._frame_top, width=7, justify='center', font="Arial 16", textvariable = self.n)
        self._entry_n.pack(side = RIGHT, padx = 5)
        self._frame_top.pack(side=TOP, fill=Y, expand=NO)
        self._btn_ok = Button(self.root, width=8, justify='center', text='Ok', command=self.ok_handler)
        self._btn_ok.pack(side=BOTTOM, padx=5, pady=5)

    def ok_handler(self, ev=None):
        self.n = int(self._entry_n.get())
        self._lbl_n.pack_forget()
        self._entry_n.pack_forget()
        self._btn_ok.pack_forget()
        if not self._entry_n.get():
            showwarning(message='Enter n!')
            return
        print("n: ", self.n)
        self._input_coefficients()

    def _input_coefficients(self):
        self.first = []
        for i in range(0, self.n + 1):
            self.first.append(self._input_one(i))
        self._frame_first_wrapper = Frame(self._frame_top)
        self._btn_f = Button(self._frame_first_wrapper, width=8, justify='center', text='Ok', command=self.ok_input())
        self._btn_f.pack(side=RIGHT, padx=5, pady=5)
        self._frame_first_wrapper.pack(side=TOP, fill=Y, expand=NO)

    def _input_one(self, i):
        self._frame_first = Frame(self._frame_top)
        self._lbl_first = Label(self._frame_first, text='*x**' + str(i), font="Arial 16")
        self._lbl_first.pack(side=RIGHT, padx=5)
        self._entry_first = Entry(self._frame_first, width=3, justify='center', font="Arial 16", textvariable="")
        self._entry_first.pack(side=LEFT, padx=5)
        self._frame_first.pack(side=LEFT, fill=Y, expand=NO)

    def ok_input(self):
        result = self._entry_first.get()
        if result:
            self._frame_first.pack_forget()
            self._lbl_first.pack_forget()
            self._entry_first.pack_forget()
            self._frame_top.pack_forget()
        return result

def main():
    top = Tk()
    d = Calculator(top)
    mainloop()
    # val = d.get()

if __name__ == '__main__':
    main()
