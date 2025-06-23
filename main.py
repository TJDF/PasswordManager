# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import password_generator
import json
def write_password():
    password_input.delete(0,"end")
    password_input.insert(0, password_generator.generate_password())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:{
                "email": email,
                "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Please, don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email}\n"
                                                              f"Password: {password}\n\n"
                                                              f"Are you sure you want to save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_input.delete(0, "end")
                password_input.delete(0,"end")

def search():

    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Warning", message="No data info")
    else:
        try:
            messagebox.showinfo(title=website, message=f"Email: {data[website]["email"]} \n"
                                                         f"Password: {data[website]["password"]}")
        except KeyError:
            messagebox.showinfo(title="Warning", message="No data found")
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)

website_lbl = Label(text="Website:")
website_lbl.grid(row=1,column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, sticky="ew")
website_input.focus()

search_btn = Button(text="Search", command=search)
search_btn.grid(row=1,column=2, sticky="ew")

email_lbl = Label(text="Email/Username:")
email_lbl.grid(row=2,column=0)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="ew")
email_input.insert(0,"Tijololol")

password_lbl = Label(text="Password:")
password_lbl.grid(row=3,column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="ew")

generate_btn = Button(text="Generate Password", command=write_password)
generate_btn.grid(row=3,column=2, sticky="ew")

add_btn = Button(text="add", width=36, command=save)
add_btn.grid(row=4,column=1, columnspan=2, sticky="ew")

window.mainloop()