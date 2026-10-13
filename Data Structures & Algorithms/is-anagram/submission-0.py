class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {} # map char to occurence
        for i in s:
            c = count.get(i, 0) + 1
            count[i] = c
        
        for j in t:
            c = count.get(j, 0) - 1
            if c < 0:
                return False
            else:
                count[j] = c
        
        return True
        