class Note:
    notes = []
    time = 0
    pitch_list = ["c", "d", "e", "f", "g", "a", "b", "C", "D", "E", "F", "G", "A", "B"]

    def __init__(self, start, pitch):
        
        # if type(start) != int or start < 1 or pitch[0] not in Note.pitch_list:
        #     raise ValueError("Invalid input")
        self.start = start
        self.pitch = pitch
        self.colour = "grey"
        if self.start != None:
            Note.notes.append(self)

    def __str__(self):
        string = str(self.pitch) + " from " + str(self.start) + " to " + str(self.end) + " with duration " + str(self.duration)
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
    
    def get_duration(self):
        self.duration = self.end - self.start
        return self.duration
    
    def set_end(self, new):
        # if type(new) != int or new < self.start or new < 1:
        #     raise ValueError("Invalid input")
        self.end = new
        if self.start != None:
            self.duration = self.end - self.start

    def get_pitch(self, mode=False, flats=False):
        if mode:
            if self.pitch == "r":
               return "r"
            text = self.pitch[0:-1].lower()
            # text.replace("#", "is")
            # text.replace("b", "es")
            if flats:
                enharmonics = [["c#","db"], ["d#","eb"], ["f#","gb"], ["g#","ab"], ["a#","bb"]]
                for possible in enharmonics:
                    text = text.replace(possible[0], possible[1])
            octave = int(self.pitch[-1])
            if text == "c":
                octave += 1
            if octave > 4:
                for i in range(octave - 4):
                    text += "'"
                    if text[0] != "c":
                        text += "'"
            elif octave < 4:
                for i in range(4 - octave):
                    text += ","
                    if text[0] != "c":
                        text = text.rstrip(",")
            else:
                if text[0] != "c":
                    text += "'"
            return text
        return self.pitch
    
    def set_pitch(self, new):
        self.pitch = new

    def set_region(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def check_region(self, x, y):
        if x < self.x1 or x > self.x2 or y < self.y1 or y > self.y2:
            return False
        self.colour = "blue"
        return True
    
    def get_colour(self):
        return self.colour

    def set_colour(self):
        self.colour = "grey"
# Note.time = 8
# n = Note("s","#")
# n.set_end("d+s")
# print(n)
