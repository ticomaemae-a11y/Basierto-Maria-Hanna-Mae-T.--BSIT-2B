class Node:

    def __init__(self, data):

        self.data = data

        self.next = None



class LinkedQueue:

    def __init__(self):

        self.head = None

        self.tail = None



    def is_empty(self):

        return self.head is None



    def is_full(self):

        # No fixed capacity; limited only by available memory.

        return False



    def enqueue(self, item):

        new_node = Node(item)



        if self.is_empty():

            self.head = new_node

            self.tail = new_node

        else:

            self.tail.next = new_node

            self.tail = new_node



    def dequeue(self):

        if self.is_empty():

            raise IndexError("Cannot dequeue: Linked queue is empty.")



        item = self.head.data

        self.head = self.head.next



        if self.head is None:

            self.tail = None



        return item



    def peek_front(self):

        if self.is_empty():

            raise IndexError("Cannot peek: Linked queue is empty.")



        return self.head.data



    def display(self):

        current = self.head

        print("Queue (front to rear):", end=" ")



        while current:

            print(current.data, end=" -> ")

            current = current.next



        print("None")

