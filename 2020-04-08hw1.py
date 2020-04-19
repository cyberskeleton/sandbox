from tkinter import *

root = Tk()
enter = Entry(root, bg = 'cyan', fg = 'blue', borderwidth = 50)
enter.pack()
last = 0
count = 0

def check_sign():
    global last, count
    num = int(enter.get())
    msg = 'the sign has not changed'
    if num * last < 0:
        count += 1
        msg = 'the sign changed {} times!'.format(count)
    last = num
    action_label = Label(root, text=msg)
    action_label.pack()
    enter.delete(0, END)

test_button = Button(root, text = 'calculate', command = check_sign, bg = 'lightblue', fg = 'darkcyan')
test_button.pack()

root.mainloop()
