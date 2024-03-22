# https://codereview.stackexchange.com/questions/259710/login-system-using-bcrypt-and-mysql-to-be-used-for-any-future-projects
import bcrypt

password = input("What should your password be: ")
password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(14)).decode("utf-8")
print(password_hash)
guess = input("Reenter your correct password: ")
if bcrypt.checkpw(guess.encode('utf8'), password_hash.encode('utf8')):
    print("Correct")
else:
    print("Incorrect")
