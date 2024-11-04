import tkinter as tk



def populate_background(canvas, width, height):
    colour_ref = {0:"grey", 20:"grey", 40:"black", 60:"grey"}
    for line in range(40,width,20):
        #int(width/24)):
        
        
        canvas.create_line(line,0,line,height,fill=colour_ref[line%80])
        num = int(line/20)+2
        canvas.create_text(line+10,20,text=str(num//4)+"."+str(num%4))
        print(line)

    note_ref = {0:"c",20:"b",40:"a#",60:"a",80:"g#",100:"g",120:"f#",140:"f",160:"e",180:"d#",200:"d",220:"c#"}
    octave_ref = {-1:"8",0:"7",1:"6",2:"5", 3:"4",4:"3",5:"2",6:"1",7:"0"}
    for line in range(40, 40+12*8*20+20, 20):
        canvas.create_line(0,line,width,line,fill="grey")
        print(line)
        canvas.create_text(20,line+10,text=note_ref[(line-40)%240]+octave_ref[(line-60)//240])

#<140=0
#140-280=1
#280-420=2

#420=3
  
#140, 140, 140
def add_note(canvas, start, end, pitch):
    note_ref = {'c': 0, 'b': 20, 'a#': 40, 'a': 60, 'g#': 80, 'g': 100, 'f#': 120, 'f': 140, 'e': 160, 'd#': 180, 'd': 200, 'c#': 220}
    octave_ref = {'8': -1, '7': 0, '6': 1, '5': 2, '4': 3, '3': 4, '2': 5, '1': 6, '0': 7}
    canvas.create_rectangle(start*20+20, 40+note_ref[pitch[:-1]]+240*octave_ref[pitch[-1]]\
            , end*20+40, 40+note_ref[pitch[:-1]]+240*octave_ref[pitch[-1]]+20, fill="grey")


time_sig = input("Time Sig: ") ###################### Time sig still isn't implemented, but last end is good. Add note is getting the wrong coordinates though so use the notepad again
last_end = int(input("Last End: "))
window = tk.Tk()
window.title("Test")
width = last_end*20+40
height = 80+12*8*20
window.geometry(str(width)+"x"+str(height))
window.maxsize(width, height)
window.minsize(width,height)
canvas = tk.Canvas(window, width=width, height=height)
canvas.pack()
populate_background(canvas, width, height)
for note in [[1,1,"e4"],[10,12,"c2"],[4,15,"c5"]]:
    add_note(canvas,*note, height)
note = "e4"
start = 1
end = 1
while note != "" and start != "" and end != "":
    note = input("Note: ")
    start = int(input("Start: "))
    end = int(input("End: "))
    add_note(canvas,start,end,note)
window.mainloop()
