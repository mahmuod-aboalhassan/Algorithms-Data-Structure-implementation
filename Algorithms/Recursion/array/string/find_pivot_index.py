class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        
        prefix_sum = [0] * len(nums)
        suffix_sum = [0] * len(nums)
        
        # Initialize prefix and suffix sums
        prefix_sum[0] = nums[0]
        suffix_sum[-1] = nums[-1]
        
        # Calculate prefix sums
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        # Calculate suffix sums
        for i in range(len(nums)-2, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + nums[i]
        
        # Check for the pivot index
        for i in range(len(nums)):
            left_sum = 0 if i == 0 else prefix_sum[i-1]
            right_sum = 0 if i == len(nums) - 1 else suffix_sum[i+1]
            
            if left_sum == right_sum:
                return i
        
        return -1