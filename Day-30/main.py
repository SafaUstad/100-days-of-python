# Password Manager with Search Function

import json
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

password_entry = ""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()

    new_data = {
        website:{
            "user": user,
            "password": password
        }
    }
    if website == "" or user == "" or password == "":
        messagebox.showinfo("Oops", "Please don't leave any fields empty!")

    else:
        try:
            with open("data.json","r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json","w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json","r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found.")
    except KeyError:
        messagebox.showinfo(title="Oops", message= f"No Details for {website} exists.")
    else:
        messagebox.showinfo(title=website,message=f"Email: {data[website]['user']}\n"
                                                  f"Password: {data[website]['password']}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)

user_entry = Entry(width=52)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "safaustad@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=gen_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add",width=44, command=save)
add_button.grid(row=4, column=1,columnspan=2)

window.mainloop()
