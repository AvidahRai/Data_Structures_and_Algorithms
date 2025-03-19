"""
LinkedList Class
@author Avinash Rai

Methods overview:
    - append(value)
    - prepend(value)
    - pop()
    - popFirst()
    - removeByIndex(index)
    - removeByValue(value)
    - getByIndex(index)
    - setByIndex(index, value)
    - find(value)
    - print()
    - length()
    - isEmpty()
    - reverse()
"""
from datastructures.Node import Node
class LinkedList:
    """
    Create an instance of Linked List class
        Initialize with a value or empty list
    Private Members:-
        - head pointer
        - tail pointer
        - length counter
    """
    def __init__(self:object, value=None)->None:
        if value:
            newNode = Node(value)
            self.__head = newNode
            self.__tail = newNode
            self.__length = 1
        else:
            self.__head = None
            self.__tail = None
            self.__length = 0

    """
    Adds a node at the end of the list.
    @return Boolean
    Complexity: T:O(1) S:O(1)
    """
    def append(self:object, value:any)->bool:
        newNode = Node(value)
        if self.__length == 0:
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = newNode
        self.__length += 1
        return True
    
    """
    Add a node at the beginning of the list.
    @return Boolean
    Complexity: O(1)
    """
    def prepend(self:object, value:any)->bool:
        newNode = Node(value)
        if self.__length == 0:
            self.__head = newNode
            self.__tail = newNode
        else:
            newNode.next = self.__head
            self.__head = newNode
        self.__length += 1   
        return True
    
    """
    Removes the last node from the list and return it.
    @return Node
    Complexity: T:O(n) S:O(1)
    """
    def pop(self:object)->Node:
        if self.__length == 0:
            return None
        temp = self.__head
        prev = self.__head
        
        while temp.next is not None:
            prev = temp
            temp = temp.next

        self.__tail = prev
        self.__tail.next = None
        self.__length -= 1

        if self.__length == 0:
            self.__head = None
            self.__tail = None

        return temp

    """
    Removes the first node.
    @return Node
    Complexity: O(1)
    """
    def popFirst(self:object)->Node:
        if self.__length == 0:
            return None        
        
        temp = self.__head
        self.__head = self.__head.next
        temp.next = None
        self.__length -= 1

        if self.__length == 0:
            self.__head = None
            self.__tail = None

        return temp

    """
    Removes a node at a specific position.
    @return Node/none
    Complexity: T:O(n) S:O(1)
    """
    def removeByIndex(self:object, index:int)->Node:
        if index < 0 or index >= self.__length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.__length - 1:
            return self.pop()
        prev = self.getByIndex(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.__length -= 1
        return temp

    """
    Search for a value and remove the first node found.
    @return Node/none
    Complexity: T:O(n) S:O(1)
    """
    def removeByValue(self:object, value:any)->Node:
        temp = self.__head
        prev = None

        while temp is not None:
            if temp.value == value:
                if prev is not None:
                    prev.next = temp.next
                else:
                    self.__head = temp.next

                if temp == self.__tail:
                    self.__tail = prev
                
                self.__length -= 1
                return temp
        
            prev = temp
            temp = temp.next
        
        return None

    """
    Returns the node at a given index.
    @return Node/None
    Complexity: T:O(n) S:O(1)
    """
    def getByIndex(self:object, index:int)->Node:
        if index < 0 or index >= self.__length:
            return None
        temp = self.__head
        for i in range(index):
            temp = temp.next
        return temp

    """
    Updates the node at a specific index.
    @return bool - True if updated
    Complexity: T:O(n) S:O(1)
    """
    def setByIndex(self:object, index:int, value:any)->bool:
        temp = self.getByIndex(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    """
    Returns the index of the first node containing the given value.
    @return Node/none
    Complexity: T:O(n) S:O(1)
    """
    def find(self:object, value:any)->Node:
        temp = self.__head
        while temp:
            if temp.value == value:
                return temp
            temp = temp.next
        return None
    
    """
    Print all items in the Linked List
    Complexity: T:O(n) S:O(1)
    """
    def print(self:object)->None:
        temp = self.__head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    """
    Length/size of the Linked List
    @return int
    Complexity: O(1)
    """
    def length(self:object)->int:
        return self.__length
    
    """
    Checks if the list is empty.
    @return boolean
    Complexity: O(1)
    """
    def isEmpty(self:object)->bool:
        if self.__length > 0:
            return False
        return True

    """
    Reverses the linked list.
    @return Boolean - True if operation completed
    Complexity: T:O(n) S:O(1)
    """
    def reverse(self:object)->None:
        if self.__length == 0:
            return False
        if self.__length == 1:
            return True
        
        temp = self.__head
        self.__head = self.__tail
        self.__tail = temp

        after = temp.next
        before = None
        for i in range(self.__length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
        return True