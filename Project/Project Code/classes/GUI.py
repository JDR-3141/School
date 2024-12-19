import tkinter as tk
from tkinter import filedialog
from os import getcwd
from time import sleep, time
import sys
import sounddevice as sd
import numpy as np
from tkinterPdfViewer import tkinterPdfViewer as pdf


sys.path.append(getcwd()+"\\Project\\Project Code")

#from classes.Takes import Take
from modules.login import validate_login, validate_signup
################################################################## Pass in save_notes file and implement during note_gui before calling lilypond


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
        self.logged_in = False
        GUI.gui = self 

        menu = tk.Menu(self)
        item = tk.Menu(menu)
        item.add_command(label="Logout", command=lambda: self.set_logged_in(False) or self.login())
        item.add_command(label="New Take", command=lambda: self.import_audio() if self.logged_in else self.login())
        menu.add_cascade(label="Options", menu = item)
        self.config(menu=menu)
        #self.login()
        #print("CADENZA VERSION 0.07689")

    def set_logged_in(self, new):
        self.logged_in = new
        return False



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
    
    def recording_screen(self, record, song=False, take=False):
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
        if song:
            song_name_entry.insert(0, song)
            song_name_entry.config(state="disabled")
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
        def on_record(record, song, take):
            song_name = song_name_entry.get()
            self.tempo = tempo_entry.get()
            key_note = key_note_var.get()
            tonality = tonality_var.get()
            time_signature = (top_var.get(), bottom_var.get())
            self.count_count = int(top_var.get())
            bars = time_entry.get()

            if song_name and self.tempo.isdigit() and bars.isdigit():
                args = [song_name, int(self.tempo), key_note, tonality, time_signature, bars, record]
                if self.take.check_song_name(song_name):
                    self.count(args, "1")
                elif song:
                    self.count(args, take)
                else:
                    tk.messagebox.showerror("Error", "Song name already exists. Please choose a different name.")
            else:
                tk.messagebox.showerror("Error", "Please fill out all fields correctly")


        record_button = self.Button(input_frame, text="Continue", command=lambda: on_record(record, song, take))
        record_button.grid(row=5, column=0, columnspan=3, pady=10)

    def import_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
        self.take.import_file(file_path)

    # def record(self, total_duration, count_number, samplerate=44100):
    #     # Clear the screen
    #     for widget in self.winfo_children():
    #         if not isinstance(widget, tk.Menu):
    #             widget.destroy()

    #     self.background_Label()

    #     # Create a label to display the count
    #     count_var = tk.StringVar()
    #     count_label = self.Label(self, text=count_var, variable=True)
    #     count_label.pack(pady=20)

    #     # Calculate the duration for each count cycle
    #     duration_per_count = total_duration / count_number

    #     # Prepare to record audio
    #     audio_data = []

    #     def start_recording():
    #         start_time = time()

    #         # Continue recording until the total duration is reached
    #         while time() - start_time < total_duration:
    #             for i in range(1, count_number + 1):
    #                 if time() - start_time >= total_duration:
    #                     break
    #                 count_var.set(str(i))
    #                 self.update_idletasks()
    #                 sleep(duration_per_count)

    #             # Record audio for the duration of one count cycle
    #             audio_chunk = sd.rec(int(samplerate * duration_per_count), samplerate=samplerate, channels=1, dtype='float64')
    #             sd.wait()
    #             audio_data.append(audio_chunk)

    #         # After recording, concatenate all audio chunks
    #         complete_audio = np.concatenate(audio_data, axis=0)
    #         # Process or save the complete_audio as needed

    #         self.take.save_audio(complete_audio)
            

    #     # Start the recording process
    #     self.after(0, start_recording)
        



    def import_audio(self):
        from classes.Users import User
        for widget in self.winfo_children():
            if type(widget) != tk.Menu:
                widget.destroy()

        self.background_Label()

        frame2 = GUI.Frame(self, self, "bgblue")
        frame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create and place the record button
        record_button = self.Button(frame2,"New Audio", lambda: self.record_or_import())
        record_button.grid(row=0,column=1,padx=(5, 5))


        # Create and place the choose button
        choose_button = self.Button(frame2,"Existing audio",lambda: self.audio_input(False, self, User.user, False, True))
        choose_button.grid(row=0,column=0,padx=(5, 5))

    def new_or_existing(self, record):
        from classes.Users import User
        for widget in self.winfo_children():
            if type(widget) != tk.Menu:
                widget.destroy()

        self.background_Label()

        frame2 = GUI.Frame(self, self, "bgblue")
        frame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create and place the record button
        record_button = self.Button(frame2,"New Song", lambda: self.audio_input(True, self, User.user, record))
        record_button.grid(row=0,column=1,padx=(5, 5))


        # Create and place the choose button
        choose_button = self.Button(frame2,"Existing song",lambda: self.audio_input(False, self, User.user, record))
        choose_button.grid(row=0,column=0,padx=(5, 5))

    def record_or_import(self):
        from classes.Users import User
        for widget in self.winfo_children():
            if type(widget) != tk.Menu:
                widget.destroy()

        self.background_Label()

        frame2 = GUI.Frame(self, self, "bgblue")
        frame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create and place the record button
        record_button = self.Button(frame2,"Record", lambda: self.new_or_existing(True))
        record_button.grid(row=0,column=1,padx=(5, 5))


        # Create and place the choose button
        choose_button = self.Button(frame2,"Import",lambda: self.new_or_existing(False))
        choose_button.grid(row=0,column=0,padx=(5, 5))

    def count(self, arguments, take):
        for widget in self.winfo_children():
            if type(widget) != tk.Menu:
                widget.destroy

        self.background_Label()
        
        count_var = tk.StringVar()
        n = 0
        count_var.set(str(n))
        count = GUI.Label(self,self, count_var, variable=True)
        count.pack()

        for i in range(self.count_count):
           sleep(60/int(self.tempo))
           n += 1
           count_var.set(str(n))
           self.update_idletasks()

        self.take.record(*arguments, take)
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

    # def note_gui(self):
    #     for widget in self.winfo_children():
    #         if type(widget) != tk.Menu:
    #             widget.destroy()

    #     # Create a frame to hold the canvas and scrollbar
    #     canvas_frame = self.Frame(self)
    #     canvas_frame.pack(fill=tk.BOTH, expand=True)

    #     # Create a canvas widget
    #     self.canvas = tk.Canvas(canvas_frame, bg=GUI.colour_palette["bgblue"], width=480, height=480)
    #     self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    #     # Create a horizontal scrollbar linked to the canvas (optional)
    #     h_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
    #     h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    #     self.canvas.configure(xscrollcommand=h_scrollbar.set)

    #     # Create a frame inside the canvas to hold the content
    #     # self.content_frame = tk.Frame(self.canvas, bg=GUI.colour_palette["bgblue"])
    #     # self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")

    #     # Configure the canvas to resize with the window
    #     self.content_frame.bind("<Configure>", self.on_frame_configure)
    
    #     for line in range(40,480,int(480/24)):
    #         colour_ref = {0:"grey", 20:"grey", 40:"black", 60:"grey"}
    #         note_ref = {0:"e",20:"d",40:"c",60:"b",80:"a",100:"g",120:"f"}
    #         octave_ref = {-1:"5",0:"4",1:"3",2:"2"}
    #         self.canvas.create_line(0,line,480,line,fill="grey")
    #         self.canvas.create_line(line,0,line,480,fill=colour_ref[line%80])
    #         self.canvas.create_text(line+10,20,text=str(int(line/20)-1))
    #         self.canvas.create_text(20,line+10,text=note_ref[line%140]+octave_ref[(line-60)//140])

    #<140=0
    #140-280=1
    #280-420=2
    #420=3
    
    #140, 140, 140
    def add_note(self, start, end, pitch, note):
        if pitch == "r":
            return
        note_ref = {'c': 240, 'b': 20, 'a#': 40, 'a': 60, 'g#': 80, 'g': 100, 'f#': 120, 'f': 140, 'e': 160, 'd#': 180, 'd': 200, 'c#': 220}
        octave_ref = {'8': -1, '7': 0, '6': 1, '5': 2, '4': 3, '3': 4, '2': 5, '1': 6, '0': 7}
        x1 = start*20-40
        y1 = 40+note_ref[pitch[:-1]]+240*octave_ref[pitch[-1]]
        x2 = end*20-20
        y2 = 40+note_ref[pitch[:-1]]+240*octave_ref[pitch[-1]]+20
        note.set_region(x1, y1, x2, y2)
        self.canvas.create_rectangle(start*20-40, 40+note_ref[pitch[:-1]]+240*octave_ref[pitch[-1]]\
                , end*20-20, 40+note_ref[pitch[:-1]]+240*octave_ref[pitch[-1]]+20, fill=note.get_colour())



    def note_gui(self, notes): # DATABASE THINGS AFTERWARDS!!!
        self.notes = notes
        self.width = int(self.notes[-1].get_end()*4)*20
        self.height = 80+12*8*20
        for widget in self.winfo_children():
            if type(widget) != tk.Menu:
                widget.destroy()

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)

        def on_content_click(event):

            x = self.canvas.canvasx(event.x)
            y = self.canvas.canvasy(event.y)
            #print(f"Clicked at: ({x}, {y})")
            for note in self.notes:
                if note.check_region(x, y):
                    self.note_to_edit = note
                    key_note_var.set(self.note_to_edit.get_pitch()[:-1])
                    octave_var.set(self.note_to_edit.get_pitch()[-1])
                    start_var.set(self.time_dict[self.note_to_edit.get_start()-0.75])
                    end_var.set(self.time_dict[self.note_to_edit.get_end()-0.75]) 
                    self.update_note_gui()
                    break
                    
        # Create a frame to contain the canvas and scrollbars
        frame = tk.Frame(self, width=500, height=350)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid_propagate(False)

        # Create a canvas widget
        self.canvas = tk.Canvas(frame, bg="white", width=self.width, height=self.height)
        #self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Create vertical and horizontal scrollbars linked to the canvas
        v_scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.canvas.yview)
        #v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        v_scrollbar.grid(row=0, column=1, sticky="ns")

        h_scrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        #h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        h_scrollbar.grid(row=1, column=0, sticky="ew")

        # Configure the canvas to work with the scrollbars
        self.canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        # Ensure the content frame is large enough and update the scroll region
        def configure_scroll_region(event=None):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self.canvas.bind("<Configure>", configure_scroll_region)

        # Bind the click event to the content_frame
        self.canvas.bind("<Button-1>", on_content_click) ############################################################## Detection of notes clicked, make method to check validity and then change note (also add delete), link up to Lilypond, save take ti database - DONE!!!

        sidebar_frame = tk.Frame(self, padx=10, pady=10)
        sidebar_frame.grid(row=0, column=1, sticky="nsew")

        tk.Label(sidebar_frame, text="Pitch").grid(row=0, column=0, sticky="e", pady=5, padx=5)
        key_note_var = tk.StringVar(value="C")
        key_note_dropdown = tk.OptionMenu(sidebar_frame, key_note_var, "C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B")
        key_note_dropdown.grid(row=0, column=1, sticky="w", pady=5)
        octave_var = tk.StringVar(value="4")
        octave_dropdown = tk.OptionMenu(sidebar_frame, octave_var, "0", "1", "2", "3", "4", "5", "6", "7", "8")
        octave_dropdown.grid(row=0, column=2, sticky="w", pady=5)
        #self.pitch_entry = tk.Entry(sidebar_frame).grid(row=0, column=1, pady=5, padx=5)

        tk.Label(sidebar_frame, text="Start").grid(row=1, column=0, sticky="e", pady=5, padx=5)
        times = []
        for line in range(40,self.width,20):
            #print(self.width)
            num = int(line/20)+2
            #print(num)
            times.append(str(num//4)+"."+str(num%4))
        raw_starts = [i/4 for i in range(1, 1+int(self.notes[-1].get_end()*4))]
        self.time_dict = dict(zip(raw_starts, times))
        self.reverse_dict = dict(zip(times, raw_starts))
        #print(self.time_dict)
        #print(times)

        start_var = tk.StringVar(value=times[0])
        start_dropdown = tk.OptionMenu(sidebar_frame, start_var, *times)
        start_dropdown.grid(row=1, column=1, sticky="w", pady=5, padx=5)


        #self.start_entry = tk.Entry(sidebar_frame).grid(row=1, column=1, pady=5, padx=5)

        tk.Label(sidebar_frame,text="End").grid(row=2, column=0, sticky="e", pady=5, padx=5)
        end_var = tk.StringVar(value=times[1])
        end_dropdown = tk.OptionMenu(sidebar_frame, end_var, *times)
        end_dropdown.grid(row=2, column=1, sticky="w", pady=5, padx=5)
        #self.end_entry = tk.Entry(sidebar_frame).grid(row=2, column=1, pady=5, padx=5)

        #tk.Button(sidebar_frame, command=self.update_note_gui, text="Add").grid(row=3, column=0, pady=10, padx=5)
        tk.Button(sidebar_frame, command=self.delete_note, text="Delete").grid(row=3, column=1, pady=10, padx=5)
        tk.Button(sidebar_frame, command=self.set_first_to_start, text="Set first to start").grid(row=3, column=2, pady=10, padx=5)

        tk.Button(sidebar_frame, command=lambda: self.change_note(start_var.get(), end_var.get(), key_note_var.get()+octave_var.get()), text="Update").grid(row=4, column=0, pady=10, padx=5)
        tk.Button(sidebar_frame, command=lambda: self.take.lilypond(self.notes), text="Finish").grid(row=4, column=1, pady=10, padx=5)

        # for i in self.notes:
        #     print(i)

        self.update_note_gui()


    def update_note_gui(self):
        self.canvas.delete("all")
        colour_ref = {0:"grey", 20:"grey", 40:"black", 60:"grey"}
        for line in range(40,self.width,20):
            #int(width/24)):
            
            
            self.canvas.create_line(line,0,line,self.height,fill=colour_ref[line%80])
            num = int(line/20)+2
            self.canvas.create_text(line+10,20,text=str(num//4)+"."+str(num%4))
            #print(line)

        note_ref = {0:"c",20:"b",40:"a#",60:"a",80:"g#",100:"g",120:"f#",140:"f",160:"e",180:"d#",200:"d",220:"c#"}
        octave_ref = {-1:"8",0:"7",1:"6",2:"5", 3:"4",4:"3",5:"2",6:"1",7:"0"}
        for line in range(40, 40+12*8*20+20, 20):
            self.canvas.create_line(0,line,self.width,line,fill="grey")
            #print(line)
            self.canvas.create_text(20,line+10,text=note_ref[(line-40)%240]+octave_ref[(line-60)//240])

        for note in self.notes:
            pitch = note.get_pitch().lower()
            start = note.get_start() * 4
            end = note.get_end() * 4 -1
            self.add_note(start, end, pitch, note)



    def delete_note(self):
        if self.note_to_edit != None:
            self.notes.remove(self.note_to_edit)
            self.note_to_edit = None
            self.update_note_gui()

    def change_note(self, start, end, pitch):
        if self.note_to_edit != None:
            if start < end:
                self.note_to_edit.set_start(self.reverse_dict[start]+0.75)
                self.note_to_edit.set_end(self.reverse_dict[end]+0.75)
                self.note_to_edit.set_pitch(pitch)
                self.note_to_edit.set_colour()
                self.update_note_gui()

    def display_pdf(self, pdf_path):
        for widget in self.winfo_children():
            if type(widget) != tk.Menu:
                widget.destroy()
        image = pdf.ShowPdf()
        show_image = image.pdf_view(self, pdf_location=pdf_path, width=70, height=100)
        show_image.pack()


    def set_first_to_start(self):
        displacement = 1 - self.notes[0].get_start()
        for note in self.notes:
            note.set_start(note.get_start()+displacement)
            note.set_end(note.get_end()+displacement)
        self.update_note_gui()





                

        # gui = GUI(None)
        # gui.check_audio()
        # gui.mainloop()