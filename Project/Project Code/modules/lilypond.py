# import sys
# from os import getcwd
# sys.path.append(getcwd()+"\\Project\\Project Code")



from classes.Notes import Note
from math import log


def highestPowerof2(n):
    ans = 1024
    print(n)
    while ans > n:
        ans /= 2
    return ans

    # p = int(log(n, 2))
    # return int(pow(2, p))

def convert(take):
    #print(5)
    
    for i in range(len(Note.notes)-1, 0, -1):
        if Note.notes[i].get_start() != Note.notes[i-1].get_end():
            temp = Note(Note.notes[i-1].get_end(),"r")
            temp.set_end(Note.notes[i].get_start())
            Note.notes.insert(i, temp)
            Note.notes.pop(-1)

    # for note in Note.notes:
    #     print(note)
    text = """
\\version "2.25.12"
\\new Voice \\with {
  \\remove Note_heads_engraver
  \\consists Completion_heads_engraver
  \\remove Rest_engraver
  \\consists Completion_rest_engraver
}
{
  \\clef treble
  """
    text += " \\time " + take.get_time() + "\n  \\key " + take.get_key(True) + "\n  "
    flat = False
    key_note = take.get_key(True).split(" ")[0]
    flats = ["bes", "ees", "aes", "des", "ges", "ces", "fes", "f"]
    if key_note in flats:
        flat = True
    in_a_bar = take.get_time(0)
    base = take.get_time(1)
    current_time = 1
    current_bar = 1
    for note in Note.notes:
        #print(6)
        text += str(note.get_pitch(True, flat))
        d = note.get_duration()
        x = highestPowerof2(d)
        text += str(int(base//x))
        if int(text[-1]) < 1:
            temp = 1-int(text[-1])
            text = text[:-1]
            for i in range(int(temp)+1):
                text += "1~ "
            text = text[:-2]
        dots = log(1-d/(2*x), 0.5)-1
        while int(dots) != dots:
            # print(note)
            # print(dots)
            # print(text)
            text += "~ "
            text += str(note.get_pitch(True, flat))
            d -= x
            x = highestPowerof2(d)
            text += str(int(base//x))
            dots = log(1-d/(2*x), 0.5)-1
        # print(7)
        for i in range(int(dots)):
            text += "."
        text += " "
    #print(8)
    text = text.rstrip()
    text += "\n}"
    text = text.replace("#", "is")
    text = text.replace("b", "es")
    text = text.replace("treesle", "treble")
    text = text.replace("eses", "bes")
    return text
            

        
