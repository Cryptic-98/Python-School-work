from tkinter import *

m = Tk()
m.title('My first GUI application')
# labels are used for indicating what needs to be added.
Label(m, text='Enter number 1: ').grid(row=0)
Label(m, text='Enter number 2: ').grid(row=1)
Label(m, text='Answer: ').grid(row=2)

tf1 = Entry(m)
tf2 = Entry(m)
tf3 = Entry(m)
tf1.grid(row=0, column=1)
tf2.grid(row=1, column=1)
tf3.grid(row=2, column=1)


def button_on_click():
    # to get input from entry, we use method get()
    number1 = int(tf1.get())
    number2 = int(tf2.get())
    result = number1 + number2
    result = str(result)
    tf3.insert(0, result)


Button(m, text='Calculate', width=15, command=button_on_click).grid(row=3, column=1)
# add dimension to your GUI we use the geometry method
m.geometry('400x200')
m.mainloop()
