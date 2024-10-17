from tkinter import *
from tkinter import messagebox

m = Tk()
m.title('My Second GUI application')
Label(m, text='Enter name: ').grid(row=0)
name = Entry(m)
name.grid(row=0, column=1)
terms_var = IntVar()
newsletter_var = IntVar()
agree_terms = Checkbutton(m, text='Agree to Terms', variable=terms_var).grid(row=1, column=0, padx=10)
subscribe_newsletter = Checkbutton(m, text='Subscribe to Newsletter', variable=newsletter_var).grid(row=2)



def button():
    if not name.get():
        messagebox.showinfo('Alert!', 'Please enter a name.')
        return
    elif agree_terms and subscribe_newsletter:
        messagebox.showinfo('Alert!', f'Hello, {name.get().capitalize()}! You agreed to the terms and subscribed to the newsletter.')
    elif terms_var.get():
        messagebox.showinfo('Alert!',f'Hello, {name.get().capitalize()}! You agreed to the terms.')
    else:
        messagebox.showinfo('Alert!', f'Hello {name.get().capitalize()}! Please agree to the terms.')


Button(m, text='Submit', width=50, command=button).grid(row=3, columnspan=2)
m.geometry('1080x720')
m.mainloop()
