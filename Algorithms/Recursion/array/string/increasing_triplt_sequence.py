
# 334. Increasing Triplet Subsequence
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
from typing import List
import math
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first=math.inf
        second=math.inf
        for n in nums:
            if n<=first:
                first=n
            elif n<=second:
                second=n
            else:
                if first<=second<=n:
                    return True
        return False