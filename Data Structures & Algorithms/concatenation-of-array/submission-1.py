class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        pre_length = len(nums)
        for i in range(pre_length):
            ans.append(nums[i])
        
        for j in range(pre_length):
            ans.append(nums[j])
        return ans
        

        # time: n
        # space: n


        