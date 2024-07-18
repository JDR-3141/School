#########################################################################################################
# Imports and globals

import sounddevice as sd 
from scipy.io.wavfile import write
import tkinter as tk
from os import getcwd
import customtkinter as ctk
import sqlite3

global parent
global colour_palette
colour_palette = {"bgteal": "#BEE9E8", "bgblue": "#CAE9FF", "fgteal": "#62B6CB", "fgblue": "#5FA8D3", "dark": "#1B4965"}
global name
name = "Cadenza"
#########################################################################################################

#########################################################################################################
# Classes

class GUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("580x388")
        #self.resizable(False, False)
        self.title(name)
        self.configure(bg = "blue")

    def Label(self):
        self.backGroundImage = tk.PhotoImage(file = getcwd()+"\\Images\\solid-color-image.png")
        self.backGroundImageLabel = tk.Label(self, image = self.backGroundImage)
        self.backGroundImageLabel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.titleLabel = tk.Label(self, text = name, font = ("Arial", 30, "bold"), bg = colour_palette["bgblue"], fg = colour_palette["dark"])
        self.titleLabel.place(relx = 0.5, y=30, anchor = tk.CENTER)

class Take:

    def __init__(self, fs, seconds, user, song, take, audio_file):
        self.fs = fs
        self.seconds = seconds
        self.user = user
        self.song = song
        self.take = take
        self.file = audio_file
        
    def record(self):
        self.audio = sd.rec(int(self.seconds*self.fs), samplerate=self.fs, channels=2)
        sd.wait()
        write(self.file, self.fs, self.audio)

    def choose(self):
        conn = sqlite3.connect(getcwd()+"\\Files.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT Projectname FROM Songs WHERE Creator = ?''', (self.user,),)
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        choose(result)

    def set_audio(self, new):
        self.file = new

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

def default_screen():
    for widget in parent.winfo_children():
        if type(widget) != tk.Menu:
            widget.destroy()

    frame2 = tk.Frame(parent)
    frame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Create and place the record button
    record_button = tk.Button(frame2, text="Record", command=lambda: audio_input(True))
    record_button.grid(row=0,column=1,padx=(5, 5))


    # Create and place the choose button
    choose_button = tk.Button(frame2, text="Choose", command=lambda: audio_input(False))
    choose_button.grid(row=0,column=0,padx=(5, 5))


def audio_input(recording):
    new_take = Take(44100, 3, "Dev", "", 0, "test.wav")
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
    gui.mainloop()
    gui.main.wm_attributes("-transparentcolor", 'blue')