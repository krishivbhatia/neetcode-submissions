'''
loop through string1 --> if string2 doesnt contain --> false
                            if string 1 and string2 contains --> string slice
if list not empty --> false | retuern tre
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # count numbr of characters
        sCounts = {}
        for charVal in s:
            if charVal not in sCounts:
                sCounts[charVal] = 1
            else:
                sCounts[charVal] = sCounts[charVal]+1
    

        tCounts = {}
        for charVal in t:
            if charVal not in tCounts:
                tCounts[charVal] = 1
            else:
                tCounts[charVal] = tCounts[charVal]+1

        if len(sCounts) != len(tCounts):
            return False

        # loop over one dic and compare with othrs
        for key in sCounts:
            if key not in tCounts or tCounts[key] != sCounts[key]:
                return False

        return True
            
            



        '''
        Time complexity: O(n^2)
        charHolder = []
        while s != "":
            print("loop")
            i = 0;
            charAt = s[i]
            if charAt not in t:
                return False
            # error if only 1 element 

            s = s[1:] 
  
            t = t[0: t.index(charAt)] + t[t.index(charAt)+1:]
        if s!="" or t != "":
            return False
        return True 
        '''

         
            


        