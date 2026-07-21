class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # let's create a character count array for each word
        # Then store those words in a way where we can return the list
        # Let's add it to a hashmap
        # Hash map will have (k,v) --> character array, [] of words
        # We will need to convert the char count array to a tuple
        # becuase keys should be immutable

        group_map = defaultdict(list)

        for word in strs:

            char_count = [0] * 26

            for char in word:
                char_count[ord(char) - ord('a')] += 1
            
            group_map[tuple(char_count)].append(word)
        

        return list(group_map.values())
        