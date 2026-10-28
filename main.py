from array_stack import ArrayStack

from linked_stack import LinkedStack

from array_queue import ArrayQueue

from linked_queue import LinkedQueue





def display_stack(stack):

    if hasattr(stack, "items") and isinstance(stack.items, list):

        print("Stack state:", stack.items)

        return



    node = getattr(stack, "top", None)

    if node is None:

        node = getattr(stack, "head", None)



    values = []

    visited = set()



    while node is not None and id(node) not in visited:

        visited.add(id(node))

        value = getattr(node, "data", None)



        if value is None:

            value = getattr(node, "value", None)

        if value is None:

            value = getattr(node, "item", None)



        values.append(value)

        node = getattr(node, "next", None)



    print("Stack state (top to bottom):", values)





def display_queue(queue):

    display_method = getattr(queue, "display", None)



    if callable(display_method):

        display_method()

        return



    if hasattr(queue, "items") and isinstance(queue.items, list):

        if hasattr(queue, "size") and hasattr(queue, "front"):

            values = [

                queue.items[(queue.front + i) % len(queue.items)]

                for i in range(queue.size)

            ] if queue.items else []

            print("Queue state (front to rear):", values)

        else:

            print("Queue state:", queue.items)

        return



    node = getattr(queue, "head", None)

    values = []

    visited = set()



    while node is not None and id(node) not in visited:

        visited.add(id(node))

        value = getattr(node, "data", None)



        if value is None:

            value = getattr(node, "value", None)

        if value is None:

            value = getattr(node, "item", None)



        values.append(value)

        node = getattr(node, "next", None)



    print("Queue state (front to rear):", values)





def stack_menu(stack):

    while True:

        print("\n--- STACK OPERATIONS ---")

        print("1. Push")

        print("2. Pop")

        print("3. Peek")

        print("4. Check if empty")

        print("5. Check if full")

        print("0. Back to Main Menu")



        choice = input("Choose an operation: ")



        if choice == "0":

            break



        try:

            if choice == "1":

                value = input("Enter value to push: ")

                stack.push(value)

                print("Value pushed successfully.")



            elif choice == "2":

                print("Removed:", stack.pop())



            elif choice == "3":

                print("Top value:", stack.peek())



            elif choice == "4":

                print("Stack is empty:", stack.is_empty())



            elif choice == "5":

                print("Stack is full:", stack.is_full())



            else:

                print("Invalid choice.")

                continue



            display_stack(stack)



        except (IndexError, OverflowError, ValueError) as error:

            print("Error:", error)

            display_stack(stack)





def queue_menu(queue):

    while True:

        print("\n--- QUEUE OPERATIONS ---")

        print("1. Enqueue")

        print("2. Dequeue")

        print("3. Peek Front")

        print("4. Check if empty")

        print("5. Check if full")

        print("0. Back to Main Menu")



        choice = input("Choose an operation: ")



        if choice == "0":

            break



        try:

            if choice == "1":

                value = input("Enter value to enqueue: ")

                queue.enqueue(value)

                print("Value added successfully.")



            elif choice == "2":

                print("Removed:", queue.dequeue())



            elif choice == "3":

                print("Front value:", queue.peek_front())



            elif choice == "4":

                print("Queue is empty:", queue.is_empty())



            elif choice == "5":

                print("Queue is full:", queue.is_full())



            else:

                print("Invalid choice.")

                continue



            display_queue(queue)



        except (IndexError, OverflowError, ValueError) as error:

            print("Error:", error)

            display_queue(queue)





def is_balanced(expression):

    stack = []

    matching = {

        ")": "(",

        "]": "[",

        "}": "{"

    }



    for char in expression:

        if char in "([{":

            stack.append(char)



        elif char in ")]}":

            if not stack:

                return False



            if stack.pop() != matching[char]:

                return False



    return len(stack) == 0





def parentheses_exercise():

    expression = input(

        "\nEnter an expression using () [] {}: "

    )



    if is_balanced(expression):

        print("The parentheses are balanced.")

