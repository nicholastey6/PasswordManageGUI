from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)


window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
my_pass = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)


email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'asd@gmail.com')

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# def genPass():
#     pass

password_button = Button(text="Generate Password",command=generate_password)
password_button.grid(row=3, column=2)

def savePassword():
    website_name = website_input.get()
    email_name = email_input.get()
    password_name = password_input.get()

    if len(website_name) == 0  or len(password_name) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty.")

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                   f"\nPassword: {password} \nIs it ok to save?")

    if is_ok:
        with open('data.txt', 'a') as data_file:
            data_file.write(f"{website_name} | {email_name} | {password_name}")
            website_input.delete(0, END)
            password_input.delete(0, END)

        
add_button = Button(text="Add", width = 36, command=savePassword)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()