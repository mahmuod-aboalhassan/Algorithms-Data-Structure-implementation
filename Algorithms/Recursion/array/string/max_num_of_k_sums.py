from typing import  List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sors_nums=sorted(nums)
        left,right=0,len(nums)-1
        count_of_them=0
        def count(n1,n2):
            return sors_nums[n1]+sors_nums[n2]
        while left<right:
            sum_of_them=count(left,right)
            if sum_of_them==k:
                left+=1
                right-=1
                count_of_them+=1
            elif sum_of_them<k:
                left+=1
            else:
                right-=1
            
        return count_of_them