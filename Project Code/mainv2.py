#########################################################################################################
# Imports and globals

#from tkinter import messagebox
from classes.GUI import GUI
from modules.recording import audio_input

#########################################################################################################

#########################################################################################################
# Functions

if __name__ == "__main__":
    gui = GUI(audio_input)
    gui.Label()
    gui.default_screen()
    gui.mainloop()
    gui.main.wm_attributes("-transparentcolor", 'blue')