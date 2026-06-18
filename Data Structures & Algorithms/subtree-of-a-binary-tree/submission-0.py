# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
sameTree helper method returns if subtree is contained in a particular subset of maintree
loop over main func recursivly to call on children of main tree nodes
base cas if one of them are empty 
return helper(.left) OR helper(.right) if a subtree is contained in either --> true 


'''
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(main, sub):
            if main is None and sub is None:
                return True
            if main is None or sub is None:
                return False 
            if main.val != sub.val:
                return False
            return sameTree(main.left, sub.left) and sameTree(main.right, sub.right)
        
        if root is None:
            return False
        if subRoot is None: # overall thing not recursive case
            return True
        if sameTree(root, subRoot):
            return True 
        # self because method is not in scope of itself --> belongs to overall class
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
        

        
        