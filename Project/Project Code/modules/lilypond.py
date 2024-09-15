#from classes.Takes import Take
from math import log


def highestPowerof2(n):
 
    p = int(log(n, 2))
    return int(pow(2, p))

def convert(take):
    text = """
\\version "2.12.3"
\\new Voice \\with {
  \\remove Note_heads_engraver
  \\consists Completion_heads_engraver
  \\remove Rest_engraver
  \\consists Completion_rest_engraver
}
{
  \\clef treble                                                                                                                    8                                                                                                                                                                                                                                                               
    """
    in_a_bar = take.get_time(0)
    base = take.get_time(1)
    current_time = 1
    current_bar = 1
    for note in take.Notes:
        text += str(note.get_pitch())
        d = note.get_duration()
        x = highestPowerof2(d)
        text += str(base//x)
        dots = log(1-d/(2*x), 0.5)
        if int(dots) == dots:
          for i in range(int(dots)):
              text += "."


        
