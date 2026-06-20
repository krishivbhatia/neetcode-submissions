'''
Used Solution:
Runtime: N log N [built insort]
Space: N [built in sort + loop]
Spacee Complexity:
sort interval by first val
loop over intervals
if end of prev and start of current dont overlap



Solution #1: 
for loop for each meeting 
--> compare start and end to each valu 
 (if alreeady compared stop)
Runtime: 1+2+3..N --> N^2 

Solution #2: 
Sort start times array
Sort end times array
if theey don't correspond exactly --> false 
using .sort 

Runtime:
.sort (N log N)
compare vals: N 


'''

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start) 
        for i in range(1, len(intervals)):
            interval1 = intervals[i-1]
            interval2 = intervals[i]
            
            if interval1.end > interval2.start:
                return False
        return True 


        
        


