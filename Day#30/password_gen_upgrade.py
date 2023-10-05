from tkinter import *
from tkinter import messagebox
import string
from random import choice, shuffle
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
LIGHT_BEIGE = "#F8F0E5"
MIDDLE_BEIGE = "#EADBC8"
DARK_BEIGE = "#DAC0A3"
BLUE = "#0F2C59"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def create_password():
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '+']

    password_low_letters = [choice(alphabet_lower) for _ in range(3)]
    password_up_letters = [choice(alphabet_upper) for _ in range(3)]
    password_numbers = [choice(numbers) for _ in range(3)]
    password_symbols = [choice(symbols) for _ in range(3)]

    password = password_low_letters + password_up_letters + password_numbers + password_symbols
    shuffle(password)

    final_password = "".join(password)

    password_text.insert(0, final_password)
    pyperclip.copy(final_password)
    info_label.config(text="Info: Password Copied")





# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear_email_info(event):
    email_text.delete(0, END)
    email_text.config(fg=BLUE)


def save():
    # collect entries from entry boxes
    website_info = website_text.get()
    email_info = email_text.get()
    password_info = password_text.get()
    new_data = {
        website_info: {
            "email": email_info,
            "password": password_info,
        }
    }
    # show a popup info
    if website_info == "" or password_info == "":
        messagebox.showinfo(title="Wrong entry", message=f"Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data1.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print("LOg -- file not found error")
            with open("data1.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # print(data)
            data.update(new_data)

            with open("data1.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # clear_entries()
            website_text.delete(0, END)
            password_text.delete(0, END)
            email_text.delete(0, END)
            info_label.config(text="")

# ---------------------------- SEARCH WEBSITE ------------------------------- #


def find_password():
    website = website_text.get()
    if website == "":
        messagebox.showinfo(title="Wrong entry", message=f"Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data1.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50, bg=LIGHT_BEIGE)

canvas = Canvas(width=200, height=200, bg=LIGHT_BEIGE, highlightthickness=0)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=1, row=0, sticky="EW")

#Labels
website_label = Label(text="Website:", bg=LIGHT_BEIGE, fg=BLUE, width=20)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg=LIGHT_BEIGE, fg=BLUE, width=20)
email_label.grid(column=0, row=2)
password_label = Label(text="Password: ", bg=LIGHT_BEIGE, fg=BLUE, width=20)
password_label.grid(column=0, row=3)
info_label = Label(text="", bg=LIGHT_BEIGE, fg=BLUE, width=20)
info_label.grid(column=0, row=5, columnspan=2,sticky="E")

#Entries
website_text = Entry(width=35, fg=BLUE)
website_text.grid(column=1, row=1, columnspan=2, sticky="EW")
website_text.focus()
email_text = Entry(width=35, fg="grey")
email_text.grid(column=1, row=2, columnspan=2, sticky="EW")
email_text.insert(0, "Enter your email")
email_text.bind('<Button-1>', clear_email_info)
password_text = Entry(width=21, fg=BLUE)
password_text.grid(column=1, row=3, sticky="W")



#Buttons
search_button = Button(text="Search", bg=LIGHT_BEIGE, width=25, highlightthickness=0, fg=BLUE, command=find_password)
search_button.grid(column=2, row=1, sticky="E")
generate_button = Button(text="Generate Password", bg=LIGHT_BEIGE, width=25, highlightthickness=0, fg=BLUE,
                         command=create_password)
generate_button.grid(column=2, row=3, sticky="E")
add_button = Button(text="Add", highlightthickness=0, bg=LIGHT_BEIGE, fg=BLUE, width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
