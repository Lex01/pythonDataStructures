"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:
"""

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node




def has_cycle(head):    #Uses Floyd Turtoise/Hare algorithm
    #One fast, one slow pointer. Fast will overtake slow, loop around, and be equal to slow
    slow = head
    fast = head
    if head == None:
        return False
    while fast != None and fast.next != None: #If reach end of list, it is not looped
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False
u\