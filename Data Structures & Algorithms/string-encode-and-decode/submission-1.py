class Solution:

    def encode(self, strs: List[str]) -> str:        
        res = []
        for index, s in enumerate(strs):
            res.append(str(len(s)) + "#" + s)
        
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        index = 0
        res = []
        while index < len(s):
            num = ""
            while s[index] != '#':
                num += s[index]
                index += 1
            
            res.append(s[index+1 : index + 1 + int(num) : 1])
            index = index + int(num) + 1

        return res