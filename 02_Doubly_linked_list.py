class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            self.tail = node

        else:
            node = Node(data, self.head)
            self.head.prev = node
            self.head = node
        self.length += 1

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            self.tail =  node

        elif self.tail == self.head:
            node = Node(data, None, self.head)
            self.tail = node

        else:
            node = Node(data,None, self.tail)
            self.tail.next = node
            self.tail = node

        self.length += 1

    def get_length(self):
       return self.length
    
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            print("Invallid Index")
        
        else:
            itr = self.head
            count = 0
            while itr:
                if count == index -1:
                    node = Node(data, itr.next, itr)
                    itr.next.prev = node
                    itr.next = node

            # (OR)

                """
                if count == index:
                    node = Node(data, itr, itr.prev)
                    itr.prev.next = node
                    itr.prev = node
                """

                itr = itr.next
                count += 1

    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            print("Invalid Index")
        
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
        
        else:
            count = 0
            itr = self.head
            while itr:

                if count == index:
                    itr.prev.next = itr.next
                    if itr.next:
                        itr.next.prev = itr.prev

                count += 1
                itr = itr.next
            self.length -= 1

    def remove_by_value(self, data):
        itr = self.head
        while itr:
            if itr.data == data:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                elif itr.next is None:
                    self.tail = itr.prev
                return           
            itr = itr.next
        self.length -= 1

    def insert_list(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    
    def print_forward (self):
        if self.head is None:
            print("The doubly Linked list is empty")
            
        else:
            itr = self.head
            print("none", end='<-->')
            while itr:
                print(itr.data, end='<-->')
                itr = itr.next
            print('none')

    def print_backward (self):
        if self.head is None:
            print("The doubly linked list is empty")

        else:
            itr = self.tail
            print('none', end='<-->')
            while itr:
                print(itr.data, end='<-->')
                itr = itr.prev
            print('none')
    
dll = DoublyLinkedList()
dll.insert_at_beginning(2)
dll.insert_at_beginning(1)
dll.insert_at_beginning(3)

dll.insert_at_end(33)
dll.insert_at_end(44)

dll.insert_at(2, "Two")
dll.insert_at(5, "five")

dll.print_forward()
print(f'Length : {dll.get_length()}')
dll.print_backward()
print(f'Length : {dll.get_length()}')

dll.remove_at(2)

dll.insert_list(["Apple", 'Mango', 'Orange'])
dll.print_forward()
dll.print_backward()

dll.remove_by_value('Orange')
dll.print_forward()
dll.print_backward()