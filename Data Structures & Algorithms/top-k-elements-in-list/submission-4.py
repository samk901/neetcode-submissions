class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We want to do bucket sort for efficiency
        # single pass will sort the nums by their frequency
        # We can use the array indicies to denote frequency
        # Then we iterated through the array backwards to skim k elements

        # Create a hashmap to count the frequency
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        # Now create a bucket which we will use to sort the num/freq
        bucket = [ [] for i in range(len(nums) + 1) ]
        for num, freq in freq.items():
            bucket[freq].append(num)
        
        result = []

        # Now iterated backwards from the list grabbing k number of elements
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result