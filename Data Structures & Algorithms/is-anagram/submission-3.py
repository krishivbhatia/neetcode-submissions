'''
loop through string1 --> if string2 doesnt contain --> false
                            if string 1 and string2 contains --> string slice
if list not empty --> false | retuern tre
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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

         
            


        