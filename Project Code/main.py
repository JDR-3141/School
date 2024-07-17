#########################################################################################################
# Imports

import sounddevice as sd 
from scipy.io.wavfile import write
import tkinter as tk
from os import getcwd
import customtkinter as ctk

#########################################################################################################

#########################################################################################################

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
        write(self.audio_file, self.fs, self.audio)

def default_screen():
    for widget in parent.winfo_children():
        if type(widget) != tk.Menu:
            widget.destroy()

    frame2 = ctk.CTkFrame(parent)
    frame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Create and place the record button
    record_button = ctk.CTkButton(frame2, text="Record")
    record_button.grid(row=0,column=1,padx=(5, 5))


    # Create and place the choose button
    choose_button = ctk.CTkButton(frame2, text="Choose")
    choose_button.grid(row=0,column=0,padx=(5, 5))


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
    # Create the main window
parent = ctk.CTk()
parent.title("Login Form")

# dimensions of the main window
parent.geometry("400x500")
parent.iconbitmap(getcwd()+"\\Icon.ico")

menu = tk.Menu(parent)
menu.configure()
item = tk.Menu(menu)
item.add_command(label="View details")
item.add_command(label="Change details")
menu.add_cascade(label="Options", menu = item)
parent.config(menu=menu)

# Start the Tkinter event loop
default_screen()
parent.mainloop()