from secrets import choice
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_space.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():

    is_ok = messagebox.askokcancel(title=f'{website_space.get()}',message=f'Do you want to save the details entered: \n '
                                                                   f'Email: {email_space.get()} \n '
                                                                   f'Password: {password_space.get()} \n Ok to save?')
    if is_ok:
        with open('data.txt', 'a') as data:
            data.write(f' {website_space.get()}  /  {email_space.get()}  /  {password_space.get()} \n')
            website_space.delete(0, END)
            password_space.delete(0, END)


def check():
    if len(website_space.get()) == 0 or len(password_space.get()) == 0:
        messagebox.showinfo(title='warning', message= 'Please dont leave fields empty')
    else:
        add_password()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('PASSWORD MANAGER')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_text = Label(text='Website:')
website_text.grid(row=1, column=0)

email_text = Label(text='Email/Username:')
email_text.grid(row=2, column=0)

password_text = Label(text='Password:')
password_text.grid(row=3, column=0)

generate_button = Button(text='Generate Password', width=14, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=38, command=check)
add_button.grid(row=4, column=1, columnspan=2)

website_space = Entry()
website_space.config(width=41)
website_space.grid(row=1, column=1, columnspan=2)
website_space.focus()


email_space = Entry()
email_space.config(width=41)
email_space.grid(row=2, column=1, columnspan=2)
email_space.insert(0, 'prasanth@gamil.com')

password_space = Entry()
password_space.config(width=21)
password_space.grid(row=3, column=1, columnspan=1)


window.mainloop()
