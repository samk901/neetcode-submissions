class Solution:

    # We need to be able to demarcate how long a string is
    # Then the decoder would be able to reconstruct the list. 
    # Add a special character to delineate and a number to indicate how many chars

    # The same character can appear in word, since we will always add a char


    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)))
            result.append("#")
            result.append(s)
        
        return "".join(result)


    def decode(self, s: str) -> List[str]:

        # Now to create the list we need to go through the string. 
        # Maintain two pointers probably
        # Iterated until we hit #, this section is our string length
        # Move pointer string length after #, this is our string

        i = j = 0
        res = []

        #Iterate through teh entire string
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res

