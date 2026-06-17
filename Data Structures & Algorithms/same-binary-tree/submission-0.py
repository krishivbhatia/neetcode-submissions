# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
recursion with passing in node.left, node.right
if nodes not equal or non existing --> false
isSameTree(.left)
isSameTreee(.right)
--> true
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.equiv = True
        def compareHelper(pNode, qNode):
            if pNode is None and qNode is not None or pNode is not None and qNode is None:
                self.equiv = False 
                return
            if pNode is None and qNode is None:
                return
            
            if pNode.val != qNode.val:
                self.equiv = False 
            compareHelper(pNode.left, qNode.left)
            compareHelper(pNode.right, qNode.right)


        compareHelper(p, q)
        return self.equiv



        