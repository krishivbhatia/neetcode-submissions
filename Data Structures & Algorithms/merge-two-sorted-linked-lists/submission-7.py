# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next





class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy 
        while list1 and list2:
            if list1.val<list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next 
            tail = tail.next 


            
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next


        # Runtime: O(n+m)
        # SPace: O(1) (weird)
            # since each node points to the list nodes, it doesn't create any new nodes so it's 1. 














'''
        newList = ListNode(0)
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




Loop through LL1. Once val in LL2 > current val 
--> make new val point to it. 
Store current referneces and move onto next
Runtime: O(N+M)
Space Complexity: O(N+M)


    

'''
        

        