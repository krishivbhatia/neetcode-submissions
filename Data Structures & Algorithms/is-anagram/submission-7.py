'''
If the map is capped at a certain amount (ie 26), its O(1) 

loop through word 1 (time N)
    if letter not in hashmap: 
        add to hashmap with 1 value, store count = 1 
    if letter in hashmap: 
        count += 1, modiidfy value 
repat for second word   (time M)
anotehr loop to compare values (time 1 ) --> M+N time 
        


'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map1 = {}
        hash_map2 = {}
        if len(s) != len(t):
            return False
        
        for letter1 in s:
            if letter1 not in hash_map1:
                hash_map1[letter1] = 1
            if letter1 in hash_map1:
                hash_map1[letter1] = hash_map1[letter1] + 1

    
        for letter2 in t:
            if letter2 not in hash_map2:
                hash_map2[letter2] =1 
            if letter2 in hash_map2:
                hash_map2[letter2] = hash_map2[letter2] + 1


        for letter_f in s:
            if letter_f not in hash_map2 or hash_map1[letter_f] != hash_map2[letter_f]:
                return False
        return True


        
        

















        '''

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

         
            