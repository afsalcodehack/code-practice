from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 1
        max_profit = 0
        while s < len(prices):
            if prices[s] > prices[b]:
                curr_profit = prices[s] - prices[b]
                max_profit = max(curr_profit , max_profit)
            else:
                b = s
            s += 1
        return max_profit


driver = Solution()
print(driver.maxProfit([7,1,5,3,6,4]))
print(driver.maxProfit([7,6,4,3,1]))
print(driver.maxProfit([1,2]))