class Node:
    def __init__(self, data=None, prev=None):
        self.data = data
        self.prev = prev

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        if self.top is None:
            node = Node(data)
            self.top = node
            self.size += 1
            
        else:
            node = Node(data, self.top)
            self.top = node
            self.size += 1
    
    def pop(self):
        if self.top is None:
            return 'Empty stack'
        
        temp = self.top
        self.top = self.top.prev
        self.size -= 1
        return temp.data
        

    def peek(self):
        if self.top is None:
            return 'Empty Stack'
        
        return self.top.data
    
    def getSize(self):
        return self.size

    def printStack(self):
        if self.top is None:
            print("Stack is empty")

        else:
            itr = self.top
            while itr:
                print(f'{itr.data}', end='-->')
                itr = itr.prev
            print()


s = Stack()
s.push(5)
s.push(4)
s.push(5)
s.pop()
s.push(3)
s.push(2)
s.push(1)
s.peek()
print(f'Size: {s.getSize()}')
s.printStack()
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
s.printStack()
print(f'size: {s.getSize()}')
