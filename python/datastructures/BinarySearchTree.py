"""
Binary Search Tree Class
@author Avinash Rai

STRICT rule enforced i.e. Left ≤ Node ≤ Right *
ITERATIVE approach on traversal methods rather than RECURSIVE because python
has a recursion depth limit (~1000 by default) and may hit RecursioneError on large trees.

Methods overview:
    - insert(value)
    - contains(value)
    - remove(value)
    - print()
    - size()
    - depth()
    - min()
    - max()
    - isEmpty()
    - isBalanced()
"""
from datastructures.LeftRightNode import LeftRightNode
from datastructures.Stack import Stack

class BinarySearchTree:
    """
    Create an instance of Binary Search Tree class
    Private Members:-
        - root pointer
    """
    def __init__(self)->None:
        self.__root = None
        self.__size = 0 

    """
    Adds a node to the tree.
        No duplicates allowed
    @return Boolean
    Complexity: T:O(log n) S:O(1)
    """
    def insert(self, value:any)->bool:
        newNode = LeftRightNode(value)
        
        if self.__root == None:
            self.__root = newNode
            self.__size += 1
            return True
        
        current = self.__root
        while True:
            if value == current.value:
                return False
            if value < current.value:
                if current.left == None:
                    current.left = newNode
                    self.__size += 1
                    return True
                current = current.left
            else:
                if current.right == None:
                    current.right = newNode
                    self.__size += 1
                    return True
                current = current.right

    """
    Check if the tree contains a given value.
    @return Boolean - True if found
    Complexity: T:O(log n) S:O(1)
    """
    def contains(self, value:any)->bool:
        if self.__root == None:
            return False
        current = self.__root
        while current is not None:            
            if value == current.value:
               return True
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return False
    
    """
    Removes the node from tree if found
        Cases: No children, One child and Two children (in-order succession)
        Parent tracking
    @return Boolean
    Complexity: T:O(log n) S:O(1)
    """
    def remove(self, value: any) -> bool:
        parent = None
        current = self.__root

        while current:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                # Node found
                if current.left is not None and current.right is not None:
                    # Case 3: Two children → find in-order successor
                    succ_parent = current
                    succ = current.right
                    while succ.left is not None:
                        succ_parent = succ
                        succ = succ.left
                    current.value = succ.value  # Replace value

                    # Remove successor node
                    if succ_parent.left == succ:
                        succ_parent.left = succ.right
                    else:
                        succ_parent.right = succ.right

                else:
                    # Case 1 or 2: 0 or 1 child
                    child = current.left if current.left else current.right
                    if parent is None:
                        self.__root = child  # Removing root
                    elif parent.left == current:
                        parent.left = child
                    else:
                        parent.right = child

                self.__size -= 1
                return True

        return False

    """
    Print indented Tree structure
    Rotated 90 degree counter-clockwise
    Complexity: T:O(n) S:O(1)
    """
    def print(self) -> None:
        def _print(node, level=0):
            if node is not None:
                _print(node.right, level + 1)
                print('    ' * level + f'→ {node.value}')
                _print(node.left, level + 1)

        _print(self.__root)

    """
    Returns the number of nodes in the tree.
    @return int
    Complexity: O(1)
    """
    def size(self)->int:
        return self.__size

    """
    Returns the maximum depth of the tree
        Utilises the Stack class
    @return int
    Complexity: O(n)
    """
    def depth(self)->int:
        if self.__root is None:
            return 0
        
        max_depth = 0
        stack = Stack()
        stack.push((self.__root, 1))

        while not stack.isEmpty():
            node, level = stack.pop().value
            if node is not None:
                max_depth = max(max_depth, level)
                stack.push((node.left, level + 1))
                stack.push((node.right, level + 1))
        
        return max_depth              

    """
    Return the minimum value of the tree
    @return any
    Complexity: T:O(log n) worst-case O(n) S:O(1)
    """
    def min(self)->any:
        if self.__root is None:
            return None
        current = self.__root
        while current.left is not None:
            current = current.left
        return current.value

    """
    Return the maximum value of the tree
    @return any
    Complexity: T:O(log n) worst-case O(n) S:O(1)
    """
    def max(self)->any:
        if self.__root is None:
            return None
        current = self.__root
        while current.right is not None:
            current = current.right
        return current.value

    """
    Checks if the tree is empty.
    @return boolean
    Complexity: O(1)
    """
    def isEmpty(self)->bool:
        if self.__size > 0:
            return False
        return True

    """
    Checks if the tree is balanced
    @return boolean
    Complexity: O(n)
    """
    def isBalanced(self) -> bool:
        if self.__root is None:
            return True

        stack = Stack()
        stack.push((self.__root, False))
        depths = {}

        while not stack.isEmpty():
            node, visited = stack.pop().value
            if node is None:
                continue

            if not visited:
                stack.push((node, True))
                stack.push((node.right, False))
                stack.push((node.left, False))
            else:
                left = depths.get(node.left, 0)
                right = depths.get(node.right, 0)
                if abs(left - right) > 1:
                    return False
                depths[node] = 1 + max(left, right)

        return True