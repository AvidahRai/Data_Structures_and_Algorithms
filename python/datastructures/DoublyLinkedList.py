"""
Doubly LinkedList Class
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
from datastructures.TwoPointerNode import TwoPointerNode
class DoublyLinkedList:
    """
    Create an instance of Doubly Linked List class
        Initialize with a value or create an empty list
    Private Members:-
        - head pointer
        - tail pointer
        - length counter
    """
    def __init__(self, value=None)->None:
        if value:
            newNode = TwoPointerNode(value)
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
    def append(self, value:any)->bool:
        newNode = TwoPointerNode(value)
        if self.__length == 0:
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.next = newNode
            newNode.previous = self.__tail
            self.__tail = newNode
        self.__length += 1
        return True

    """
    Add a node at the beginning of the list.
    @return Boolean
    Complexity: O(1)
    """
    def prepend(self, value:any)->bool:
        newNode = TwoPointerNode(value)
        if self.__length == 0:
            self.__head = newNode
            self.__tail = newNode
        else:
            newNode.next = self.__head
            self.__head.previous = newNode
            self.__head = newNode
        self.__length += 1
        return True
    
    """
    Removes the last node from the list and return it.
    @return TwoPointerNode/None 
    Complexity: T:O(1) S:O(1)
    """
    def pop(self)->TwoPointerNode:
        if self.__length == 0:
            return None
        temp = self.__tail
        if self.__length == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = self.__tail.previous
            self.__tail.next = None
            temp.previous = None
        self.__length -= 1
        return temp

    """
    Removes the first node from the list.
    @return TwoPointerNode
    Complexity: O(1)
    """
    def popFirst(self)->TwoPointerNode:
        if self.__length == 0:
            return None
        temp = self.__head
        if self.__length == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.previous = None
            temp.next = None
        self.__length -= 1
        return temp 

    """
    Removes a node at a specific position.
    @return TwoPointerNode/None
    Complexity: T:O(n) S:O(1)
    """
    def removeByIndex(self, index:int)->TwoPointerNode:
        if index < 0 or index >= self.__length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.__length - 1:
            return self.pop()
        temp = self.getByIndex(index)
        temp.next.previous = temp.previous
        temp.previous.next = temp.next
        temp.next = None
        temp.previous = None
        self.__length -= 1
        return temp

    """
    Search for a value and remove the first node if found.
    @return TwoPointerNode/none
    Complexity: T:O(n) S:O(1)
    """
    def removeByValue(self, value:any)->TwoPointerNode:
        temp = self.__head
        while temp is not None:
            if temp.value == value:
                if temp == self.__head:
                    return self.popFirst()
                if temp == self.__tail:
                    return self.pop()
                temp.previous.next = temp.next
                temp.next.previous = temp.previous
                temp.next = None
                temp.previous = None
                self.__length -= 1
                return temp  # Return the removed node
            temp = temp.next
        return None

    """
    Returns the node at a given index.
    @return TwoPointerNode/None
    Complexity: T:O(n/2) S:O(1)
    """
    def getByIndex(self, index: int) -> TwoPointerNode:
        if index < 0 or index >= self.__length:
            return None

        if index == 0:
            return self.__head
        if index == self.__length - 1:
            return self.__tail
    
        if index < self.__length // 2:
            temp = self.__head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.__tail
            for _ in range(self.__length - 1, index, -1):
                temp = temp.previous

        return temp

    """
    Updates the node at a specific index.
    @return bool - True if updated
    Complexity: T:O(n) S:O(1)
    """
    def setByIndex(self, index:int, value:any)->bool:
        temp = self.getByIndex(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    """
    Returns the index of the first node containing the given value.
    @return TwoPointerNode/None
    Complexity: T:O(n) S:O(1)
    """
    def find(self, value:any)->TwoPointerNode:
        temp = self.__head
        while temp is not None:
            if temp.value == value:
                return temp
            temp = temp.next
        return None

    """
    Print all items in the list
    Complexity: T:O(n) S:O(1)
    """
    def print(self)->None:
        temp = self.__head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    """
    Length/size of the list
    @return int
    Complexity: O(1)
    """
    def length(self)->int:
        return self.__length
    
    """
    Checks if the list is empty.
    @return boolean
    Complexity: O(1)
    """
    def isEmpty(self)->bool:
        if self.__length > 0:
            return False
        return True
    
    """
    Reverses the list.
    @return Boolean - True if operation completed
    Complexity: T:O(n) S:O(1)  
    """
    def reverse(self)->bool:
        if self.__length == 0:
            return False
        if self.__length == 1:
            return True
        
        temp = self.__head
        self.__head, self.__tail = self.__tail, self.__head

        while temp:
            temp.next, temp.previous = temp.previous, temp.next
            temp = temp.previous

        return True