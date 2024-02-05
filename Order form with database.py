##########################################################################################################

# Imports

from tkinter import *

##########################################################################################################

#############################################################################################################

# Globals

#############################################################################################################

##########################################################################################################

# Classes

class Item():

    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        print(self.item_name)

    def __str__(self):
        return self.item_name

    def get_item_name(self):
        return self.item_name
   
    def set_item_name(self, new):
        self.item_name = new

    def get_quantity(self):
        return self.quantity
   
    def set_quantity(self, new):
        self.quantity = new

    def get_price(self):
        return self.price
   
    def set_price(self, new):
        self.price = new



class Order():
    unique_order_num = 1

    orders = []
   
    def __init__(self):
        self.order_num = Order.unique_order_num
        self.order_details = []
        self.order_name = ""
        Order.unique_order_num += 1
        Order.orders.append(self)

    def get_order_name(self):
        return self.order_name
   
    def set_order_name(self, new):
        self.order_name = new

    def get_order_num(self):
        return self.order_num
   
    def set_order_num(self, new):
        self.order_num = new

    def get_order_details(self):
        return self.order_details
   
    def set_order_details(self, new):
        self.order_details = new
   
    def add_item(self, item_name, quantity, price):
        """Add each item to the objects list of items for each order"""
        self.order_details.append(Item(item_name, quantity, price))

#############################################################################################################

#############################################################################################################

# Main Code

def new_order(label):
    Order()
    label.place_forget()
    order_name()
   

def add_item_to_order(e1, e2, e3, text):
    current_order = Order.orders[-1]
    current_order.add_item(e1.get(), e2.get(), e3.get())
    text_add(e1.get(), text)
    for entry in [e1, e2, e3]:
        clear_text(entry)

def name_order(e1, text):
    Order.orders[-1].set_order_name(e1.get())
    text_add(e1.get()+":", text)
    for widget in window.winfo_children():
        if type(widget) != Menu:
            widget.destroy()
    enter_text(text)
   
def finish_order():
    for widget in window.winfo_children():
        if type(widget) != Menu:
            widget.destroy()

def view_order():
    choose(Order.orders)

#############################################################################################################


#############################################################################################################

# Tkinter stuff

# the main Tkinter window
global window
window = Tk()
 
# setting the title  
window.title('Order form')
 
# dimensions of the main window
window.geometry("500x500")
 
menu = Menu(window)
item = Menu(menu)
item.add_command(label="New Order", command=lambda: new_order(label))
item.add_command(label="View Orders", command=lambda: view_order())
menu.add_cascade(label="Options", menu = item)
window.config(menu=menu)

label = Label(window, text="Welcome to the ordering system")
label.place(relx=0.5, rely=0.5, anchor=CENTER)

def order_name(): # Work this out next
    frame = Frame(window)
    frame.place(relx=0.5, rely=0, anchor=N)
    l1 = Label(frame,
            text="Order name")
    l1.grid(row=0)

    e1 = Entry(frame)


    e1.grid(row=0, column=1)


    text = StringVar()
    order_label = Label(frame, textvariable=text)
    order_label.grid(row=5)

    save_button = Button(frame,
            text='Add',
            command=lambda: name_order(e1, text))
    save_button.grid(row=3) 
    save_button.grid_columnconfigure(0, weight=1)    

def enter_text(text):
    frame = Frame(window)
    frame.place(relx=0.5, rely=0, anchor=N)
    l1 = Label(frame,
            text="Item name")
    l1.grid(row=0)
    l2 = Label(frame,
            text="Quantity")
    l2.grid(row=1)
    l3 = Label(frame,
            text="Price")
    l3.grid(row=2)

    e1 = Entry(frame)
    e2 = Entry(frame)
    e3 = Entry(frame)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)

    order_label = Label(frame, textvariable=text)
    order_label.grid(row=5)

    save_button = Button(frame,
            text='Add',
            command=lambda: add_item_to_order(e1, e2, e3, text))
    save_button.grid(row=3)
    save_button.grid_columnconfigure(0, weight=1)

    finish_button = Button(frame,
            text='Finish',
            command=finish_order)
    finish_button.grid(row=3,column=1)
    finish_button.grid_columnconfigure(0, weight=1)

def clear_text(entry):
    entry.delete(0, END)

def text_add(entry, text):
    current_text = text.get()
    current_text += "\n" + entry
    text.set(current_text)

def choose(choices):
    for widget in window.winfo_children():
        if type(widget) != Menu:
            widget.destroy()
    result = [i+1 for i in range(len(choices))]
    yscrollbar = Scrollbar(window)
    yscrollbar.pack(side = RIGHT, fill = Y)
    files = Listbox(window, selectmode = "single",yscrollcommand = yscrollbar.set)
    files.pack(padx = 10, pady = 10, expand = YES, fill = "both")
    for item in range(len(result)):
        files.insert(END, choices[item].get_order_name())
    yscrollbar.config(command = files.yview)
    button = Button(window, text = "Open", command = lambda:display_order(files.curselection()[0]))
    button.pack(fill = "x", side = "bottom")
   
def display_order(order):
    for widget in window.winfo_children():
        if type(widget) != Menu:
            widget.destroy()
    text = Order.orders[order].get_order_name() + ":"
    for item in Order.orders[order].get_order_details():
        text += "\n" + item.get_item_name() + " x " + str(item.get_quantity()) + " (£" + str(item.get_price()) + " each)"# add 
    label = Label(window, text=text, justify="left")
    label.place(relx=0.5, rely=0.5, anchor=CENTER)

# run the gui
window.mainloop()

#######################################################################################################