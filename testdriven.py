from array_stack import ArrayStack

from linked_stack import LinkedStack

from array_queue import ArrayQueue

from linked_queue import LinkedQueue



def test_array_stack():

    print("\n--- TEST ARRAY STACK ---")



    stack = ArrayStack(2)



    stack.push("A")

    stack.push("B")

    print("After push:", stack.peek())



    print("Pop:", stack.pop())

    print("Pop:", stack.pop())

    print("Is empty:", stack.is_empty())



    try:

        stack.pop()

    except (IndexError, OverflowError) as error:

        print("Underflow test passed:", error)



    stack.push("A")

    stack.push("B")



    try:

        stack.push("C")

    except (IndexError, OverflowError) as error:

        print("Overflow test passed:", error)





def test_linked_stack():

    print("\n--- TEST LINKED STACK ---")



    stack = LinkedStack()



    stack.push("A")

    stack.push("B")



    print("Peek:", stack.peek())

    print("Pop:", stack.pop())

    print("Pop:", stack.pop())

    print("Is empty:", stack.is_empty())



    try:

        stack.pop()

    except (IndexError, OverflowError) as error:

        print("Underflow test passed:", error)





def test_array_queue():

    print("\n--- TEST CIRCULAR ARRAY QUEUE ---")



    queue = ArrayQueue(3)



    queue.enqueue("A")

    queue.enqueue("B")

    queue.enqueue("C")



    print("Front:", queue.peek_front())

    print("Dequeue:", queue.dequeue())

    print("Dequeue:", queue.dequeue())



    # Test circular wrap-around

    queue.enqueue("D")

    queue.enqueue("E")



    print("After wrap-around:")

    if hasattr(queue, "display"):

        queue.display()



    print("Dequeue:", queue.dequeue())

    print("Dequeue:", queue.dequeue())

    print("Dequeue:", queue.dequeue())

    print("Is empty:", queue.is_empty())



    try:

        queue.dequeue()

    except (IndexError, OverflowError) as error:

        print("Underflow test passed:", error)



    queue.enqueue("X")

    queue.enqueue("Y")

    queue.enqueue("Z")



    try:

        queue.enqueue("W")

    except (IndexError, OverflowError) as error:

        print("Overflow test passed:", error)





def test_linked_queue():

    print("\n--- TEST LINKED QUEUE ---")



    queue = LinkedQueue()



    queue.enqueue("A")

    queue.enqueue("B")



    print("Front:", queue.peek_front())

    print("Dequeue:", queue.dequeue())

    print("Dequeue:", queue.dequeue())

    print("Is empty:", queue.is_empty())



    try:

        queue.dequeue()

    except (IndexError, OverflowError) as error:

        print("Underflow test passed:", error)





if __name__ == "__main__":

    test_array_stack()

    test_linked_stack()

    test_array_queue()

    test_linked_queue()



    print("\nAll test functions finished.")

