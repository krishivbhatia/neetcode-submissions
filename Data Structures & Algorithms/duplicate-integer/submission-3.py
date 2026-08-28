'''
empty list 
for loop though array
if value is in list --> return true
else return false 

'''




class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return True
            hash_map[num] = 0
        return False

















        '''
        contains = set()
        for num in nums:
            if num in contains:
                return True
            contains.add(num)
        return False
        '''
        