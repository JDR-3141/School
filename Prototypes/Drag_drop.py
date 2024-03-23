import tkinter as tk
from tkinter.constants import *
import tkinter_dndr as dndr

window = tk.Tk()
window.title("Test")
window.geometry("480x480")
window.maxsize(480, 480)
window.minsize(480,480)
canvas = tk.Canvas(window, width=440, height=20,bg="black")
canvas.place(x=20,y=100,width=440, height=20)
instance = dndr.DragDropResizeWidget(canvas)
instance.make_draggable_and_resizable()
window.mainloop()