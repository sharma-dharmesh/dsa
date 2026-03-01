class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begenning(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            return
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return 
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        if index < 0:
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_begenning(data)
            return
        
        elif index == self.get_length() - 1:
            self.insert_at_end(data)
            return
        
        count = 0
        itr = self.head

        while itr:
            if count == index-1:
                itr.next = Node(data, itr.next)
            count += 1
            itr = itr.next
            

    def print_list(self):
        if self.head is None:
            print("The linked List is empty")
            return
        
        itr = self.head
        list_str = ''
        while itr:
            list_str += f'{itr.data}-->'
            itr = itr.next
        list_str += 'none'
        print(list_str)


ll = Linkedlist()
ll.insert_at_begenning(2)
ll.insert_at_begenning(3)
ll.insert_at_begenning(54)

ll.insert_at_end(84)
ll.insert_at_end(89)

ll.print_list()
print(f"The length is: {ll.get_length()}")

ll.remove_at(1)
ll.insert_at(4, 9999)
ll.print_list()
print(f"The length is: {ll.get_length()}")