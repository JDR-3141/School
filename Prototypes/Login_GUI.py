import tkinter as tk
from tkinter import messagebox, ttk
from ttkthemes import ThemedTk, THEMES
from os import getcwd


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
    login_button = tk.Button(frame2, text="Log in", command=lambda: print("Login now"))
    login_button.grid(row=0,column=1,padx=(5, 5))

    # Create and place the login button
    signin_button = tk.Button(frame2, text="Sign up", command=lambda: print("Sign in now"))
    signin_button.grid(row=0,column=0,padx=(5, 5))




# Create the main window
parent = ThemedTk(theme="Black")
parent.title("Login Form")

# dimensions of the main window
parent.geometry("200x230")
parent.iconbitmap(getcwd()+"\\Icon.ico")

menu = tk.Menu(parent)
item = tk.Menu(menu)
item.add_command(label="Do something", command=lambda: print("Something done here"))
menu.add_cascade(label="Options", menu = item)
parent.config(menu=menu)

# Start the Tkinter event loop
default_screen()
parent.mainloop()