# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head 
        while curr:
            currNext = curr.next
            curr.next = prev 
            prev = curr
            curr = currNext
        return prev

# runtime: n
# space 1
# space:

    

'''
1 -> 2 -> 3 -> 4 

1. save refernece of curr.next to curr.next.next 
2. curr.next point to curr
3. move to curr.next 

1 -> 2 -> 3 -> 4 
'''


        










'''
        prev = None 
        curr = head 
        while curr is not None:
            nxt = curr.next 
            curr.next = prev 
            prev = curr
            curr = nxt 
        return prev

        
        curr = head 
        tempList = []
        while curr is not None:
            tempList.append(curr.val)
            curr = curr.next 
        print(tempList)
        

        curr2 = head 
        head2 = curr2
        for i in range(len(tempList)-1, -1, -1):
                curr2.val = tempList[i]
                curr2 = curr2.next 

        return head2



        

Solution 1: New List
Loop through linked list --> add vals to a list 
loop backwards through list --> modify linked list 
Runtime: N
Space complexity: N

Solution 2: Pointers 

'''

                







        