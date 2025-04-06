"""
HashTable Class
@author Avinash Rai

Uses "Seperate Chaining" method using Python Lists for Collision Handling.
Python List are amortized thus appending to the list are O(1). 
When the list runs out of capacity, Python automatically resizes the internal memory buffer (usually 2×)

Methods overview:
    - _hash(key) Private method
    - setItem(key,value)
    - getItem(key)
    - keys()
    - remove(key)
    - keyExists(key)
    - print()
    - capacity()
    - numItems()
    - isEmpty()
    - resize()
    - clear()
"""
class HashTable:
    """
    Creates a hash table using a Python list to store key-value pairs.
    Private Members:-
        - map Python List structure to hold the data. Default size is 10
    """
    def __init__(self, size=10):
        self.__map = [None] * size

    """
    Private method - Computes a hash value for the given key.
    @return int
    Complexity: T:O(k), where k = length of the key | S:O(1)
    """
    def __hashSum(self, key):
        hash_sum = 0
        for char in key:
            hash_sum = (hash_sum + ord(char) * 23) % len(self.__map)
        return hash_sum

    """
    Inserts or updates a key-value pair in the hash table.
    @return Bool
    Complexity: T:O(k), where k = length of the key | S:O(1)
    """
    def setItem(self, key:any, value:any)->bool:
        if value is None:
            return False
        index = self.__hashSum(key)

        if self.__map[index] == None:
            self.__map[index] = []
        
        for item in self.__map[index]:
            if item[0] == key:
                item[1] = value
            return True

        self.__map[index].append([key,value])
        return True
    
    """
    Retrieves the value for a given key.
    @return any
    Complexity: T:O(k), where k = length of the key | S:O(1)
    """
    def getItem(self, key:any)->any:
        index = self.__hashSum(key)
        if self.__map[index] == None:
            return None
        for k,v in self.__map[index]:
            if k == key:
                return v
        return None        
    
    """
    Returns a list of all keys in the hash table.
    @return List
    Complexity: O(n)
    """
    def keys(self)->list:
        all_keys = []
        for item in self.__map:
            if item is not None:
                for k,_ in item:
                    all_keys.append(k)
        return all_keys

    """
    Removes the key-value pair if the key exists
    @return Bool
    Complexity: T:O(k), where k = length of the key | S:O(1)
    """
    def remove(self, key: any) -> bool: 
        index = self.__hashSum(key)
        if self.__map[index] is None:
            return False
        for i in range(len(self.__map[index])):
            if self.__map[index][i][0] == key:
                self.__map[index].pop(i)
                return True
        return False

    """
    Check if a key exists in the HashTable
    @return bool
    Complexity: T:O(k), where k = length of the key | S:O(1)
    """
    def keyExists(self, key:any)->any:
        index = self.__hashSum(key)
        if self.__map[index] == None:
            return False
        for k,v in self.__map[index]:
            if k == key:
                return True
        return False    

    """
    Prints the contents of the hash table (index and bucket values)
    Complexity: T:O(n) S:O(1)    
    """
    def print(self):
        for i, val in enumerate(self.__map): 
            print(i, ": ", val)

    """
    Current Capacity of the Hash Table
    @return int
    Complexity: O(1)
    """
    def capacity(self)->int:
        return len(self.__map)
    
    """
    Returns the number of key-value pairs stored in the hash table.
    @return int
    Complexity: T:O(n), S:O(1)
    """
    def numItems(self)->int:
        no_of_items = 0
        for item in self.__map:
            if item is not None:
                no_of_items += len(item)
        return no_of_items

    """
    Checks if the Hash Table is empty.
    @return boolean
    Complexity: T:O(n) S:O(1)
    """
    def isEmpty(self)->bool:
        for item in self.__map:
            if item is not None:
                if len(item) > 0:
                    return False
        return True

    """
    Resize  
    @return None
    Complexity: T:O(n) S:O(1)
    """    
    def resize(self):
        pass 
    
    """
    Clears all items 
    @return None
    Complexity: T:O(n) S:O(1)
    """
    def clear(self)->None:
        for i in range(len(self.__map)):
            self.__map[i] = None
