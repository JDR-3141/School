import tkinter as tk
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
def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

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
login_button = tk.Button(frame, text="Log in", command=validate_login)
login_button.grid(row=0,column=1,padx=(5, 5))

# Create and place the login button
signin_button = tk.Button(frame, text="Sign in", command=validate_login)
signin_button.grid(row=0,column=0,padx=(5, 5))

# Start the Tkinter event loop
parent.mainloop()

