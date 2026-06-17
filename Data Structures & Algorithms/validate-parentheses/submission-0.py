'''
Loop forward add ({[ to stack
    stack: first in last out 
    queuee: first in first out 
if a )}] is spootted, compare to stack removal 
    if stack empty or wrong element --> false 
if stack is empty at end --> true (else false )


'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charDic = {}
        charDic[")"] = "("
        charDic["]"] = "["
        charDic["}"] = "{"

        for punc in s:
            # open bracket
            if not punc in charDic:
                print("open bracket")
                stack.append(punc)
            # closed bracket
            else:
                if len(stack)>0:
                    print("close bracket")
                    compareChar = stack.pop()
                    if charDic[punc] != compareChar:
                        print("false pop")
                        return False
                else:
                    return False
        if len(stack) != 0:
            print("false len stack")
            return False
        return True 



        
        