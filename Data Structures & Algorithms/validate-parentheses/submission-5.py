'''
append & pop 
Set up dictionary. closing before opening because 
    that means already looped through earlier
Loop through list, 
    if val is closing
       if stack is not empty AND pop stack key--> val ==
            good, stack.pop
       else:
          return false 
    else val opening   
        stack.append 
    return true if stack empty; false otherwise 

'''
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        h_punc = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for punc in s:
            if punc in h_punc:
                if stack and stack[-1] == h_punc[punc]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(punc)

        if not stack:
            return True
        return False






        
        

        
            


















        
        