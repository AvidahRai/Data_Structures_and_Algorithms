"""
TwoPointerNode Class
@author Avinash Rai

Contains both reference to PREVIOUS and NEXT pointers.
"""
class TwoPointerNode:
    def __init__(self:object, value:any)->None:
        self.value = value
        self.previous = None
        self.next = None