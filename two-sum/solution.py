# Tueely LeetCode Solutions, source: https://github.com/criszhou/LeetCode-Python
# Problem: Two Sum
# Solution Type: Optimal Hash Map Approach
# Tags: Array, Hash Map, Linear Time

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Key Component: Hash Map for O(1) lookups
        numToIndex = dict()  # Maps numbers to their indices in the input array
        
        # Core Logic: Single-pass iteration with complement check
        for i, num in enumerate(nums):
            # Optimization: Check for complement before adding to map
            complement = target - num
            if complement in numToIndex:
                # Early Exit: Return indices immediately when found
                return [numToIndex[complement], i]
            # State Update: Track current number's index after check
            numToIndex[num] = i
        
        # Constraint Enforcement: Problem guarantees a solution
        assert False, "Input must contain exactly one valid solution"
