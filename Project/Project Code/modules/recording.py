from classes import Take
from modules.note_recognition import STFT
from modules.save_notes import save

def audio_input(new_song, gui, user, record, mode=False):
    new_take = Take(44100, 3, "", 0, gui, "4/4", STFT, user, save)
    gui.add_take(new_take)
    new_take.set_record(record)
    if new_song:
        gui.recording_screen(record)
        #new_take.record()
    else:
        #new_take.choose_song(new_take.choose_take, record)
        if mode:
            next_func = new_take.choose_take
        else:
            next_func = new_take.find_next_available_take
        new_take.choose_song(next_func)#, record)
    #new_take.get_notes()
