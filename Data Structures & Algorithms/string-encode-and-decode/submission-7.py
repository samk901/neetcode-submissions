class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)))
            result.append("#")
            result.append(s)
        
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        i = j = 0 
        result = []

        while i < len(s):
            j = i 
            # find the index where the lenght of string ends
            while s[j] != "#":
                j += 1
            
            # calculate length using index slice
            length = int(s[i:j])

            # now we can start one index after the # to get our string
            i = j + 1
            j = i + length
            result.append(s[i:j])
            
            # now reset for the next len, delimter, word sequence
            i = j
        
        return result
