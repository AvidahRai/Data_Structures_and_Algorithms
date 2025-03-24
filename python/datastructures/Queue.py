"""
Queue Class
@author Avinash Rai

FIFO (Last in First Out)

Methods overview:
    - enqueue(value)
    - front()
    - dequeue()
    - contains(value)
    - print()
    - length()
    - isEmpty()
    - clear()
"""
from datastructures.Node import Node

class Queue:
    """
    Create an instance of Queue class
        Initialize with a value or create an empty queue.
    
    Private Members:
        - __first (Node): Points to the front of the queue
        - __last (Node): Points to the rear of the queue
        - __length (int): Number of elements in the queue
    """
    def __init__(self, value=None)->None:
        if value:
            newNode = Node(value)
            self.__first = newNode
            self.__last = newNode
            self.__length = 1
        else:
            self.__first = None
            self.__last = None
            self.__length = 0

    """
    Adds a new node to the rear of the queue.
    @return Boolean - True when successful.
    Complexity: O(1)
    """
    def enqueue(self, value:any)->bool:
        newNode = Node(value)
        if self.__length == 0:
            self.__first = newNode
            self.__last = newNode
        else:
            self.__last.next = newNode
            self.__last = newNode
        self.__length += 1
        return True

    """
    View the first value of the queue without removing it.
    @return any
    Complexity: O(1)
    """
    def front(self)->any:
        if self.__length > 0:
            return self.__first.value
        return None

    """
    Removes and returns the front node from the queue.
    @return Node/None
    Complexity: O(1)
    """
    def dequeue(self)->Node:
        if self.__length == 0:
            return None
        temp = self.__first
        if self.__length == 1:
            self.__first = None
            self.__last = None
        else:
            self.__first = self.__first.next
        temp.next = None
        self.__length -= 1
        return temp
    
    """
    Check if the queue contains a given value.
    @return Boolean - True if found
    Complexity: T:O(n) S:O(1)
    """
    def contains(self, value:any)->bool:
        temp = self.__first
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
        return False

    """
    Prints the queue from front to rear.
    @return None
    Complexity: T:O(n) S:O(1)
    """
    def print(self)->None:
        temp = self.__first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    """
    Returns the number of elements in the queue.
    @return int
    Complexity: O(1)
    """
    def length(self)->int:
        return self.__length

    """
    Checks if the queue is empty.
    @return boolean
    Complexity: O(1)
    """
    def isEmpty(self)->bool:
        if self.__length > 0:
            return False
        return True

    """
    Clears all elements in the queue.
    @return None
    Complexity: O(1)
    """
    def clear(self)->None:
        self.__first = None
        self.__last = None
        self.__length = 0