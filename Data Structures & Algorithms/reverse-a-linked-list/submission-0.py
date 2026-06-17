# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Loop through linked list --> add vals to a list 
loop backwards through list --> modify linked list 


'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
                







        