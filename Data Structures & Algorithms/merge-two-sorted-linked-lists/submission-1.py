# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Loop through LL1. Once val in LL2 > current val 
--> make new val point to it. 
Store current referneces and move onto next


    

'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newList = ListNode(0, None)
        returnP = newList
        curr1 = list1 
        curr2 = list2

        while curr1 is not None:
            if curr2 is not None and (curr1.val >= curr2.val):
                newList.next = ListNode(curr2.val, None)
                newList = newList.next
                curr2 = curr2.next 
            else:
                newList.next = ListNode(curr1.val, None)
                newList = newList.next
                curr1 = curr1.next 
                        
        while curr2 is not None: 
            newList.next = ListNode(curr2.val, None)
            newList = newList.next
            curr2 = curr2.next
                    
        
    
        return returnP.next
        

        