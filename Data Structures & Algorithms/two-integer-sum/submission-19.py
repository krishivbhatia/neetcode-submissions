'''

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}
        for i in range(len(nums)):
            numCurrent = nums[i]
            numWanted = target - numCurrent 
            if numWanted in dic:
                return [dic[numWanted],i]
            dic[numCurrent] = i 

            











        '''
        Correect: N^2 runtime
        for num in nums:
            val2 = target-num 
            val1Inx = nums.index(num)
            if num != val2:
                if val2 in nums:
                    return [nums.index(num), nums.index(val2)]
            else:
                copyList = nums[:]
                copyList.remove(num)
                if val2 in copyList:
                    return[nums.index(num), copyList.index(num)+1]
        '''

                




        



        

        