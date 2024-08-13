from classes import Take

def audio_input(recording, gui):
    new_take = Take(44100, 3, "Dev", "", 0, "test.wav", gui)
    if recording:
        new_take.record()
    else:
        new_take.choose()
