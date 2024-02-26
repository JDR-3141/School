import tkinter as tk
from tkinter import messagebox
import sqlite3
from os import getcwd


class User():
    users = []
    def __init__(self, username, password, email, date):
        self.username = username
        self.password = password
        self.email = email
        self.date = date#
        User.users.append(self)

    def save(self):
        #create database connection
        conn = sqlite3.connect(getcwd()+"\\accounts.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (Username, Password, Email, Date) VALUES (?,?,?,?)",
                (
                    self.username,
                    self.password,
                    self.email,
                    self.date
                ))
        conn.commit()
        conn.close()
        #load_from_db()

def save_to_database():
    for user in User.users:
        user.save()

def load_from_database():
    pass

# Function to validate the login
def validate_login(username_entry, password_entry):
    userid = username_entry.get()
    password = password_entry.get()

def validate_signup(username_entry, password_entry):
    userid = username_entry.get()
    password = password_entry.get()
    errors = []
    if userid == "":
        errors.append(["Username", "Username must not be blank"])
    if password == "":
        errors.append(["Password", "Password must not be blank"])
    elif password.isnumeric():
        errors.append(["Password", "Password must contain letters"])
    elif password.isalpha():
        errors.append(["Password", "Password must contain numbers"])
    else:
        res = False
        for ele in password:
            if ele.isupper():
                res = True
                break
        if not res:
            errors.append(["Password", "Password must contain at least 1 uppercase letter"])
    if len(errors) != 0:
        first = ""
        second = ""
        for error in errors:
            first += error[0] + " & "
            second += error[1] + "\n"
        first = first.rstrip(" & ")
        first += " Invalid"
        second = second.rstrip("\n")
        messagebox.showerror(first, second)

def show():
    password_entry.config(show='')
    show_button.grid_forget()
    hide_button.grid(row=1,column=2)

def hide():
    password_entry.config(show='*')
    hide_button.grid_forget()
    show_button.grid(row=1,column=2)

def default_screen():
    for widget in parent.winfo_children():
        if type(widget) != tk.Menu:
            widget.destroy()
    # Create and place the username label and entry
    username_label = tk.Label(parent, text="Username:")
    username_label.pack()

    username_entry = tk.Entry(parent)
    username_entry.pack()

    # Create and place the password label and entry
    password_label = tk.Label(parent, text="Password:")
    password_label.pack()

    password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
    password_entry.pack()

    frame = tk.Frame(parent)
    frame.pack()

    # Create and place the login button
    login_button = tk.Button(frame, text="Log in", command=lambda: validate_login(username_entry, password_entry))
    login_button.grid(row=0,column=1,padx=(5, 5))

    # Create and place the login button
    signin_button = tk.Button(frame, text="Sign up", command=lambda: validate_signup(username_entry, password_entry))
    signin_button.grid(row=0,column=0,padx=(5, 5))

# Create the main window
parent = tk.Tk()
parent.title("Login Form")

# dimensions of the main window
parent.geometry("200x115")

menu = tk.Menu(parent)
item = tk.Menu(menu)
item.add_command(label="View details")#, command=lambda: return)
item.add_command(label="Change details")#, command=lambda: return)
menu.add_cascade(label="Options", menu = item)
parent.config(menu=menu)

# Start the Tkinter event loop
default_screen()
parent.mainloop()


