class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # okay looking for two nums that add to target
        # answer is guaranteed, just need to return indicies
        # return smaller index first. 

        # loop through
        # maintain a hashmap that contains (k,v) --> (num to find, index)
        # We can calculate num to find by subtracing current num from target

        mapping = {}

        for i, num in enumerate(nums):
            if num in mapping:
                return [mapping[num], i]
            else:
                mapping[target - num] = i