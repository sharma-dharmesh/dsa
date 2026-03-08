'''
Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]".
'''

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
                print(f'{itr.data}', end=', ')
                itr = itr.prev
            print()

def is_match(ch1, ch2):
    match_dict = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }
    return match_dict[ch1] == ch2

def is_balanced(expression):
    s = Stack()
    left_brackets = ['(', '{', '[']
    right_brackets = [')', '}', ']']
    for character in expression:
        if character in left_brackets:
            s.push(character)

        if character in right_brackets:
            if s.getSize() == 0:
                return False
            
            if not is_match(character, s.pop()):
                return False
        
    return s.getSize() == 0
    

print(is_balanced('{a+b} (a-b)'))
print(is_balanced('{(a+b)*(a-b)}'))
print(is_balanced('}}{{'))
print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("((a+b))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))