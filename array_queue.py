class ArrayQueue:

    def __init__(self, capacity):

        if capacity <= 0:

            raise ValueError("Capacity must be greater than zero.")



        self.items = [None] * capacity

        self.front = 0

        self.rear = -1

        self.size = 0

        self.capacity = capacity



    def is_empty(self):

        return self.size == 0



    def is_full(self):

        return self.size == self.capacity



    def enqueue(self, item):

        if self.is_full():

            raise OverflowError("Cannot enqueue: Array queue is full.")



        self.rear = (self.rear + 1) % self.capacity

        self.items[self.rear] = item

        self.size += 1



    def dequeue(self):

        if self.is_empty():

            raise IndexError("Cannot dequeue: Array queue is empty.")



        item = self.items[self.front]

        self.items[self.front] = None

        self.front = (self.front + 1) % self.capacity

        self.size -= 1



        if self.size == 0:

            self.front = 0

            self.rear = -1



        return item



    def peek_front(self):

        if self.is_empty():

            raise IndexError("Cannot peek: Array queue is empty.")



        return self.items[self.front]



    def display(self):

        print("Physical array:", self.items)



        if self.is_empty():

            print("Queue (front to rear): []")

        else:

            values = []

            for i in range(self.size):

                index = (self.front + i) % self.capacity

                values.append(self.items[index])



            print("Queue (front to rear):", values)



        print("Front index:", self.front, "| Rear index:", self.rear)
