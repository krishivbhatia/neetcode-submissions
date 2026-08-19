class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max = 0
        for num in nums:
            print(num)
            if num==1:
                print("reached")
                counter=counter+1
                if counter>max:
                    max = counter
                
            else:
                counter = 0 
        return max


        