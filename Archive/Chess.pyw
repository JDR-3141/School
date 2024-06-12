# The class square has an x and y position on the board, and contains
# a state, which is either empty or filled with an object (piece)

from tkinter import *
import os

global choice
choice = False
global move_list
move_list = []
global current
current = "white"
global to_promote

global basedir
basedir = os.path.dirname(__file__)

try:
    from ctypes import windll
    myappid = "NA.Chess.Chess.0"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass
    


def on_click(event):
    global to_promote
    for line in squares:
        for square in line:
            square.unglow()
    clickx = (window.winfo_pointerx()-window.winfo_rootx())//60
    clicky = (window.winfo_pointery()-window.winfo_rooty())//60
    if choice == False:
        filler = check_moves(last_move, clickx, clicky, True)
    elif choice == None:
        do_promote(clickx, clicky, move_list, to_promote)
    else:   
        to_promote = do_move(move_list, choice, clickx, clicky, current, images)

def take_first(item):
    return item[0]

def show_promote(images, current, choice):
    reference = {
        "white":15,
        "black":14}
    xreference = (180,180,180,180,-120,-120,-120,-120)
    global promote_picture
    promote_picture = canvas.create_image(choice.x*60+xreference[choice.x], choice.y*60+30,image = images[reference[current]])
    global move_list
    move_list = []
    for square in range(4):
        move_list.append([choice.x+((xreference[choice.x]//abs(xreference[choice.x]))*(square+1)), choice.y])
    return choice

def do_promote(clickx, clicky, move_listl, to_promote):
    canvas.delete(promote_picture)
    move_listl.sort(key=take_first)
    reference = [[Knight, Bishop, Rook, Queen],[2,4,6,8]]
    if [clickx,clicky] in move_listl:
        squares[to_promote.x][to_promote.y].state.taken()
        
        pieces.append(reference[0][move_listl.index([clickx,clicky])](to_promote.x, to_promote.y, to_promote.colour, reference[1][move_listl.index([clickx,clicky])]))
        squares[to_promote.x][to_promote.y].state = pieces[-1]
    global move_list
    move_list = []

    global choice
    choice = False
    
def check_illegal(last_move, move_list):
        reference = {
            "white":0,
            "black":1}
        to_remove = []
        for move in move_list:
            displaced = squares[move[0]][move[1]].state
            displaced_last_move = last_move
            last_move = [choice,[choice.x,choice.y],[move[0],move[1]]]
            squares[choice.x][choice.y].state = False
            squares[move[0]][move[1]].state = choice
            gone = False
            temp_move_list = []
            for piece in pieces:
                if not gone and [piece.x,piece.y] != [move[0],move[1]]:
                    if piece.colour != choice.colour:
                        temp = piece.check(last_move)
                        for item in temp:
                            temp_move_list.append(item)
            if type(choice) != King:
                if [pieces[reference[choice.colour]].x,pieces[reference[choice.colour]].y] in temp_move_list:
                    to_remove.append(move)
                    gone = True
            elif [move[0],move[1]] in temp_move_list:
                to_remove.append(move)
                gone = True
            squares[choice.x][choice.y].state = choice
            squares[move[0]][move[1]].state = displaced
            last_move = displaced_last_move
        for move in to_remove:
            move_list.remove(move)
        return move_list

def check_checkmate(images, current):
    moves = False
    move_list = []
    for piece in pieces:
        if piece.colour == current:
            move_list = check_moves(last_move, piece.x, piece.y, False)
            if len(move_list) != 0:
                moves = True
                break
    if moves == False:
        end_game(images, current)
    choice = False
    move_list = []

def end_game(images, winner):
    reference = {"white":13,
                 "black":12}
    picture = canvas.create_image(240, 240,image = images[reference[winner]])
    
        
    
def check_moves(last_move, clickx, clicky, visible):
    if squares[clickx][clicky].state != False:
        if squares[clickx][clicky].state.colour == current:
            global move_list
            move_list = squares[clickx][clicky].state.check(last_move)
            global choice
            choice = squares[clickx][clicky].state
            move_list = check_illegal(last_move, move_list)
            if visible:
                for coord in move_list:
                    squares[coord[0]][coord[1]].glow()
            return move_list

def do_move(move_listl, choicel, clickx, clicky, old, images):
    to_promote = False
    if [clickx,clicky] in move_listl:
        if type(choicel) == Pawn and abs(clickx-choicel.x) == 1 and squares[clickx][clicky].state == False:
            squares[clickx][choicel.y].state.taken()
        if squares[clickx][clicky].state != False:
            squares[clickx][clicky].state.taken()
        if type(choicel) == King and choicel.x == 4 and [clickx,clicky] == [2,choicel.y]:
            squares[0][choicel.y].state.move(3,choicel.y)
        if type(choicel) == King and choicel.x == 4 and [clickx,clicky] == [6,choicel.y]:
            squares[7][choicel.y].state.move(5,choicel.y)
        global last_move
        last_move = [choicel,[choicel.x,choicel.y],[clickx,clicky]]
        choicel.move(clickx,clicky)
        if type(choicel) == Pawn or type(choicel) == Rook or type(choicel) == King:
            choicel.moved = True
        swap = {"black":"white",
            "white":"black"}
        global current
        current = swap[old]
        check_checkmate(images, current)
    global move_list
    move_list = []
    global choice
    choice = False
    reference = {"white": 0,
        "black": 7}
    if type(choicel) == Pawn and choicel.y == reference[choicel.colour]:
        to_promote = show_promote(images, current, choicel)
        choice = None
    return to_promote
    
    
    
    

def square_creation():
    global squares
    squares = []
    colours = ["white", "#3BD129"]
    count = 0
    for r in range(8):
        temp = []
        count += 1
        for c in range(8):
            count += 1
            temp.append(Square(r, c, False, colours[count%2]))
        temp.append(Border(r, 8, None, None))
        temp.append(Border(r, 9, None, None))
        squares.append(temp)
    temp = []
    for r in range(2):
        for c in range(10):
            temp.append(Border(r+8, c, None, None))
        squares.append(temp)

def piece_creation():
    global pieces
    pieces = []
    colours = ["white", "black"]
    pawnr = [6,1]
    otherr = [7,0]
    for c in range(2):
        pieces.append(King(4, otherr[c], colours[c], 10))
    for c in range(2):
        for r in range(8):
            pieces.append(Pawn(r, pawnr[c], colours[c], 0))
        pieces.append(Rook(0, otherr[c], colours[c], 6))
        pieces.append(Rook(7, otherr[c], colours[c], 6))
        pieces.append(Knight(1, otherr[c], colours[c], 2))
        pieces.append(Knight(6, otherr[c], colours[c], 2))
        pieces.append(Bishop(2, otherr[c], colours[c], 4))
        pieces.append(Bishop(5, otherr[c], colours[c], 4))
        pieces.append(Queen(3, otherr[c], colours[c], 8))

def new_file():
    clear_window()
    global canvas
    canvas = Canvas(window, width=480, height=480)
    canvas.pack()
    square_creation()
    piece_creation()
    global current
    current = "white"
    global last_move
    last_move = [pieces[0],[0,0],[0,0]]
    global game_name
    game_name = False

def check_name(game_name, squares, images):
    if game_name == False:
        game_name = ask_for_name()
        if os.path.isfile(game_name):
            override(game_name, squares, images)
    save_file(game_name, squares)

def override(game_name, squares, images):
    global var1
    var1 = IntVar()
    picture = canvas.create_image(240, 220,image = images[16])
    okay = Button(window, text = "Replace", command = lambda: var1.set(1))
    okay.place(relx = 0.4, rely = 0.5, anchor = CENTER)
    stop = Button(window, text = "Cancel", command = lambda: cancel(game_name, squares, images, okay, stop, picture))
    stop.place(relx = 0.6, rely = 0.5, anchor = CENTER)
    okay.wait_variable(var1)
    


def cancel(game_namel, squares, images, okay, stop, picture):
    global game_name
    game_name = False
    var1.set(1)
    canvas.delete(picture)
    okay.destroy()
    stop.destroy()
    check_name(game_name, squares, images)
    

def save_file(game_name, squares):
    file = ""
    for line in squares:
        for square in line:
            if square.state == None:
                file += "None"
            elif square.state == False:
                file += "False"
            else:
                file += repr(square.state)
            file += ","
        file = file.rstrip(file[-1])
        file += "\n"
    for part in range(1,3):
        for item in last_move[part]:
            file += str(item)
            file += ","
    file = file.rstrip(file[-1])
    file += "\n"
    file += current
    f = open(os.path.join(basedir, "game_files", game_name), mode = "w")
    f.write(file)
    f.close

def ask_for_name():
    global var
    var = IntVar()
    background = canvas.create_rectangle(240-100, 240-50, 240+100, 240+50, fill="#0080FF")
    entry = Entry(window)
    entry.place(relx = .45, rely = .5, anchor = CENTER)
    button = Button(window, text = "Save", command = lambda: get_data(entry))
    button.place(relx = .65, rely = .5, anchor = CENTER)
    button.wait_variable(var)
    canvas.delete(background)
    button.destroy()
    entry.destroy()
    return game_name

def get_data(entry):
    global game_name
    game_name = entry.get()
    game_name += ".txt"
    var.set(1)

def clear_window():
    for widgets in window.winfo_children():
        if type(widgets) != Menu:
            widgets.destroy()

def choose_file():
    result = []
    for files in os.walk(os.getcwd()):
        for sublist in files:
            for file in sublist:
                if ".txt" in file:
                    result.append(file)
    for file in range(len(result)):
        result[file] = result[file].replace(".txt","")

    file_window = Tk()
    file_window.title("Choose file to open")
    yscrollbar = Scrollbar(file_window)
    yscrollbar.pack(side = RIGHT, fill = Y)
    
    files = Listbox(file_window, selectmode = "single",yscrollcommand = yscrollbar.set)
    files.pack(padx = 10, pady = 10, expand = YES, fill = "both")
    for item in range(len(result)):
        files.insert(END, result[item])
    yscrollbar.config(command = files.yview)
    button = Button(file_window, text = "Open", command = lambda: open_file(files, file_window))
    button.pack(fill = "x", side = "bottom")
    
    
def open_file(files, file_window):
    global query
    query = str(files.get(files.curselection()) + ".txt")
    file_window.destroy()
    global game_name
    game_name = query
    f = open(os.path.join(basedir, "game_files", query))
    file = f.readlines()
    f.close()
    for line in range(len(file)):
        file[line] = file[line].strip()
    for i in range(10):
        file[i] = file[i].split(",")
    square_contents = file[:10]
    for line in range(len(square_contents)):
        for square in range(len(square_contents[line])):
            square_contents[line][square] = square_contents[line][square].split(".")
    clear_window()
    global canvas
    canvas = Canvas(window, width=480, height=480)
    canvas.pack()
    square_creation()
    reference = {"Pawn":[Pawn, 0],
                 "Knight":[Knight, 2],
                 "Bishop":[Bishop, 4],
                 "Rook":[Rook, 6],
                 "Queen":[Queen, 8],
                 "King":[King, 10]}
    for r in range(10):
        for c in range(10):
            if "None" != square_contents[r][c][0] != "False":
                squares[r][c].state = reference[square_contents[r][c][0]][0](r, c, square_contents[r][c][1], reference[square_contents[r][c][0]][1])
                squares[r][c].state.moved = eval(square_contents[r][c][2])
                if len(pieces) != 0:
                    if type(squares[r][c].state) != King:
                        pieces.append(squares[r][c].state)
                    elif type(pieces[0]) == King:
                        if pieces[0].colour == "white":
                            pieces.insert(1, squares[r][c].state)
                        else:
                            pieces.insert(0, squares[r][c].state)
                    else:
                        pieces.insert(0, squares[r][c].state)
                else:
                    pieces.append(squares[r][c].state)
    insert_last_move = file[10]
    insert_last_move = insert_last_move.split(",")
    moves = False
    for item in insert_last_move:
        if insert_last_move != 0:
            moves = True
    global last_move
    if not moves:
        last_move = [pieces[0],[0,0],[0,0]]
    else:
        last_move = [squares[int(insert_last_move[2])][int(insert_last_move[2])].state\
                     ,[int(insert_last_move[0]),int(insert_last_move[1])]\
                     ,[int(insert_last_move[2]),int(insert_last_move[3])]]
    global current
    current = file[11]
                        
    
    

def main():
    global window
    window = Tk()
    window.title("Chess")
    window.geometry("480x480")
    window.maxsize(480, 480)
    window.minsize(480,480)
    window.iconbitmap(os.path.join(basedir, "icons", "Icon.ico")) 
    global canvas
    canvas = Canvas(window, width=480, height=480)
    window.bind("<Button-1>", on_click)
    canvas.pack()
    global images
    images = []
    imagep = ["p","n","b","r","q","k"]
    imagec = ["l","d"]
    for piece in imagep:
        for colour in imagec:
            images.append(PhotoImage(file=os.path.join(basedir, "icons", "Chess_"+piece+colour+"t60.png")))
    images.append(PhotoImage(file=os.path.join(basedir, "icons", "white_wins.png")))
    images.append(PhotoImage(file=os.path.join(basedir, "icons", "black_wins.png")))
    images.append(PhotoImage(file=os.path.join(basedir, "icons", "white_promote.png")))
    images.append(PhotoImage(file=os.path.join(basedir, "icons", "black_promote.png")))
    images.append(PhotoImage(file=os.path.join(basedir, "icons", "file_exists.png")))
    square_creation()
    piece_creation()
    global last_move
    last_move = [pieces[0],[0,0],[0,0]]
    global game_name
    game_name = False
    menu = Menu(window)
    item = Menu(menu)
    item.add_command(label="New", command = new_file)
    item.add_command(label="Save", command = lambda: check_name(game_name, squares, images))
    item.add_command(label="Open", command = choose_file)
    menu.add_cascade(label="File", menu = item)
    window.config(menu=menu)
    window.mainloop()

class Square:
    
    def __init__(self, x, y, state, colour):
        self.x = x
        self.y = y
        self.state = state
        self.colour = colour
        self.image = canvas.create_rectangle(60*self.x, 60*self.y, 60*self.x+60, 60*self.y+60, fill=self.colour)

    def glow(self):
        reference = {
            "white":"red1",
            "#3BD129":"red3"}
        canvas.itemconfig(self.image, fill = reference[self.colour])

    def unglow(self):
        canvas.itemconfig(self.image, fill = self.colour)

    def __str__(self):
        string = "Coords: " + str(self.x) + "," + str(self.y) +\
                 " occupied by: " + str(self.state) + " with colour: " + self.colour
        return string

class Border(Square):

    def __init__(self, x, y, state, colour):
        Square.__init__(self, x, y, state, colour)
    

class Piece:

    def __init__(self, x, y, colour, piece_type):
        self.y = y
        self.x = x
        self.colour = colour
        self.present = True
        self.moved = None
        self.piece_type = piece_type
        if colour == "white":
            self.image =images[self.piece_type]
        else:
            self.image =images[self.piece_type+1]
        self.picture = canvas.create_image(60*self.x+30, 60*self.y+30,image = self.image)
        self.points = 0
        squares[self.x][self.y].state = self

    def move(self, x, y):
        squares[self.x][self.y].state = False
        tempx = self.x
        tempy = self.y
        self.x = x
        self.y = y
        squares[x][y].state = self
        canvas.move(self.picture, (self.x*60+30)-(tempx*60+30), (self.y*60+30)-(tempy*60+30))

    def taken(self):
        canvas.delete(self.picture)
        squares[self.x][self.y].state = False
        pieces.remove(self)

    def add_coords(self, position, move):
        new = [position[0]+move[0], position[1]+move[1]]
        return new

    def check(self, last_move):
        move_list = []
        for move in self.moves:
            x = self.add_coords([self.x,self.y],move)[0]
            y = self.add_coords([self.x,self.y],move)[1]
            while squares[x][y].state != None:
                if squares[x][y].state == False:
                    move_list.append([x,y])
                elif squares[x][y].state.colour != self.colour:
                    move_list.append([x,y])
                    break
                else:
                    break
                x = self.add_coords([x,y],move)[0]
                y = self.add_coords([x,y],move)[1]
        return(move_list)
        
    def __repr__(self):
        string = self.__class__.__name__ + "." + self.colour  + "." + str(self.moved)
        return string

class Pawn(Piece):

    def __init__(self, x, y, colour, piece_type):
        Piece.__init__(self, x, y, colour, piece_type)
        self.moved = False
        self.points = 1

    def check(self, last_move):
        
        move_list = []
        reference = {
            "white":[-1,3],
            "black":[1,4]}
        if squares[self.x][self.y+reference[self.colour][0]].state == False:
            move_list.append([self.x,self.y+reference[self.colour][0]])
            if not self.moved:
                if squares[self.x][self.y+2*reference[self.colour][0]].state == False:
                    move_list.append([self.x,self.y+2*reference[self.colour][0]])
        for direction in [-1,1]:
            if None != squares[self.x+direction][self.y+reference[self.colour][0]].state != False:
                if squares[self.x+direction][self.y+reference[self.colour][0]].state.colour != self.colour:
                    move_list.append([self.x+direction,self.y+reference[self.colour][0]])
        if type(last_move[0]) == Pawn:
            if abs(last_move[2][0] - self.x) == 1:
                if abs(last_move[1][1]-last_move[2][1]) == 2:
                    if self.y == reference[self.colour][1]:
                        move_list.append([last_move[2][0],self.y+reference[self.colour][0]])
        return move_list

class Knight(Piece):

    def __init__(self, x, y, colour, piece_type):
        Piece.__init__(self, x, y, colour, piece_type)
        self.moves = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
        self.points = 3
    
    def check(self, last_move):
        move_list = []
        for move in self.moves:
            x = self.add_coords([self.x,self.y],move)[0]
            y = self.add_coords([self.x,self.y],move)[1]
            if None != squares[x][y].state:
                if squares[x][y].state == False:
                    move_list.append([x,y])
                elif squares[x][y].state.colour != self.colour:
                    move_list.append([x,y])
        return(move_list)


class Bishop(Piece):

    def __init__(self, x, y, colour, piece_type):
        Piece.__init__(self, x, y, colour, piece_type)
        self.moves = [[1,1],[1,-1],[-1,1],[-1,-1]]
        self.points = 3

    


class Rook(Piece):

    def __init__(self, x, y, colour, piece_type):
        Piece.__init__(self, x, y, colour, piece_type)
        self.moves = [[0,1],[0,-1],[1,0],[-1,0]]
        self.moved = False
        self.points = 5


class Queen(Piece):

    def __init__(self, x, y, colour, piece_type):
        Piece.__init__(self, x, y, colour, piece_type)
        self.moves = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        self.points = 9


class King(Piece):

    def __init__(self, x, y, colour, piece_type):
        Piece.__init__(self, x, y, colour, piece_type)
        self.moves = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        self.moved

    def check(self, last_move):
        move_list = []
        for move in self.moves:
            x = self.add_coords([self.x,self.y],move)[0]
            y = self.add_coords([self.x,self.y],move)[1]
            if None != squares[x][y].state:
                if squares[x][y].state == False:
                    move_list.append([x,y])
                elif squares[x][y].state.colour != self.colour:
                    move_list.append([x,y])
        if not self.moved:
            if squares[0][self.y].state != False:
                if not squares[0][self.y].state.moved:
                    if not squares[1][self.y].state and not squares[2][self.y].state and not squares[3][self.y].state:
                        move_list.append([2,self.y])
            if squares[7][self.y].state != False:
                if not squares[7][self.y].state.moved:
                    if not squares[5][self.y].state and not squares[6][self.y].state:
                        move_list.append([6,self.y])
        return(move_list)




if __name__ == "__main__":
    main()

