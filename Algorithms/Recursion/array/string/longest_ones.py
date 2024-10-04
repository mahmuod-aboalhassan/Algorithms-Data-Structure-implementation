from typing import List 
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k=1
        left=0
        longest_ones=0
        for right in range(len(nums)):
            if nums[right]==0:
                k-=1
            while k<1:
                if nums[left]==0:
                    k+=1
                left+=1
            longest_ones=max(longest_ones,right-left+1)
        return longest_ones



solution=Solution()
solution.longestSubarray([1,1,0,1])