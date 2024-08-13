import tkinter as tk
from os import getcwd



class GUI(tk.Tk):

    GUI.colour_palette = {"bgteal": "#BEE9E8", "bgblue": "#CAE9FF", "fgteal": "#62B6CB", "fgblue": "#5FA8D3", "dark": "#1B4965"}
    name = "Cadenza"

    def __init__(self, audio_input):
        super().__init__()
        self.geometry("580x388")
        #self.resizable(False, False)
        self.title(GUI.name)
        self.configure(bg = GUI.colour_palette["bgblue"])
        self.audio_input = audio_input

        menu = tk.Menu(self)
        item = tk.Menu(menu)
        item.add_command(label="View details")#, command=lambda: view_details())
        item.add_command(label="Change details")#, command=lambda: change_details())
        menu.add_cascade(label="Options", menu = item)
        self.config(menu=menu)
        print("CADENZA VERSION 0.07689")


    def Label(self):
        self.backGroundImage = tk.PhotoImage(file = getcwd()+"\\Images\\solid-color-image.png")
        self.backGroundImageLabel = tk.Label(self, image = self.backGroundImage)
        self.backGroundImageLabel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.titleLabel = tk.Label(self, text = GUI.name, font = ("Arial", 30, "bold"), bg = GUI.colour_palette["bgblue"], fg = GUI.colour_palette["dark"])
        self.titleLabel.place(relx = 0.5, y=30, anchor = tk.CENTER)

    def Button(self, parent, text, command):
        button = tk.Button(parent, text = text, background= GUI.colour_palette["fgblue"], foreground = GUI.colour_palette["dark"], activebackground=colour_palette["fgteal"], activeforeground=colour_palette["dark"], font = ("Arial", 15, "bold")) 
        if command:
            button.configure(command=command)
        return button


    def default_screen(self):
        for widget in self.winfo_children():
            if type(widget) != tk.Menu:
                widget.destroy()

        self.Label()

        frame2 = tk.Frame(self)
        frame2.configure(bg = GUI.colour_palette["bgblue"])
        frame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create and place the record button
        record_button = self.Button(frame2,"Record", lambda: self.audio_input(True, self))
        record_button.grid(row=0,column=1,padx=(5, 5))


        # Create and place the choose button
        choose_button = self.Button(frame2,"Choose",lambda: self.audio_input(False, self))
        choose_button.grid(row=0,column=0,padx=(5, 5))

    def choose(self, choices):
        for widget in self.winfo_children():
            if type(widget) != tk.Menu:
                widget.destroy()
        result = [i+1 for i in range(len(choices))]
        yscrollbar = tk.Scrollbar(self)
        yscrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        files = tk.Listbox(self, selectmode = "single",yscrollcommand = yscrollbar.set)
        files.pack(padx = 10, pady = 10, expand = tk.YES, fill = "both")
        for item in range(len(result)):
            files.insert(tk.END, choices[item])
        yscrollbar.config(command = files.yview)
        button = tk.Button(self, text = "Open", command = lambda:print(choices[files.curselection()[0]][0]))
        button.pack(fill = "x", side = "bottom")