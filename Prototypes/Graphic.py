import tkinter as tk



def populate_background(canvas):
    for line in range(40,480,int(480/24)):
        colour_ref = {0:"grey", 20:"grey", 40:"black", 60:"grey"}
        note_ref = {0:"e",20:"d",40:"c",60:"b",80:"a",100:"g",120:"f"}
        octave_ref = {-1:"5",0:"4",1:"3",2:"2"}
        canvas.create_line(0,line,480,line,fill="grey")
        canvas.create_line(line,0,line,480,fill=colour_ref[line%80])
        canvas.create_text(line+10,20,text=str(int(line/20)-1))
        canvas.create_text(20,line+10,text=note_ref[line%140]+octave_ref[(line-60)//140])
        print(line)
#<140=0
#140-280=1
#280-420=2
#420=3
  
#140, 140, 140
def add_note(canvas, start, end, pitch):
    note_ref={"c":0,"d":20,"e":40,"f":60,"g":80,"a":100,"b":120}
    octave_ref={"2":0,"3":140,"4":280,"5":420}
    canvas.create_rectangle(start*20+20, 480-note_ref[pitch[0]]-octave_ref[pitch[1]]\
            , end*20+40, 480-note_ref[pitch[0]]-octave_ref[pitch[1]]-20, fill="grey")



window = tk.Tk()
window.title("Test")
window.geometry("480x480")
window.maxsize(480, 480)
window.minsize(480,480)
canvas = tk.Canvas(window, width=480, height=480)
canvas.pack()
populate_background(canvas)
for note in [[1,1,"e4"],[10,12,"c2"],[4,15,"c5"]]:
    add_note(canvas,*note)
note = "e4"
start = 1
end = 1
while note != "" and start != "" and end != "":
    note = input("Note: ")
    start = int(input("Start: "))
    end = int(input("End: "))
    add_note(canvas,start,end,note)
window.mainloop()
