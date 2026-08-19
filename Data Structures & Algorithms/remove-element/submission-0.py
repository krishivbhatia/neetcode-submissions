class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # given num array, remove occurances of val, return # relevant

        # inex loop, if num = val, 

        #1 1 3 2 3 2 5 6  
        #1 1 3 3 5 6 

        #problem: can't access previous indx to modify 
        #sol: if bool true, set prev (curr-count) index to val

        pointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pointer] = nums[i]
                pointer = pointer +1
        return pointer
            




        