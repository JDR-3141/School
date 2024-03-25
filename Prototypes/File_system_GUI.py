import tkinter as tk

projects = [["Test1", "Test2"],[["Take1","Take2","Take3"],["Take1"]]]

def choose(choices):
    for widget in window.winfo_children():
        if type(widget) != tk.Menu:
            widget.destroy()
    result = [i+1 for i in range(len(choices))]
    yscrollbar = tk.Scrollbar(window)
    yscrollbar.pack(side = tk.RIGHT, fill = tk.Y)
    files = tk.Listbox(window, selectmode = "single",yscrollcommand = yscrollbar.set)
    files.pack(padx = 10, pady = 10, expand = tk.YES, fill = "both")
    for item in range(len(result)):
        files.insert(tk.END, choices[item])
    yscrollbar.config(command = files.yview)
    button = tk.Button(window, text = "Open", command = lambda:choose(projects[1][files.curselection()[0]]))
    button.pack(fill = "x", side = "bottom")

window = tk.Tk()
window.title("Test")
window.geometry("480x480")
window.maxsize(480, 480)
window.minsize(480,480)

choose(projects[0])
window.mainloop()



