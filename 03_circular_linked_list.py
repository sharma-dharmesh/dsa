class Node:
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data


class CircularLinkedList:
    def __init__(self):
        # self.firstptr = None
        self.lastptr = None
    
    def insert_next(self, data):

        if self.lastptr is None:
            node = Node(data, self.lastptr)
            self.lastptr = node
            self.lastptr.next = node
            return

        node = Node(data, self.lastptr.next)
        self.lastptr.next = node
        self.lastptr = node

    def print_list(self):

        #TODO: Some of the elements are either not inserted or not printed
         
        if self.lastptr is None:
            print("The Circular Linked List is empty!!")
            return
        
        itr = self.lastptr.next
        str = '[ '

        while itr:
            if itr.next == self.lastptr.next:
                itr.next = None
            str += f'{itr.data}, '
            itr = itr.next
        str += ']'
        print(str)


if __name__ == '__main__':
    cll = CircularLinkedList()
    cll.insert_next(2)
    cll.insert_next(33)
    cll.insert_next(444)
    cll.insert_next(5555)
    cll.insert_next(6)


    cll.print_list()

    cll.insert_next(7)
    cll.insert_next(88)

    cll.print_list()