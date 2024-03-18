import tkinter as tk
from tkinter import messagebox
import sqlite3
from os import getcwd
from datetime import date
from ttkthemes import ThemedTk, THEMES

global logged_in
logged_in = False

class User():
    users = []
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.date = date.today()#
        self.email = ""
        self.nationality = ""
        self.age = 0
        self.gender = ""
        User.users.append(self)
        #create database connection
        conn = sqlite3.connect(getcwd()+"\\accounts.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (Username, Password, Date) VALUES (?,?,?)",
                (
                    self.username,
                    self.password,
                    self.date
                ))
        conn.commit()
        conn.close()

# Function to validate the login
def validate_login(username_entry, password_entry):
    userid = username_entry.get()
    password = password_entry.get()
    conn = sqlite3.connect(getcwd()+"\\accounts.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT * from Users WHERE Username=?;''',[userid,])
    names = list(map(lambda x: x[0], cursor.description))
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    print(result)
    print(names)
    if len(result) == 0:
        messagebox.showerror("Error", "No such user")
    elif result[0][1] == password:
        messagebox.showinfo("Success", "Logged in as " + userid)
        global logged_in
        logged_in = userid
    else:
        messagebox.showerror("Error", "Incorrect password")


def validate_signup(username_entry, password_entry):
    userid = username_entry.get()
    password = password_entry.get()
    errors = []
    conn = sqlite3.connect(getcwd()+"\\accounts.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT * from Users WHERE Username=?;''',[userid,])
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    if userid == "":
        errors.append(["Username", "Username must not be blank"])
    elif len(result) != 0:
        errors.append(["Username", "Username already in use"])
    else:
        res = False
        for ele in userid:
            if ele == " ":
                res = True
                break
        if res:
            errors.append(["Username", "Username cannot contain empty space"])
    if len(password) < 5:
        errors.append(["Password", "Password must have at least 5 characters"])
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
    print(errors)
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
    else:
        User(userid, password)
        messagebox.showinfo("Success", "User successfully created")

def show(password_entry, show_button, hide_button):
    password_entry.config(show='')
    show_button.grid_forget()
    hide_button.grid(row=0,column=1)

def hide(password_entry, show_button, hide_button):
    password_entry.config(show='*')
    hide_button.grid_forget()
    show_button.grid(row=0,column=1)

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

    frame1 = tk.Frame(parent)
    frame1.pack()

    password_entry = tk.Entry(frame1, show="*", width=13)  # Show asterisks for password
    password_entry.grid(row=0,column=0)

    show_button = tk.Button(frame1, text="Show", command=lambda: show(password_entry, show_button, hide_button))
    show_button.grid(row=0,column=1)

    hide_button = tk.Button(frame1, text="Hide", command=lambda: hide(password_entry, show_button, hide_button))

    frame2 = tk.Frame(parent)
    frame2.pack()

    # Create and place the login button
    login_button = tk.Button(frame2, text="Log in", command=lambda: validate_login(username_entry, password_entry))
    login_button.grid(row=0,column=1,padx=(5, 5))

    # Create and place the login button
    signin_button = tk.Button(frame2, text="Sign up", command=lambda: validate_signup(username_entry, password_entry))
    signin_button.grid(row=0,column=0,padx=(5, 5))

def view_details():
    if not logged_in:
        messagebox.showerror("Error", "No user logged in")
    else:
        for widget in parent.winfo_children():
            if type(widget) != tk.Menu:
                widget.destroy()
        conn = sqlite3.connect(getcwd()+"\\accounts.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * from Users WHERE Username=?;''',[logged_in,])
        names = list(map(lambda x: x[0], cursor.description))
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        message = ""
        for i in range(len(result[0])):
            message += names[i] + ": "
            if result[0][i] != None:
                message += result[0][i] + "\n"
            else:
                message += "Not added\n"
        message = message.rstrip("\n")
        username_label = tk.Label(parent, text=message)
        username_label.pack()

    
    
    
def change_details():
    if not logged_in:
        messagebox.showerror("Error", "No user logged in")
    else:
        for widget in parent.winfo_children():
            if type(widget) != tk.Menu:
                widget.destroy()
        conn = sqlite3.connect(getcwd()+"\\accounts.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * from Users WHERE Username=?;''',[logged_in,])
        names = list(map(lambda x: x[0], cursor.description))
        results = cursor.fetchall()
        conn.commit()
        conn.close()
        result = [i+1 for i in range(len(names))]
        yscrollbar = tk.Scrollbar(parent)
        yscrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        files = tk.Listbox(parent, selectmode = "single",yscrollcommand = yscrollbar.set)
        files.pack(padx = 10, pady = 10, expand = tk.YES, fill = "both")
        for item in range(len(result)):
            files.insert(tk.END, names[item])
        yscrollbar.config(command = files.yview)
        button = tk.Button(parent, text = "Change", command = lambda:change(files, names, results)) 
        button.pack(fill = "x", side = "bottom")

def change(files, names, results):
    name = names[files.curselection()[0]]
    result = results[0][files.curselection()[0]]
    for widget in parent.winfo_children():
        if type(widget) != tk.Menu:
            widget.destroy()
    # Create and place the username label and entry
    username_label = tk.Label(parent, text="Current " + name + ":\n" + result + "\nNew " + name + ":")
    username_label.pack()

    username_entry = tk.Entry(parent)
    username_entry.pack()

    frame2 = tk.Frame(parent)
    frame2.pack()

    # Create and place the login button
    login_button = tk.Button(frame2, text="Submit", command=lambda: execute_change(name, username_entry.get()))
    login_button.grid(row=0,column=1,padx=(5, 5))

    # Create and place the login button
    signin_button = tk.Button(frame2, text="Cancel", command=lambda: default_screen())
    signin_button.grid(row=0,column=0,padx=(5, 5))

def execute_change(name, new):
    print("change " + name + " to " + new)

# Create the main window
parent = tk.Tk()
parent.title("Login Form")

# dimensions of the main window
parent.geometry("200x230")
parent.iconbitmap(getcwd()+"\\Icon.ico")

#ThemedTk.set_theme(parent, "equilux")

menu = tk.Menu(parent)
item = tk.Menu(menu)
item.add_command(label="View details", command=lambda: view_details())
item.add_command(label="Change details", command=lambda: change_details())
menu.add_cascade(label="Options", menu = item)
parent.config(menu=menu)

# Start the Tkinter event loop
default_screen()
parent.mainloop()
