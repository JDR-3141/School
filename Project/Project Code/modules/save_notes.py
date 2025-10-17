def save(filepath, load=False): # Load parameter determines whether to save or load
    if load:
        with open(filepath, "r") as f:
            raw_notes = f.readlines()
        for i in range(len(raw_notes)):
            temp = raw_notes[i]
            temp = temp.rstrip("\n")
            temp_list = temp.split(",")
            if temp_list[0] != "r":
                add_note(temp_list[0], float(temp_list[1]), float(temp_list[2]))
        notes = get_notes()
    else:
        notes = get_notes()
        text = ""
        for note in notes:
            text += note.to_string() + "\n"
        text = text.rstrip("\n")
        with open(filepath, "w") as f:
            f.write(text)
    return notes # Notes are returned independent of whether they are saved or loaded

def get_notes():
    from classes.Notes import Note # local import to avoid circular import
    return Note.notes

def add_note(pitch, start, end):
    from classes.Notes import Note
    temp = Note(start, pitch) # temporary variable as class list holds all notes
    temp.set_end(end)

