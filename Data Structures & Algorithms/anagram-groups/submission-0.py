class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            count = [0] * 26 # the ID of each s
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            ID = tuple(count)
            if ID not in seen:
                seen[ID] = []
            
            seen[ID].append(s)
        
        return list(seen.values()) 