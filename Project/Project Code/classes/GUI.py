import tkinter as tk
from os import getcwd
from time import sleep
import sys

sys.path.append(getcwd()+"\\Project\\Project Code")

#from classes.Takes import Take
from modules.login import validate_login, validate_signup


class GUI(tk.Tk):

    colour_palette = {"bgteal": "#BEE9E8", "bgblue": "#CAE9FF", "fgteal": "#62B6CB", "fgblue": "#5FA8D3", "dark": "#1B4965"}
    name = "Cadenza"
    gui = None

    def __init__(self, audio_input):
        super().__init__()
        self.geometry("580x388")
        #self.resizable(False, False)
        self.title(GUI.name)
        self.configure(bg = GUI.colour_palette["bgblue"])
        self.audio_input = audio_input
        GUI.gui = self 

        menu = tk.Menu(self)
        item = tk.Menu(menu)
        item.add_command(label="View details")#, command=lambda: view_details())
        item.add_command(label="Change details")#, command=lambda: change_details())
        menu.add_cascade(label="Options", menu = item)
        self.config(menu=menu)
        #self.login()
        #print("CADENZA VERSION 0.07689")


    def background_Label(self):
        self.backGroundImage = tk.PhotoImage(file = getcwd()+"\\Images\\solid-color-image.png")
        self.backGroundImageLabel = tk.Label(self, image = self.backGroundImage)
        self.backGroundImageLabel.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.titleLabel = tk.Label(self, text = GUI.name, font = ("Arial", 30, "bold"), bg = GUI.colour_palette["bgblue"], fg = GUI.colour_palette["dark"])
        self.titleLabel.pack(side=tk.TOP)


    def Label(self, parent, text, variable=False):
        if variable:
            label = tk.Label(parent, textvariable = text, background = GUI.colour_palette["bgblue"])
        else: 
            label = tk.Label(parent, text = text, background = GUI.colour_palette["bgblue"])
        return label

    def Button(self, parent, text, command):
        button = tk.Button(parent, text = text, background= GUI.colour_palette["fgblue"], foreground = GUI.colour_palette["dark"], activebackground = GUI.colour_palette["fgteal"], activeforeground = GUI.colour_palette["dark"], font = ("Arial", 15, "bold")) 
        if command:
            button.configure(command=command)
        return button
    
    def Frame(self, parent, colour):
        frame = tk.Frame(parent)
        frame.configure(bg = GUI.colour_palette[colour])
        return frame
    
    def Entry(self, parent, width, show):
        entry = tk.Entry(parent, font="Arial 15", show=show)
        if width != False:
            entry.configure(width=width)
        return entry

    def import_audio(self):
        from classes.Users import User
        for widget in self.winfo_children():
            if type(widget) != tk.Menu:
                widget.destroy()

        self.background_Label()

        frame2 = GUI.Frame(self, self, "bgblue")
        frame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create and place the record button
        record_button = self.Button(frame2,"Record", lambda: self.audio_input(True, self, User.user))
        record_button.grid(row=0,column=1,padx=(5, 5))


        # Create and place the choose button
        choose_button = self.Button(frame2,"Choose",lambda: self.audio_input(False, self, User.user))
        choose_button.grid(row=0,column=0,padx=(5, 5))

    def count(self):
        for widget in self.winfo_children():
            if type(widget) != tk.Menu:
                widget.destroy

        self.background_Label()
        
        count_var = tk.StringVar()
        n = 1
        count_var.set(str(n))
        count = GUI.Label(self, count_var, True)
        count.pack()

        for i in range(self.take.get_time(0)):
           sleep(60/self.take.get_tempo())
           n += 1
           count_var.set(str(n))
        ## Add here later

    def check_audio(self):
        for widget in self.winfo_children():
            if type(widget) != tk.Menu:
                widget.destroy

        self.background_Label()

        outerframe = self.Frame(self, "bgblue")
        outerframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        audio_player = self.Frame(outerframe, "fgblue")
        audio_player.grid(row=0,column=0,padx=(5, 5))

        # Create and place the play button
        play_button = self.Button(audio_player,"Play", lambda: print("yay")) #lambda: self.audio_input.play_audio(self.audio_input.audio_file_path, self))
        play_button.grid(row=0,column=0,padx=(5, 5))





    def show(self, password_entry, show_button, hide_button):
        password_entry.config(show='')
        show_button.grid_forget()
        hide_button.grid(row=0,column=1)

    def hide(self, password_entry, show_button, hide_button):
        password_entry.config(show='*')
        hide_button.grid_forget()
        show_button.grid(row=0,column=1)

    def login(self):
        for widget in self.winfo_children():
            if type(widget) != tk.Menu:
                widget.destroy()

        self.background_Label()

        frame2 = tk.Frame(self)
        frame2.configure(bg = GUI.colour_palette["bgblue"])
        frame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        username_label = self.Label(self, text="Username:")
        username_label.pack()

        username_entry = self.Entry(self, False, "")
        username_entry.pack()

        # Create and place the password label and entry
        password_label = self.Label(self, text="Password:")
        password_label.pack()

        frame1 = self.Frame(self, "bgblue")
        frame1.pack()

        password_entry = self.Entry(frame1, 14, "*")  # Show asterisks for password
        password_entry.grid(row=0,column=0)

        show_button = self.Button(frame1, text="Show", command=lambda: self.show(password_entry, show_button, hide_button))
        show_button.grid(row=0,column=1)

        hide_button = self.Button(frame1, text="Hide", command=lambda: self.hide(password_entry, show_button, hide_button))

        frame3 = tk.Frame(self)
        frame3.configure(bg = GUI.colour_palette["bgblue"])
        frame3.pack()

        # Create and place the login button
        login_button = self.Button(frame2, text="Log in", command=lambda: validate_login(username_entry, password_entry))
        login_button.grid(row=0,column=1,padx=(5, 5))

        # Create and place the login button
        signin_button = self.Button(frame2, text="Sign up", command=lambda: validate_signup(username_entry, password_entry))
        signin_button.grid(row=0,column=0,padx=(5, 5))


    def choose(self, choices, function):
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
        button = self.Button(self, text = "Open", command = lambda:function(files.curselection()[0]))
        button.pack(fill = "x", side = "bottom")

    def add_take(self, take):
        self.take = take

# gui = GUI(None)
# gui.check_audio()
# gui.mainloop()