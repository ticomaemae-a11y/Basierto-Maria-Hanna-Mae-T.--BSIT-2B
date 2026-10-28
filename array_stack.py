
class ArrayStack:

    def __init__(self, capacity):

        if capacity <= 0:

            raise ValueError("Capacity must be greater than zero.")



        self.items = [None] * capacity

        self.top = -1

        self.capacity = capacity



    def is_empty(self):

        return self.top == -1



    def is_full(self):

        return self.top == self.capacity - 1



    def push(self, item):

        if self.is_full():

            raise OverflowError("Cannot push: Array stack is full.")



        self.top += 1

        self.items[self.top] = item



    def pop(self):

        if self.is_empty():

            raise IndexError("Cannot pop: Array stack is empty.")



        item = self.items[self.top]

        self.items[self.top] = None

        self.top -= 1

        return item



    def peek(self):

        if self.is_empty():

            raise IndexError("Cannot peek: Array stack is empty.")



        return self.items[self.top]



    def display(self):

        print("Stack (bottom to top):", self.items[:self.top + 1])


next


class Node:

    def __init__(self, data):

        self.data = data

        self.next = None





class LinkedStack:

    def __init__(self):

        self.top = None



    def is_empty(self):

        return self.top is None



    def is_full(self):

        # No fixed capacity; limited only by available memory.

        return False



    def push(self, item):

        new_node = Node(item)

        new_node.next = self.top

        self.top = new_node



    def pop(self):

        if self.is_empty():

            raise IndexError("Cannot pop: Linked stack is empty.")



        item = self.top.data

        self.top = self.top.next

        return item



    def peek(self):

        if self.is_empty():

            raise IndexError("Cannot peek: Linked stack is empty.")



        return self.top.data



    def display(self):

        current = self.top

        print("Stack (top to bottom):", end=" ")



        while current:

            print(current.data, end=" -> ")

            current = current.next



        print("None")

