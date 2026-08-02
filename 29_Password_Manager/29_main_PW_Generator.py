# used Links:
#https://tkdocs.com/tutorial/canvas.html
#https://web.archive.org/web/20201108093851/effbot.org/tkinterbook/canvas.htm
#https://www.w3schools.com/python/python_file_write.asp
#https://tkdocs.com/tutorial/widgets.html#entry
#https://pypi.org/project/pyperclip/
#https://www.w3schools.com/python/ref_string_join.asp

from random import choice,randint, shuffle
from tkinter import messagebox
from tkinter import *
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = ( password_letters + password_symbols + password_numbers)
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    #empty_warning = messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title="website", message=f"These are the details entered: \nEmail: {email}"
                                                         f"\nPassword: {password} \nIs it okay to save?")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)



    website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Make the input columns expandable
window.grid_columnconfigure(1, weight=3)
window.grid_columnconfigure(2, weight=2)

# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3, pady=(0, 20))

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e", padx=(0, 10), pady=3)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="e", padx=(0, 10), pady=3)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e", padx=(0, 10), pady=3)

# Entries
website_entry = Entry()
website_entry.grid(
    column=1,
    row=1,
    columnspan=2,
    sticky="ew",
    pady=3
)
website_entry.focus()

email_entry = Entry()
email_entry.grid(
    column=1,
    row=2,
    columnspan=2,
    sticky="ew",
    pady=3
)
email_entry.insert(0,"engel@gmail.com")

password_entry = Entry()
password_entry.grid(
    column=1,
    row=3,
    sticky="ew",
    padx=(0, 5),
    pady=3
)

# Buttons
generate_pw_button = Button(
    text="Generate Password",
    command=generate_password
)
generate_pw_button.grid(
    column=2,
    row=3,
    sticky="ew",
    padx=(5, 0),
    pady=3
)

add_button = Button(
    text="Add",
    command=save
)
add_button.grid(
    column=1,
    row=4,
    columnspan=2,
    sticky="ew",
    pady=(5, 0)
)

website_entry.focus()

window.mainloop()