from os import getcwd
import sqlite3


class User():
    user = None
    def __init__(self, username, password, email=None, date=None, songs_created=None, songs_liked=None):
        self.username = username
        self.password = password
        self.email = email
        self.date = date#
        self.songs_created = songs_created
        self.songs_liked = songs_liked
        User.user = self
        

    def save(self):
        #create database connection
        conn = sqlite3.connect(getcwd()+"\\Project\\Assets\\Files.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (Username, Password, Email, Date, Songs_created, Songs_liked) VALUES (?,?,?,?,?,?)",
                (
                    self.username,
                    self.password,
                    self.email,
                    self.date,
                    self.songs_created,
                    self.songs_liked
                ))
        conn.commit()
        conn.close()
        #load_from_db()

    def get_username(self):
        return self.username

def loadUser(data):
    User(data[0], data[1], data[2], data[3], data[4], data[5])

# user1 = User("Test", "Pa$$w0rd")
# print(user1.get_username())