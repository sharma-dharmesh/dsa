"""Write a program to print binary numbers from 1 to 10 using Queue."""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, data):
        node = Node(data)
        if self.front is None:
            self.front = self.rear = node
            self.length += 1
            return
        
        self.rear.next = node
        self.rear = node
        self.length += 1

    def dequeue(self):
        if self.front is None:
            return 
        self.front = self.front.next
        self.length -= 1
    
    def print_list(self):
        if self.front is None:
            return
        
        itr = self.front
        while itr:
            print(itr.data, end=' ')
            itr = itr.next
        print()
    
    def get_front(self):
        if self.front:
            return self.front.data
        return ''
    
    def get_length(self):
        return self.length


q = Queue()
q.print_list()
n = 10
q.enqueue('1')
for i in range(n):
    front = q.get_front()
    print(front)
    if i < int(n/2):
        q.enqueue(front + '0')
        q.enqueue(front + '1')

    q.dequeue()
    print(f'Length: {q.get_length()}')
