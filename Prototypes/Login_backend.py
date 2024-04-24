import sqlite3
from os import getcwd

class User():
    users = []
    def __init__(self, userID, username, password):
        self.userID = userID
        self.username = username
        self.password = password
        User.users.append(self)
        #create database connection
        conn = sqlite3.connect(getcwd()+"\\Prototypes\\Files.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (UserID, Username, Password) VALUES (?,?,?)",
                (
                    self.userID,
                    self.username,
                    self.password,
                ))
        conn.commit()
        conn.close()

# Function to validate the login
def validate_login(userid, password):
    conn = sqlite3.connect(getcwd()+"\\Prototypes\\Files.db")
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
    elif result[0][2] == password:
        print("Logged in as " + userid)
        global logged_in
        logged_in = userid
    else:
        print("Incorrect password")


def validate_signup(userid, password):
    errors = []
    conn = sqlite3.connect(getcwd()+"\\Prototypes\\Files.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT * from Users WHERE Username=?;''',[userid,])
    result = cursor.fetchall()
    cursor.execute('''SELECT UserID from Users''')
    users = cursor.fetchall()
    conn.commit()
    conn.close()
    users.sort()
    print(users)
    ID = users[-1][0] + 1
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
        print(first)
        print(second)
    else:
        User(ID, userid, password)
        print("User successfully created")

choice = input("Sign up or login (1/2): ")
if choice == "1":
    username = input("Username: ")
    password = input("Password: ")
    validate_signup(username, password)
elif choice == "2":
    username = input("Username: ")
    password = input("Password: ")
    validate_login(username, password)