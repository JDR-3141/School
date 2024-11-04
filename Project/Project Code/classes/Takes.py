#import sounddevice as sd 
import sqlite3
from os import getcwd
from scipy.io.wavfile import write, read
import lilypond
import subprocess
import sounddevice as sd
import shutil

import sys

sys.path.append(getcwd()+"\\Project\\Project Code")

#from modules.note_recognition import STFT
# from classes.Notes import Note
# from modules.lilypond import convert
#from modules.save_notes import save

class Take: ################################################################### 

    def __init__(self, fs, seconds, song, take, gui, time, STFT, user, save):
        self.fs = fs
        self.seconds = seconds
        self.song = song
        self.take = take
        self.gui = gui
        self.time = time
        self.STFT = STFT
        self.user = user
        self.key = None
        self.to_record = None
        self.save_load = save
        
    def record(self, song_name, tempo, key_note, tonality, time_signature, time, record, take):

        self.time = time_signature[0] + "/" + time_signature[1]
        self.tempo = int(tempo)
        self.key = key_note + " \\" + tonality.lower()
        self.song = song_name
        #print(type(time), type(tempo), type(time_signature[0]), type(self.fs))
        #self.bars = int(time)
        self.seconds = int(time) * (60 / self.tempo) * int(time_signature[0])
        ######################################################### TEMPORARY!!
        self.take = str(take)
        self.file = getcwd()+"\\Project\\Assets\\"+self.user.get_username()+"-"+self.song+"-Take"+self.take+".wav"
        #self.gui.record(int(self.seconds*self.fs), self.fs)
        #self.gui.record(self.seconds, self.get_time(0), self.fs)
        if record:
            self.audio = sd.rec(int(self.seconds*self.fs), samplerate=self.fs, channels=1)
            sd.wait()
            write(self.file, self.fs, self.audio)
            self.get_notes()
        else:
            self.gui.import_file() # Next we need to call self.gui to input an external audio file here and set self.file to the changed file path
        

    def import_file(self, file_name):
        shutil.copy(file_name, self.file)
        self.get_notes()

    def save_audio(self, audio):
        self.audio = audio
        write(self.file, self.fs, self.audio)
        self.get_notes()

    def save_to_db(self):
        conn = sqlite3.connect(getcwd()+"\\Project\\Assets\\Files.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT TakeID FROM Takes''')
        result = cursor.fetchall()
        cursor.execute('''SELECT Takes FROM Songs WHERE SongID = ?''', (self.songID,))
        result1 = cursor.fetchall()[0]
        conn.commit()
        conn.close()
        self.takeID = str(len(result)+1)
        print(str(int(result1[0])+1))
        self.take = 1 + int(result1[0])
        conn = sqlite3.connect(getcwd()+"\\Project\\Assets\\Files.db")
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Takes(TakeID, SongID, Takenum, Time, Tempo, Key_note, Key_tonality) VALUES(?,?,?,?,?,?,?)''',\
                        (self.takeID, self.songID, self.take, self.time, self.tempo, self.key.split(" ")[0], self.key.split(" ")[1]),)
        cursor.execute('''UPDATE Songs SET Takes = ? WHERE SongID = ?''', (str(int(result1[0])+1), self.songID,),)
        conn.commit()
        conn.close()



    def get_notes(self, file=False):
        if file:
            self.file = file[0]
            self.file = getcwd() + "\\Project\\Assets\\" +file[0]
            # print(file[0])
            # print(self.result)
            self.time = file[2]
            self.tempo = file[3]
            self.key = file[4] + " " + file[5]
        self.fs, self.data = read(self.file)
        #self.STFT(self.data, 1024, 512, self.fs)
        self.text = self.STFT(self.data, 1024, 512, self.fs, self)
        self.note_file = self.file[:-4] + ".txt"
        #self.text = convert(Note.notes())
        #print(self.text)
        self.notes = self.save_load(self.note_file)
        self.graphic()

    def choose_take(self, song):
        conn = sqlite3.connect(getcwd()+"\\Project\\Assets\\Files.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT Time, Takenum, Tempo, Key_note, Key_tonality FROM Takes WHERE SongID = ?''', (song[0],),)
        self.songID = song[0]
        self.song = song[1]
        self.result = cursor.fetchall()
        cursor.execute('''SELECT Takes FROM Songs WHERE SongID = ?''', (song[0],),)
        result1 = cursor.fetchall()[0]
        conn.commit()
        conn.close
        self.take = 1 + int(result1[0])
        self.gui.choose(self.result, self.load)

    def choose_song(self, next_func):
        conn = sqlite3.connect(getcwd()+"\\Project\\Assets\\Files.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT SongID, Projectname FROM Songs WHERE Creator = ?''', (self.user.get_username(),),)
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        self.gui.choose(result, next_func)

    def find_next_available_take(self, result):
        conn = sqlite3.connect(getcwd()+"\\Project\\Assets\\Files.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT Takenum FROM Takes WHERE SongID = ?''', (str(result[0]),),)
        result1 = cursor.fetchall()
        conn.commit()
        conn.close()
        take_num = max(result1[0])+1
        self.take=take_num
        self.songID = result[0]
        self.gui.recording_screen(self.to_record, result[1], take_num)


        
        


    def load(self, file=False):
        self.file = getcwd() + "\\Project\\Assets\\" + self.user.get_username()+\
            "-"+self.song+"-Take"+str(file[1])+".wav"
        # print(file[0])
        # print(self.result)
        self.time = file[0]
        self.take = file[1]
        self.tempo = file[2]
        self.key = file[3] + " " + file[4]
        #self.bars = int(file[5])
        #self.fs, self.data = read(self.file)
        #self.text = self.STFT(self.data, 1024, 512, self.fs, self)
        #self.text = convert(Note.notes())
        #print(self.text)
        #self.save()

        #print("success")
        self.note_file = self.file[:-4] + ".txt"
        self.notes = self.save_load(self.note_file, load=True)


        conn = sqlite3.connect(getcwd()+"\\Project\\Assets\\Files.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT Takes FROM Songs WHERE SongID = ?''', (str(self.songID),),)
        result1 = cursor.fetchall()
        conn.commit()
        conn.close()
        take_num = int(result1[0][0])+1


        self.take = take_num
        self.file = getcwd() + "\\Project\\Assets\\" + self.user.get_username()+"-"+self.song+"-Take"+str(self.take)+".wav"
        self.text_file = self.file[:-4] + ".ly"
        self.image_file = self.file[:-4] + ".pdf"
        self.note_file = self.file[:-4] + ".txt"
        self.graphic()

    def get_key(self, lilypond):
        if lilypond:
            temp = self.key.split(" ")
            temp[0] = temp[0].lower()
            temp[0] = temp[0].replace("#", "is")
            temp[0] = temp[0].replace("b", "es")
            return temp[0] + " " + temp[1]
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
        
    def set_record(self, new):
        self.to_record = new
        
    def lilypond(self, notes):
        self.save_to_db()
        self.file = getcwd() + "\\Project\\Assets\\" + self.user.get_username()+"-"+self.song+\
            "-Take"+str(self.take)+".wav"
        self.text = self.STFT(mode=True, take=self)
        self.notes = notes
        self.notes = self.save_load(self.note_file)
        self.text_file = self.file[:-4] + ".ly"
        self.image_file = self.file[:-4] + ".pdf"
        with open(self.text_file, "w") as f:
            f.write(self.text)
        subprocess.run([lilypond.executable(), self.text_file])
        shutil.move(getcwd() + "\\" + self.user.get_username()+"-"+self.song+"-Take"+str(self.take)+".pdf", self.image_file)
        self.gui.display_pdf(self.image_file)

    def check_song_name(self, name):
        conn = sqlite3.connect(getcwd()+"\\Project\\Assets\\Files.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT Projectname FROM Songs WHERE Creator = ?''', (self.user.get_username(),),)
        result = cursor.fetchall()
        cursor.execute('''SELECT SongID FROM Songs''')
        result1 = cursor.fetchall()
        conn.commit()
        conn.close()
        self.songID = max(result1)[0]+1
        for i in result:
            if i[0] == name:
                return False
        conn = sqlite3.connect(getcwd()+"\\Project\\Assets\\Files.db")
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Songs (SongID, Creator, Projectname, Takes) VALUES (?, ?, ?, ?)''', (self.songID, self.user.get_username(), name, 0),)
        conn.commit()
        conn.close()
        return True
    

    def graphic(self):
        self.gui.note_gui(self.notes)
######################################################## In case of errors check here
# def get_notes():
#     from classes.Notes import Note
#     return Note.notes()