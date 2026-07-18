class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # We know that the len of array will be 2 * len(nums)
        # We know that at ans[i] = ans[i + len(nums)]
        # So we can initialize an array of the correct length. 
        # Then in 1 pass, set both i and i + len(nums) index values

        n = len(nums)
        ans = [0] * (2 * n)

        for i, num in enumerate(nums): # enumerate gives us index, value at index in pairs
            ans[i] = ans[i + n] = num

        return ans

