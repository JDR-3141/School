class Note:
    notes = []
    time = 0

    def __init__(self, start, pitch):
        self.start = start
        self.pitch = pitch
        if self.start != None:
            Note.notes.append(self)

    def __str__(self):
        string = str(self.pitch) + " from " + str(self.start) + " to " + str(self.end) + " with duration " + str(self.duration)
        return string

    def get_start(self):
        return self.start
    
    def set_start(self, new):
        self.start = new
        self.duration = self.end - self.start

    def get_end(self):
        return self.end
    
    def get_duration(self):
        return self.duration
    
    def set_end(self, new):
        self.end = new
        if self.start != None:
            self.duration = self.end - self.start

    def get_pitch(self):
        return self.pitch
    
    def set_pitch(self, new):
        self.pitch = new

# Note.time = 8
# Note(1,4,"c4")
# Note(4,4,"f5")
# Note(4,4,"e7")
# for note in Note.notes:
#     print(note)