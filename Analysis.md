# Analysis 

1.  A linked-list stack performs pish and pop operators at te head because it is faster. These operators take O(1) time.If we use the tail in a singly linked list, we need to traverse all nodes first which take O(n) time. Using the head makes the stack efficient and follows the LIFO principle.


2.  An array queue should be circular so that we can reuse the empty spaces at the front of the array after dequeues. If is not circular, the rear will reach the end of the start. A circular array queue makes both enqueue and dequeue O(1) and saves memory.
