'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
#sol1: simple (6096 ms	15.2 MB)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for ind in range(len(prices)-1):
            maxx = max(prices[ind+1:])
            profit = max(profit, maxx-prices[ind])
        return profit

#sol2: based on dp -> Top down (72 ms 45.3 MB)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = list(0 for _ in range(len(prices)))
        profit = 0
        def solution(ind):
            nonlocal profit
            if ind == len(prices)-1:
                maxx[ind] = prices[ind]
                return prices[ind]
            maxx[ind] = max(prices[ind], solution(ind+1))
            profit = max(profit, maxx[ind]-prices[ind])
            return maxx[ind]
        if maxx:
            solution(0)
        return profit

#sol3: based on dp -> Bottom up (68 ms	15 MB) -> memory efficiency
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = list(0 for _ in range(len(prices)))
        profit = 0
        if prices:
            maxx[-1] = prices[-1]
            for i in range(len(maxx)-2,-1,-1):
                maxx[i] = max(prices[i], maxx[i+1])
                profit = max(profit, maxx[i]-prices[i])
        return profit

#sol4: not using list (64 ms 15 MB)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx, minn = 0, 987654321
        for price in prices:
            minn = min(minn, price)
            maxx = max(maxx, price-minn)
        return maxx