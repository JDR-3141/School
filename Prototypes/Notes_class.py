class Note:
    notes = []
    time = 0

    def __init__(self, start, end, pitch):
        self.start = start
        self.end = end
        self.duration = end - start
        self.pitch = pitch
        Note.notes.append(self)

    def __str__(self):
        string = self.pitch

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
