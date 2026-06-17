'''
Option 1: make list with every node and check if in list
Option 2: replace node with dummy node if .next is a dummy node 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None or head.next == None:
            return False

        turtoise = head
        hare = head.next

        while hare is not None:
            if turtoise == hare:
                return True
            if hare.next is None or hare.next.next is None:
                return False
            turtoise = turtoise.next
            hare = hare.next.next
        return False 
    
        

        

        