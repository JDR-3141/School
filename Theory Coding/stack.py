class Stack():

    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            raise Exception("Underflow error")
        else:
            value = self.stack.pop()
            return value
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return self.stack == []
    
    def size(self):
        return len(self.stack)
    
class StaticStack(Stack):

    def __init__(self, size):
        super().__init__()
        self.stack = [None] * size
        self.top = 0

    def push(self, data):
        if self.is_full():
            raise Exception("Overflow error")
        else:
            self.stack[self.top] = data
            self.top += 1

    def is_empty(self):
        return self.top == 0
    
    def is_full(self):
        return self.top == len(self.stack)-1
    
    def peek(self):
        return self.stack[self.top]

    
    
