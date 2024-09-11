from classes import Take

def audio_input(recording, gui, stft):
    new_take = Take(44100, 3, "Dev", "", 0, gui, stft)
    gui.add_take(new_take)
    if recording:
        new_take.record()
    else:
        new_take.choose()
    new_take.get_notes()
