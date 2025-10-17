class Note:
    notes = []
    time = 0

    def __init__(self, start, pitch):
        self.start = start
        self.pitch = pitch
        Note.notes.append(self)

    def __str__(self):
        string = self.pitch + " from " + str(self.start) + " to " + str(self.end)
        return string
    
    def to_string(self):
        return self.pitch + "," + str(self.start) + "," + str(self.end)

    def get_start(self):
        return self.start
    
    def set_start(self, new):
        self.start = new
        self.duration = self.end - self.start

    def get_end(self):
        return self.end
    
    def set_end(self, new):
        self.end = new
        self.duration = self.end - self.start

    def get_pitch(self):
        return self.pitch
    
    def set_pitch(self, new):
        self.pitch = new




Note.time = 8
Note(1,"c4").set_end(4)
Note(4,"f5").set_end(4)
Note(4,"e7").set_end(8)

def save(filepath, load=False):
    if load:
        with open(filepath, "r") as f:
            raw_notes = f.readlines()
        for i in range(len(raw_notes)):
            temp = raw_notes[i]
            temp = temp.rstrip("\n")
            temp_list = temp.split(",")
            if temp_list[0] != "r":
                add_note(temp_list[0], float(temp_list[1]), float(temp_list[2]))
        notes = Note.notes
    else:
        notes = Note.notes
        text = ""
        for note in notes:
            text += note.to_string() + "\n"
        text = text.rstrip("\n")
        with open(filepath, "w") as f:
            f.write(text)
    return notes

def add_note(pitch, start, end):
    temp = Note(start, pitch)
    temp.set_end(end)
print("Original Notes")
for note in Note.notes:
    print(note)

save("test.txt")

Note.notes = []
print("Notes removed from program")
print(Note.notes)

save("test.txt", load=True)
print("Notes after loading")
for note in Note.notes:
    print(note)
