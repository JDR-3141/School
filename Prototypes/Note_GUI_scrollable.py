import tkinter as tk

def on_content_click(event):
    # Calculate the coordinates taking into account the scroll position
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    print(f"Clicked at: ({x}, {y})")

root = tk.Tk()
root.title("Scrollable Canvas with Sidebar")

# Configure the grid layout
root.grid_columnconfigure(0, weight=3)  # Make the scrollable section larger
root.grid_columnconfigure(1, weight=1)  # Sidebar for label-entry pairs

# Create a frame for the scrollable canvas
scrollable_frame = tk.Frame(root)
scrollable_frame.grid(row=0, column=0, sticky="nsew")

# Create a canvas widget
canvas = tk.Canvas(scrollable_frame, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create vertical and horizontal scrollbars linked to the canvas
v_scrollbar = tk.Scrollbar(scrollable_frame, orient=tk.VERTICAL, command=canvas.yview)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

h_scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
h_scrollbar.grid(row=1, column=0, sticky="ew")

# Configure the canvas to work with the scrollbars
canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)


# Ensure the content frame is large enough and update the scroll region
def configure_scroll_region(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", configure_scroll_region)

# Bind the click event to the content_frame
canvas.bind("<Button-1>", on_content_click)

# Create a sidebar for label-entry pairs
sidebar_frame = tk.Frame(root, padx=10, pady=10)
sidebar_frame.grid(row=0, column=1, sticky="nsew")

# Add label-entry pairs to the sidebar
for i in range(3):
    tk.Label(sidebar_frame, text=f"Label {i+1}").grid(row=i, column=0, sticky="e", pady=5)
    tk.Entry(sidebar_frame).grid(row=i, column=1, pady=5)

for line in range(40,480,int(480/24)):
    colour_ref = {0:"grey", 20:"grey", 40:"black", 60:"grey"}
    note_ref = {0:"e",20:"d",40:"c",60:"b",80:"a",100:"g",120:"f"}
    octave_ref = {-1:"5",0:"4",1:"3",2:"2"}
    canvas.create_line(0,line,480,line,fill="grey")
    canvas.create_line(line,0,line,480,fill=colour_ref[line%80])
    canvas.create_text(line+10,20,text=str(int(line/20)-1))
    canvas.create_text(20,line+10,text=note_ref[line%140]+octave_ref[(line-60)//140])

root.mainloop()