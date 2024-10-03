import sounddevice as sd 
import sqlite3
from os import getcwd
from scipy.io.wavfile import write, read

import sys

sys.path.append(getcwd()+"\\Project\\Project Code")

#from modules.note_recognition import STFT
from classes.Users import User

class Take:

    def __init__(self, fs, seconds, song, take, gui, time, STFT, user):
        self.fs = fs
        self.seconds = seconds
        self.song = song
        self.take = take
        self.gui = gui
        self.time = time
        self.STFT = STFT
        self.user = user
        
    def record(self):
        self.audio = sd.rec(int(self.seconds*self.fs), samplerate=self.fs, channels=1)
        sd.wait()
        self.file = getcwd()+"\\"+self.user+"\\"+self.song+"\\"+self.take+".wav"
        write(self.file, self.fs, self.audio)

    def choose_take(self, song):
        conn = sqlite3.connect(getcwd()+"\\Files.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT Take FROM Takes WHERE Projectname = ?''', (song,),)
        result = cursor.fetchall()
        conn.commit()
        conn.close
        self.gui.choose(result, self.get_notes)

    def choose_song(self):
        conn = sqlite3.connect(getcwd()+"\\Files.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT Projectname FROM Songs WHERE Creator = ?''', (self.user,),)
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        self.gui.choose(result, self.choose_take)

    

    def get_notes(self, file=False):
        if file:
            self.file = file
        self.fs, self.data = read(self.file)
        self.STFT(self.data, 1024, 512, self.fs)
        

    def set_audio(self, new):
        self.file = new

    def get_time(self, mode=2):
        if mode == 0:
            return int(self.time[0])
        elif mode == 1:
            return int(self.time[-1])
        else:
            return self.time