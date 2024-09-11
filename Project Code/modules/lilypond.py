#from classes.Takes import Take

def convert(take):
    text = """
\\version "2.12.3"
{
    \\clef treble
    """
    in_a_bar = take.get_time(0)
    base = take.get_time(1)
    current_time = 1
    current_bar = 1
    for note in take.Notes:
        add = ""
        text += note.get_pitch()
        n  = note.get_duration()
        if n - int(n) == 0.5: # This might need to go somewhere else
            n = int(n*2/3) ##################################
            add = "." #######################################
        while (current_time + n)//in_a_bar > current_bar:
            n1 = in_a_bar - current_time%in_a_bar
            n = n - n1
            if current_time - int(current_time) == 0.5:
                
            text += n1
            text += note.get_pitch()
            

        text += str(int(base/n)) + add
        
