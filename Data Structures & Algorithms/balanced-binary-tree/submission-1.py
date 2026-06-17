# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Runtime: O(N)
Space Complexity: O(h)
    space correspodns to depth of recursion stack
    (constant var stores top node, child, child, etc --> height)
return true/false
recursion: subtree heights
    helperFunc returns height of subtr
if any call, |left-right| > 1: false

def func():
    if node empty return 0
    left = call
    right = call
    if |left-right|>1: false
    return 1+max(left right)
'''


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True 

        def heightHelper(node):
            if node == None:
                return 0 
            left = heightHelper(node.left)
            right = heightHelper(node.right)
            if abs(left-right) > 1:
                self.balanced = False 
            return 1+max(left, right)

        heightHelper(root)
        return self.balanced 



        