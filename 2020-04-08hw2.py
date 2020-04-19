from tkinter import *

root = Tk()
enter = Entry(root, bg = 'cyan', fg = 'blue', borderwidth = 50)
enter.pack()

def delete_brackets():
    string = enter.get()
    return cut_off(string)

def cut_off(string):
    if '(' in string and ')' in string:
        string1 = string[:string.find('(')]
        string2 = string[string.find(')') + 1:]
        string = string1 + string2
    else:
        print('result: ' + string)
        return string
    cut_off(string)


test_button = Button(root, text = 'delete', command = delete_brackets, bg = 'lightblue', fg = 'darkcyan')
test_button.pack()
root.mainloop()
