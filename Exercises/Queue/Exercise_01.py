'''
Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']
This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders.
'''
from threading import Thread
from time import sleep

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        node = Node(data)

        if self.front is None:
            self.front = self.rear = node
            return
        
        self.rear.next = node
        self.rear = node
    
    def dequeue(self):
        if self.front is None:
            return
        
        temp = self.front
        self.front = self.front.next
        return temp.data

    def print_queue(self):
        if self.front is None:
            return
        
        itr = self.front
        print('none', end='-->')
        while itr:
            print(itr.data, end = '-->')
            itr = itr.next
        print('none')

    def is_empty(self):
        if self.front is None:
            return True
        return False


order_queue = Queue()

def place_orders(orders):
    print("Placing order...")
    for order in orders:
        order_queue.enqueue(order)
        print(f'Order of {order} is placed')
        sleep(0.5)

def serve_orders():
    sleep(1)
    print("Serving Orders...")
    while not order_queue.is_empty():
        print(f'Served {order_queue.dequeue()}')
        sleep(2)

orders = ['pizza','samosa','pasta','biryani','burger']

th1 = Thread(target = place_orders, args=(orders,))
th2 = Thread(target = serve_orders, args=())
th1.start()
th2.start()
th1.join()
th2.join()

order_queue.print_queue()