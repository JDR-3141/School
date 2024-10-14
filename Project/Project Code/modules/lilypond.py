# import sys
# from os import getcwd
# sys.path.append(getcwd()+"\\Project\\Project Code")



from classes.Notes import Note
from math import log


def highestPowerof2(n):
    ans = 1024
    while ans > n:
        ans /= 2
    return ans

    # p = int(log(n, 2))
    # return int(pow(2, p))

def convert(take):
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
    text += " \\time " + take.get_time() + "\n  \\key " + take.get_key() + "\n  "
    in_a_bar = take.get_time(0)
    base = take.get_time(1)
    current_time = 1
    current_bar = 1
    for note in Note.notes:
        text += str(note.get_pitch(True))
        d = note.get_duration()
        x = highestPowerof2(d)
        text += str(int(base//x))
        dots = log(1-d/(2*x), 0.5)-1
        while int(dots) != dots:
            text += "~ "
            text += str(note.get_pitch(True))
            d -= x
            x = highestPowerof2(d)
            text += str(int(base//x))
            dots = log(1-d/(2*x), 0.5)-1
        for i in range(int(dots)):
            text += "."
        text += " "
    text = text.rstrip()
    text += "\n}"
    return text
            

        
