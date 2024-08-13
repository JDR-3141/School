#########################################################################################################
# Imports and globals

import sounddevice as sd 
from scipy.io.wavfile import write
import tkinter as tk
from os import getcwd
import customtkinter as ctk
import sqlite3

from classes import *
from modules import *


global parent
global colour_palette
global name

#########################################################################################################

#########################################################################################################
# Classes







#########################################################################################################

#########################################################################################################
# Functions

def choose(choices):
    for widget in parent.winfo_children():
        if type(widget) != tk.Menu:
            widget.destroy()
    result = [i+1 for i in range(len(choices))]
    yscrollbar = tk.Scrollbar(parent)
    yscrollbar.pack(side = tk.RIGHT, fill = tk.Y)
    files = tk.Listbox(parent, selectmode = "single",yscrollcommand = yscrollbar.set)
    files.pack(padx = 10, pady = 10, expand = tk.YES, fill = "both")
    for item in range(len(result)):
        files.insert(tk.END, choices[item])
    yscrollbar.config(command = files.yview)
    button = tk.Button(parent, text = "Open", command = lambda:print(choices[files.curselection()[0]][0]))
    button.pack(fill = "x", side = "bottom")

def choose_audio(user):
    for widget in parent.winfo_children():
        if type(widget) != tk.Menu:
            widget.destroy()

    conn = sqlite3.connect(getcwd()+"\\Files.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT Projectname FROM Songs WHERE Creator = ?''', (user,),)
    result = cursor.fetchall()
    conn.commit()
    conn.close()

    combobox = ctk.CTkComboBox(parent, values=result, command=callback)
    combobox.pack()
    
def callback(choice):
    print(choice)



def audio_input(recording):
    new_take = Take(44100, 3, "Dev", "", 0, "test.wav", gui)
    if recording:
        new_take.record()
    else:
        new_take.choose()


# ctk.set_appearance_mode("light")
# ctk.set_default_color_theme("blue")
    # Create the main parent
# parent = tk.Tk()
# parent.title("Login Form")

# # dimensions of the main parent
# parent.geometry("400x500")
# parent.iconbitmap(getcwd()+"\\Icon.ico")

# menu = tk.Menu(parent)
# menu.configure()
# item = tk.Menu(menu)
# item.add_command(label="View details")
# item.add_command(label="Change details")
# menu.add_cascade(label="Options", menu = item)
# parent.config(menu=menu)

# # Start the Tkinter event loop
# default_screen()
# parent.mainloop()

if __name__ == "__main__":
    gui = GUI()
    gui.Label()
    gui.default_screen()
    gui.mainloop()
    gui.main.wm_attributes("-transparentcolor", 'blue')