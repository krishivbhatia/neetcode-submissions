# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''

Original Approach:
make list of all nodes while looping through tree
     --> max height of every individual tree
loop over max height's
--> if tree's dont overlap, add them together


Optimal Approach:
For one treee: diameter = leftHeight + rightHeight 
store global max diameter
recursivly call with each subtree
height of a nod is 1+max(left, right) to aovidrecalculating

Need to return diameter (solution)
and height for calculating diamtet --> nested func 
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxVal = 0 

        def heightGet(curr):
            if curr == None:
                return 0 
            left = heightGet(curr.left)
            right = heightGet(curr.right)
            self.maxVal = max(self.maxVal, left+right)
            return 1+max(left, right)

        heightGet(root)
        return self.maxVal



        

        