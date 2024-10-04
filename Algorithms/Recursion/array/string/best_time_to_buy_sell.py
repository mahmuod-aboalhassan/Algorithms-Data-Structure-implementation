
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right,left=1,0
        max_sell=0
        
        if len(prices)==2:
            if (prices[1] - prices[0])<=0:
                return 0
            else: return prices[1]-prices[0]
        while right<=len(prices)-1:
            if prices[right]<prices[left]:
                left=right
            print(left,right)
            max_sell=max(max_sell,prices[right]-prices[left])
            right+=1
        return max_sell
    
    
solution=Solution()
solution.maxProfit([1,2,4])