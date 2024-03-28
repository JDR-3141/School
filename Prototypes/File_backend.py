from os import getcwd
import sqlite3

conn = sqlite3.connect("C:\\Users\\jdraj\\OneDrive\\Documents\\GitHub\\School\\Prototypes\\Files.db")
cursor = conn.cursor()
cursor.execute('''SELECT * from Projects WHERE User=?;''',[1,])
names = list(map(lambda x: x[0], cursor.description))
result = cursor.fetchall()
conn.commit()
conn.close()
print(names, "\n", result)
piece_name = input("Piece name: ")
found = False
for t in result:
    if piece_name == t[2]:
        piece_number = t[0]
        found = True
if not found:
    print("User not found")
else:
    conn = sqlite3.connect("C:\\Users\\jdraj\\OneDrive\\Documents\\GitHub\\School\\Prototypes\\Files.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT * from Takes WHERE Project=?;''',[piece_number,])
    names1 = list(map(lambda x: x[0], cursor.description))
    result1 = cursor.fetchall()
    conn.commit()
    conn.close()
print(names1, "\n", result1)