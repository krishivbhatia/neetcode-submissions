'''
var highest
Loop through array, calculate every num-current
    store highest (0 if -)
Runtime: N^2 

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highestDiff = 0
        for i in range(len(prices)):
            for j in range(i, len(prices), 1):
                currentDiff = prices[j] - prices[i]
                if currentDiff > highestDiff:
                    highestDiff = currentDiff;

        return highestDiff






        