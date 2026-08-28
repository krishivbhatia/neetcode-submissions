'''
every unique key (w/ index val): add to hashmap
if target-key is in hashmap 
--> return idnices

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Runtime: n
        # Space: n
        hash_map = {}
        index = 0
        for num in nums:
            #if num not in hash_map:
               # hash_map[num] = index
            if target-num in hash_map:
                return [hash_map[target-num], index]
            hash_map[num] = index
            index+=1
        return[0,1]
        















'''
        dic = {}
        for i in range(len(nums)):
            numCurrent = nums[i]
            numWanted = target - numCurrent 
            if numWanted in dic:
                return [dic[numWanted],i]
            dic[numCurrent] = i 

            







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

                




        



        

        