class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # We need a way to count the frequency of each number
        # Then return the actual number itself
        # We can store it in an array
        # We can use the index of the array to indicate the frequency
        # Then at that index store that number
        # so if an element occurs 3 times, we add that number to index 3
        # Then we work from the back of the list, and return k elements

        # We do a single pass (n) and use n space

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq = [ [] for i in range(len(nums) + 1) ]

        for num, count in count.items():
            freq[count].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res        