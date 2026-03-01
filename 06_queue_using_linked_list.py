class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.front is None:
            node = Node(data)
            self.front = node
            self.rear = node
            return
        
        node = Node(data)
        self.rear.next = node
        self.rear = node
    
    def dequeue(self):
        if self.front is None:
            return print("Queue is Empty")
        
        self.front = self.front.next

    def peek(self):
        if self.front is None:
            return "Queue is Empty"
        
        return self.front.data
    
    def isEmpty(self):
        if self.front is None:
            return True
        return False
    
    def Size(self):
        if self.front is None:
            return print("Queue is Empty")
        
        itr = self.front
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def printQueue(self):
        if self.front is None:
            return print("Queue is empty!")
        itr = self.front
        print("none", end='-->')
        while itr:
            print(itr.data, end="-->")
            itr = itr.next
        print("none")
        
        

Q = queue()
Q.dequeue()
print(Q.isEmpty())
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)

print(Q.peek())
Q.dequeue()
print(Q.peek())
print(Q.Size())
Q.printQueue()