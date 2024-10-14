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
    
    def recording_screen(self):
        for widget in self.winfo_children():
            if type(widget) != tk.Menu:
                widget.destroy()

        self.background_Label()

        # Create a frame for the inputs
        input_frame = self.Frame(self, "bgblue")
        input_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        song_name_label = self.Label(input_frame, text="Song Name:")
        song_name_label.grid(row=0, column=0, pady=5, padx=5)
        song_name_entry = self.Entry(input_frame, width=20, show="")
        song_name_entry.grid(row=0, column=1, pady=5, padx=5)

        tempo_label = self.Label(input_frame, text="Tempo:")
        tempo_label.grid(row=1, column=0, pady=5, padx=5)
        tempo_entry = self.Entry(input_frame, width=10, show="")
        tempo_entry.grid(row=1, column=1, pady=5, padx=5)

        key_label = self.Label(input_frame, text="Key:")
        key_label.grid(row=2, column=0, pady=5, padx=5)
        key_note_var = tk.StringVar(value="C")
        key_note_dropdown = tk.OptionMenu(input_frame, key_note_var, "C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B")
        key_note_dropdown.grid(row=2, column=1, pady=5, padx=5)

        tonality_var = tk.StringVar(value="Major")
        tonality_dropdown = tk.OptionMenu(input_frame, tonality_var, "Major", "Minor")
        tonality_dropdown.grid(row=2, column=2, pady=5, padx=5)

        time_sig_label = self.Label(input_frame, text="Time Signature:")
        time_sig_label.grid(row=3, column=0, pady=5, padx=5)
        top_var = tk.StringVar(value="4")
        top_dropdown = tk.OptionMenu(input_frame, top_var, "2", "3", "4", "5", "6", "7", "8")
        top_dropdown.grid(row=3, column=1, pady=5, padx=5)

        bottom_var = tk.StringVar(value="4")
        bottom_dropdown = tk.OptionMenu(input_frame, bottom_var, "1", "2", "4", "8", "16")
        bottom_dropdown.grid(row=3, column=2, pady=5, padx=5)

        time_label = self.Label(input_frame, text="Bars to record:")
        time_label.grid(row=4, column=0, pady=5, padx=5)
        time_entry = self.Entry(input_frame, width=20, show="")
        time_entry.grid(row=4, column=1, pady=5, padx=5)


        # Record Button
        def on_record():
            song_name = song_name_entry.get()
            tempo = tempo_entry.get()
            key_note = key_note_var.get()
            tonality = tonality_var.get()
            time_signature = (top_var.get(), bottom_var.get())
            bars = time_entry.get()

            if song_name and tempo.isdigit() and bars.isdigit():
                if self.take.check_song_name(song_name):
                    self.take.record(song_name, int(tempo), key_note, tonality, time_signature, bars)
                else:
                    tk.messagebox.showerror("Error", "Song name already exists. Please choose a different name.")
            else:
                tk.messagebox.showerror("Error", "Please fill out all fields correctly")

        record_button = self.Button(input_frame, text="Record", command=on_record)
        record_button.grid(row=4, column=0, columnspan=3, pady=10)    

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
            files.insert(tk.END, choices[item][1])
        yscrollbar.config(command = files.yview)
        button = self.Button(self, text = "Open", command = lambda:function(choices[files.curselection()[0]]))
        button.pack(fill = "x", side = "bottom")

    def add_take(self, take):
        self.take = take

    def note_gui(self):
        for widget in self.winfo_children():
            if type(widget) != tk.Menu:
                widget.destroy()

        # Create a frame to hold the canvas and scrollbar
        canvas_frame = self.Frame(self)
        canvas_frame.pack(fill=tk.BOTH, expand=True)

        # Create a canvas widget
        self.canvas = tk.Canvas(canvas_frame, bg=GUI.colour_palette["bgblue"])
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a horizontal scrollbar linked to the canvas (optional)
        h_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.configure(xscrollcommand=h_scrollbar.set)

        # Create a frame inside the canvas to hold the content
        # self.content_frame = tk.Frame(self.canvas, bg=GUI.colour_palette["bgblue"])
        # self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")

        # Configure the canvas to resize with the window
        self.content_frame.bind("<Configure>", self.on_frame_configure)
    
        for line in range(40,480,int(480/24)):
            colour_ref = {0:"grey", 20:"grey", 40:"black", 60:"grey"}
            note_ref = {0:"e",20:"d",40:"c",60:"b",80:"a",100:"g",120:"f"}
            octave_ref = {-1:"5",0:"4",1:"3",2:"2"}
            self.canvas.create_line(0,line,480,line,fill="grey")
            self.canvas.create_line(line,0,line,480,fill=colour_ref[line%80])
            self.canvas.create_text(line+10,20,text=str(int(line/20)-1))
            self.canvas.create_text(20,line+10,text=note_ref[line%140]+octave_ref[(line-60)//140])

    #<140=0
    #140-280=1
    #280-420=2
    #420=3
    
    #140, 140, 140
    def add_note(canvas, start, end, pitch):
        note_ref={"c":0,"d":20,"e":40,"f":60,"g":80,"a":100,"b":120}
        octave_ref={"2":0,"3":140,"4":280,"5":420}
        canvas.create_rectangle(start*20+20, 480-note_ref[pitch[0]]-octave_ref[pitch[1]]\
                , end*20+40, 480-note_ref[pitch[0]]-octave_ref[pitch[1]]-20, fill="grey")

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))        

# gui = GUI(None)
# gui.check_audio()
# gui.mainloop()