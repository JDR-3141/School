import tkinter as tk

class Square:
    
    def __init__(self, x, y, state, colour):
        self.x = x
        self.y = y
        self.state = state
        self.colour = colour
        self.image = canvas.create_rectangle(60*self.x, 60*self.y, 60*self.x+60, 60*self.y+60, fill=self.colour)

    def glow(self):
        reference = {
            "white":"red1",
            "#3BD129":"red3"}
        canvas.itemconfig(self.image, fill = reference[self.colour])

    def unglow(self):
        canvas.itemconfig(self.image, fill = self.colour)

window = tk.Tk()
window.title("Chess")
window.geometry("480x480")
window.maxsize(480, 480)
window.minsize(480,480)
global canvas
canvas = tk.Canvas(window, width=480, height=480)
