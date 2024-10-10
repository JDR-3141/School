from classes import Take
from modules.note_recognition import STFT

def audio_input(recording, gui, user):
    new_take = Take(44100, 3, "", 0, gui, "4/4", STFT, user)
    gui.add_take(new_take)
    if recording:
        new_take.record()
    else:
        new_take.choose_song()
    #new_take.get_notes()
