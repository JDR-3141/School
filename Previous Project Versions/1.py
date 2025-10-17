#from classes.Takes import Take
take = [["C4", 2], ["D4", 2], ["E4", 2], ["D4", 2], ["C4", 8]]
def convert(take):
    text = """
\\version "2.12.3"
{
    \\clef treble
    """
    in_a_bar = 4
    base = 4
    current_time = 1
    current_bar = 1
    for note in take:
        add = ""
        text += note[0]
        n  = note[1]
        if (current_time + n)//in_a_bar > current_bar:
            n2 = (current_time + n)%in_a_bar
            n1 = n - n2
            text += n1
            text += note.get_pitch()
            text += n2
        else:
            if n - int(n) == 0.5: # This might need to go somewhere else
                n = int(n*2/3) ##################################
                add = "." #######################################
            text += str(int(base/n)) + add
        return text
print(convert(take))
        