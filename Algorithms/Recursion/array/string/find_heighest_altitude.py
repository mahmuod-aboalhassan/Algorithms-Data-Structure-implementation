class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum=[0 for i in range(len(gain))]
        for i in range(len(gain)):
            # print(i,'idx')
            prefix_sum[i]=prefix_sum[i-1] + gain[i]
        # print(prefix_sum)
        return max(prefix_sum) if max(prefix_sum)>0 else 0
        