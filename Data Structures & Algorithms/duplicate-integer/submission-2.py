'''
empty list 
for loop though array
if value is in list --> return true
else return false 

'''




class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains = set()
        for num in nums:
            if num in contains:
                return True
            contains.add(num)
        return False
        