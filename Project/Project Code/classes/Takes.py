import sounddevice as sd 
import sqlite3
from os import getcwd
from scipy.io.wavfile import write, read
import lilypond
import subprocess

import sys

sys.path.append(getcwd()+"\\Project\\Project Code")

#from modules.note_recognition import STFT
# from classes.Notes import Note
# from modules.lilypond import convert

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
        self.key = None
        
    def record(self, song_name, tempo, key_note, tonality, time_signature, time):
        self.time = time_signature[0] + "/" + time_signature[1]
        self.tempo = tempo
        self.key = key_note + " \\" + tonality.lower()
        self.song = song_name
        self.seconds = time
        self.audio = sd.rec(int(self.seconds*self.fs), samplerate=self.fs, channels=1)
        sd.wait()
        self.file = getcwd()+"\\Project\\Assets\\"+self.user+"-"+self.song+"-Take"+self.take+".wav"
        write(self.file, self.fs, self.audio)
        self.get_notes()

    def save_to_db(self):
        conn = sqlite3.connect(getcwd()+"\\Project\\Assets\\Files.db")
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Takes(SongID, Takenum, Time, Tempo, Key_note, Key_tonality, Audio_filename) VALUES(?,?,?,?,?,?,?)''', (self.song, self.take, self.time, self.tempo, self.key.split(" ")[0], self.key.split(" ")[1], self.file.split("\\")[-1]),)


    def choose_take(self, song):
        conn = sqlite3.connect(getcwd()+"\\Project\\Assets\\Files.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT Audio_filename, Takenum, Time, Tempo, Key_note, Key_tonality FROM Takes WHERE SongID = ?''', (song[0],),)
        self.song = song[1]
        self.result = cursor.fetchall()
        conn.commit()
        conn.close
        self.gui.choose(self.result, self.get_notes)

    def choose_song(self):
        conn = sqlite3.connect(getcwd()+"\\Project\\Assets\\Files.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT SongID, Projectname FROM Songs WHERE Creator = ?''', (self.user.get_username(),),)
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        self.gui.choose(result, self.choose_take)

    

    def get_notes(self, file=False):
        if file:
            self.file = getcwd() + "\\Project\\Assets\\" +file[0]
            # print(file[0])
            # print(self.result)
            self.time = file[2]
            self.tempo = file[3]
            self.key = file[4] + " " + file[5]
        self.fs, self.data = read(self.file)
        self.text = self.STFT(self.data, 1024, 512, self.fs, self)
        #self.text = convert(Note.notes())
        print(self.text)
        self.save()

    def get_key(self):
        return self.key
    
    def get_tempo(self):
        return self.tempo
        

    def set_audio(self, new):
        self.file = new

    def get_time(self, mode=2):
        if mode == 0:
            return int(self.time[0])
        elif mode == 1:
            return int(self.time[-1])
        else:
            return self.time
        
    def save(self):
        self.text_file = self.file[:-4] + ".ly"
        with open(self.text_file, "w") as f:
            f.write(self.text)
        subprocess.run([lilypond.executable(), self.text_file])

    def check_song_name(self, name):
        conn = sqlite3.connect(getcwd()+"\\Project\\Assets\\Files.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT Projectname FROM Songs WHERE Creator = ?''', (self.user.get_username(),),)
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        for i in result:
            if i[0] == name:
                return False
        return True