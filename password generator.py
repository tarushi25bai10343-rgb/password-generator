from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from PIL import Image, ImageTk   # To load JPG/PNG safely

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops!", message="Don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details:\n\nEmail: {email}\nPassword: {password}\n\nSave?"
        )

        if is_ok:
            with open(r"C:\Users\Tarushi Tanavi\Desktop\New folder\python project 2 updated.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Load image (PNG recommended)
img = Image.open(r"C:\Users\Tarushi Taanvi\Desktop\project vityarthi\WhatsApp Image 2025-11-23 at 23.17.58 (1) (1).png")   # Use PNG
img = img.resize((200, 200))
logo = ImageTk.PhotoImage(img)

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.image = logo    # <<< IMPORTANT
canvas.grid(column=1, row=0)

# Labels
Label(text="Website:").grid(column=0, row=1)
Label(text="Email/Username:").grid(column=0, row=2)
Label(text="Password:").grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "user@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
Button(text="Generate Password", command=generate_password).grid(column=2, row=3)
Button(text="Add", width=36, command=save).grid(column=1, row=4, columnspan=2)

window.mainloop()
