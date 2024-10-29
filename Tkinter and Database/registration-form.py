from tkinter import *
from tkinter import messagebox
import sqlite3

window = Tk()
window.title("Registration")
window.geometry("460x520")

name = Entry(window)
Label(window, text="Enter name: ").grid(row=0)
name.grid(row=0, column=1)

email = Entry(window)
Label(window, text="Enter email: ").grid(row=1)
email.grid(row=1, column=1)

password = Entry(window)
Label(window, text="Create password: ").grid(row=2)
password.grid(row=2, column=1)

user_name = name.get().strip().capitalize()
user_email = email.get().strip()
user_password = password.get().strip()

def userdb():
    global con
    con = sqlite3.connect("user.db")
    global cur
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS usertb
                (Name text not null,
                Email text not null,
                Passwork text not null);
                ''')
    
def register():
    userdb()
    if not user_name:
        messagebox.showinfo("Alert!", "Please Enter Name.")
    elif not user_email:
        messagebox.showinfo("Alert!", "Please Enter Email.")
    elif not user_password:
        messagebox.showinfo("Alert!", "Please Create Password.")
    
    user_exists = cur.execute("SELECT Email FROM usertb WHERE Name = ?", (user_email,))
    if user_exists:
        print("User already exists.")
    else:
        cur.execute("INSERT INTO usertb (Name, Email, Password) VALUES(?, ?, ?)", (user_name, user_email, user_password))
        messagebox.showinfo("Confirmation", "Registration Successful")

Button(window, text='Register', command=register).grid(row=4)

window.mainloop()