class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = j = 0

        while i < len(s):
            j = i
            # Get the chars that indicate length
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            
            # now set i to the char after #
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res



