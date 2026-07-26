class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

      # Since we need to use 0(1) space that means we can't use a hashmap
      # We need to use pointers
      # Start left and right, 
      # Brute force would be the check every num and compare with every other num

      # Can we just increment left pointer if too small and decrement right if too big?
      left, right = 0 , len(numbers) - 1

      while left < right:
        sum = numbers[left] + numbers[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return [left + 1, right + 1]