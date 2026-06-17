'''
Forwad Loop, Backward Loop
if crated lists = --> true
Runtime: N
can stop halfway 


'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        listForward = []
        listBackward = []
        for i in range(0, len(s), 1):
            if s[i].isalnum():
                listForward.append(s[i].lower())
                print("Forward", s[i].lower())
        for j in range(len(s)-1, -1, -1):
            if s[j].isalnum():
                listBackward.append(s[j].lower())
                print("Backwards", s[j].lower())
        if listForward == listBackward:
            return True 
        return False



        