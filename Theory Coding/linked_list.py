class Node():

    def __init__(self, data=None):
        self.data = data
        self.pointer = None

    def get_data(self):
        return self.data
    
    def get_pointer(self):
        return self.pointer
    
    def set_data(self, data):
        self.data = data

    def set_pointer(self, pointer):
        self.pointer = pointer



class Linked_list():

    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head
    
    def set_head(self, head):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        current_node = self.get_head()
        if current_node == None:
            self.set_head(new_node)
        elif current_node.get_data() > new_node.get_data():
            new_node.set_pointer(current_node)
            self.set_head(new_node)
        else:
            previous_node = current_node
            while current_node != None and current_node.get_data() < new_node.get_data():
                previous_node = current_node
                current_node = current_node.get_pointer()
            new_node.set_pointer(current_node)
            previous_node.set_pointer(new_node)

    def pop(self, data):
        current_node = self.get_head()
        if current_node.get_data() == data:
            self.set_head(current_node.get_pointer())
        else:
            previous_node = current_node
            current_node = current_node.get_pointer()
            while current_node.get_data() != data and current_node != None:
                current_node = current_node.get_pointer()
            if current_node.get_data() == data:
                previous_node.set_pointer(current_node.get_pointer())
            
    def __repr__(self):
        current_node = self.get_head()
        string = ""
        while current_node != None:
            string += str(current_node.get_data()) + " -> "
            current_node = current_node.get_pointer()
        string = string.rstrip(" -> ")
        return string

test = Linked_list()
test.insert("Stan")
test.insert("Kyle")
test.insert("John")
test.insert("Carter")
test.insert("Eleanor")
test.pop("Eleanor")
test.pop("Stan")
test.pop("Carter")
#print(test)

user_in = "1"
while user_in != "":
    print("Current linked list:")
    print(test)
    print("""
Options:
    Add a node: 1
    Delete a node: 2
Click Enter to exit
Choice: """, end="")
    user_in = input()
    if user_in == "1":
        print("Enter a name: ", end= "")
        name = input()
        test.insert(name)
    elif user_in == "2":
        print("Enter a name: ", end= "")
        name = input()
        test.pop(name)