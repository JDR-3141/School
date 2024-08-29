import sounddevice as sd 
import sqlite3
from os import getcwd
from scipy.io.wavfile import write, read

class Take:

    def __init__(self, fs, seconds, user, song, take, gui, stft):
        self.fs = fs
        self.seconds = seconds
        self.user = user
        self.song = song
        self.take = take
        self.gui = gui
        self.STFT = stft
        
    def record(self):
        self.audio = sd.rec(int(self.seconds*self.fs), samplerate=self.fs, channels=1)
        sd.wait()
        write(self.file, self.fs, self.audio)

    def choose(self):
        conn = sqlite3.connect(getcwd()+"\\Files.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT Projectname FROM Songs WHERE Creator = ?''', (self.user,),)
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        self.gui.choose(result)

    def get_notes(self, file):
        self.file = file
        self.fs, self.data = read(self.file)
        self.STFT(self.data, 1024, 512, self.fs)

    def set_audio(self, new):
        self.file = new