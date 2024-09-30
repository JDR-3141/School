from os import getcwd
import sqlite3

#print(getcwd())

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
        conn = sqlite3.connect(getcwd()+"\\Project\\Assets\\Files.db")
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
