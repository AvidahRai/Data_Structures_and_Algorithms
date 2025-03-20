"""
Stack Class
@author Avinash Rai

LIFO (Last in First Out)
Unlimited size Stack

Methods overview:
    - push(value)
    - peek()
    - pop()
    - print()
    - size()
    - isEmpty()
    - clear()
"""
from datastructures.Node import Node

class Stack:
    """
    Create an instance of Stack class
        Initialize with a value or create an empty stack.
    
    Private Members:-
        - top (Node): Pointer to the top of the stack
        - size (int): Keeps track of the number of elements
    """
    def __init__(self, value=None)->None:
        if value:
            newNode = Node(value)
            self.__top = newNode
            self.__size = 1
        else:
            self.__top = None
            self.__size = 0

    """
    Adds a new node at the top of the stack.
    @return Boolean - True when successful
    Complexity: O(1)    
    """
    def push(self, value:any)->bool:
        newNode = Node(value)
        newNode.next = self.__top
        self.__top = newNode        
        self.__size += 1
        return True

    """
    View the top value of the stack without removing it.
    @return any
    Complexity: O(1)
    """
    def peek(self)->any:
        if self.__top:
            return self.__top.value
        return None

    """
    Removes the top node from the stack and return it.
    @returns Node/none 
    Complexity: O(1)
    """
    def pop(self)->Node:
        if self.__size == 0:
            return None
        temp = self.__top
        self.__top = self.__top.next
        temp.next = None
        self.__size -= 1
        return temp

    """
    Print the contents of the stack from top to bottom.
    @return None
    Complexity: T:O(n) S:O(1)
    """
    def print(self)->None:
        temp = self.__top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    """
    Size/height of the stack
    @return int
    Complexity: O(1)
    """
    def size(self)->int:
        return self.__size

    """
    Checks if the stack is empty.
    @return boolean
    Complexity: O(1)
    """
    def isEmpty(self)->bool:
        if self.__size > 0:
            return False
        return True

    """
    Clears all items in the stack
    @return None
    Complexity: O(1)
    """
    def clear(self)->None:
        self.__top = None
        self.__size = 0