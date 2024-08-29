#########################################################################################################
# Imports and globals

from tkinter import messagebox
from classes import *
from modules import *

#########################################################################################################

#########################################################################################################
# Functions

if __name__ == "__main__":
    gui = GUI(audio_input)
    gui.Label()
    gui.default_screen()
    gui.mainloop()
    gui.main.wm_attributes("-transparentcolor", 'blue')