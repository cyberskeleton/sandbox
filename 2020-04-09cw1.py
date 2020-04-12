from tkinter import *

root = Tk()
entry_l = Label(root, text='input value of currency for 1 hr in row (eu, usd)')
entry_l.pack(side = LEFT)
enter = Entry(root)
enter.pack(side = RIGHT)
last = 0
root2 = Tk()
entry_l2 = Label(root2, text='input amount of hryvnas')
entry_l2.pack(side = LEFT)
enter2 = Entry(root2)
enter2.pack()

def input_currency():
    global last
    nums = enter.get()
    f = open('currency.txt', 'w')
    f.write(nums)
    action_label = Label(root, text='done')
    action_label.pack()
    enter.delete(0, END)

def usd_to_hr():
    f = open('currency.txt', 'r')
    amount = int(enter2.get())
    list = f.read().split(' ')
    dollar_worth = float(list[1])
    ans = dollar_worth*amount
    action_label = Label(root2, text=ans)
    action_label.pack()

def eu_to_hr():
    f = open('currency.txt', 'r')
    amount = int(enter2.get())
    list = f.read().split(' ')
    eu_worth = float(list[0])
    ans = eu_worth*amount
    action_label = Label(root2, text=ans)
    action_label.pack()
test_button = Button(root, text = 'add currency', command = input_currency)
test_button.pack()
test_button2 = Button(root2, text = 'convert to usd', command = usd_to_hr)
test_button2.pack()
test_button3 = Button(root2, text = 'convert to eu', command = eu_to_hr)
test_button3.pack()
root.mainloop()
root2.mainloop()
