'''
Solution #1:
Recursion
        if n == 1:
            return 1
        if n==2:
            return 2 
        return self.climbStairs(n-1) + self.climbStairs(n-2)

Runtime: 2^N
Space Complexity: N

Solution #2:would be constant space complexity
with two variabls instead of an array




Solution Used: 
Dynamic Programming, store answers in array 
Runtime: O(N)
Space Complexity: O(N)
  (array storage)
  
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n ==2:
            return 2
        dpStore = [1,2]
        for i in range(2,n):
            dpStore.append(dpStore[i-1] + dpStore[i-2])
        return dpStore[-1]
        

        
        

        