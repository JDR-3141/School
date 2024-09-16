from os import getcwd
import sqlite3
from tkinter import messagebox
import sys

sys.path.append(getcwd()+"\\Project\\Project Code")

from classes.Users import User

def validate_login(username_entry, password_entry):
    userid = username_entry.get()
    password = password_entry.get()
    conn = sqlite3.connect(getcwd()+"\\Project\\Assets\\Files.db")
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
    conn = sqlite3.connect(getcwd()+"\\Project\\Assets\\Files.db")
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