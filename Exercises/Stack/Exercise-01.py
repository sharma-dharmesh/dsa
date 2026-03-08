"""
Write a function in python that can reverse a string using stack data structure.
reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
"""

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


def reverse_sting(sentence):
    s = Stack()
    reverse_sentence = ''
    for character in sentence:
        s.push(character)
    
    # while s.getSize() != 0:
    # Or
    for i in range(s.getSize()):
        reverse_sentence += s.pop()
    
    return reverse_sentence


print(reverse_sting('We will conquere COVID-19'))
