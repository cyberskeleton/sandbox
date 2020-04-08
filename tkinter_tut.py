from tkinter import  *

root = Tk()
#test_label = Label(root, text = 'when will you learn')
#test_label2 = Label(root, text = 'WHEN WILL YOU LEARN THAT YOUR ACTIONS HAVE CONSEQUENCES')
#test_label.pack()
#test_label.grid(row = 0, column = 1)
#test_label2.grid(row = 1, column = 0)
enter = Entry(root, bg = 'cyan', fg = 'blue', borderwidth = 100)
enter.pack()
def hryk():
    action_label = Label(root, text = 'Hello, {}, nice to meet you!'.format(enter.get()))
    action_label.pack()
test_button = Button(root, text = 'enter name', command = hryk, bg = 'pink', fg = 'cyan')
test_button.pack()
root.mainloop()
