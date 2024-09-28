
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return nums
        left,right=0,1
        n=len(nums)
        while left<n:
            if nums[left]==0:
                while right<n:
                    if nums[right]==0:
                        right+=1
                        continue
                    nums[left],nums[right]=nums[right],nums[left]
                    right+=1
                    left+=1
                n=right
            left+=1
            right=left+1
            
        return nums




solution=Solution()
print(solution.moveZeroes([4,2,4,0,0,3,0,5,1,0]))