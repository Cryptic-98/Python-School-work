from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Registration Form')
window.geometry('460x520')

name = Entry(window)
Label(window, text='Enter name: ').grid(row=0)
name.grid(row=0, column=1)
gender_var = StringVar()
male_gender = Radiobutton(window, text='Male', variable=gender_var, value='Male').grid(row=1, column=0)
female_gender = Radiobutton(window, text='Female', variable=gender_var, value='Female').grid(row=1, column=1)
Label(window, text='Enter Email: ').grid(row=2)
email = Entry(window)
email.grid(row=2, column=1)
Label(window, text='Create password: ').grid(row=3)
password = Entry(window)
password.grid(row=3, column=1)


def submit_information():
    user_name = name.get().capitalize().strip()
    user_email = email.get().strip()
    user_password = password.get().strip()
    user_gender = gender_var.get()
    user_information = {
        'Name': user_name,
        'Gender': user_gender,
        'Email': user_email,
        'Password': user_password
    }
    if not user_name:
        messagebox.showinfo('Alert', 'Please enter a name.')
    elif not user_email:
        messagebox.showinfo('Alert', 'Please enter an email')
    elif not user_gender:
        messagebox.showinfo('Alert', 'Please pick gender.')
    elif not user_password:
        messagebox.showinfo('Alert', 'Create a password.')

    messagebox.showinfo('Information', f'Name: {user_information["Name"]} \nGender: {user_information["Gender"]}\n'
                                       f'Email: {user_information["Email"]}\n')


Button(window, text='Sign Up', command=submit_information).grid(row=4)

window.mainloop()
