import sqlite3
from os import getcwd
from datetime import date


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
        print("No such user")
    elif result[0][1] == password:
        print("Logged in as " + userid)
        global logged_in
        logged_in = userid
    else:
        print("Incorrect password")


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