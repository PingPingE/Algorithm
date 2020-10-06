'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. 

You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
'''
#sol1: not using list (52 ms 14 MB)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost=0
        if cost:
            cost1, cost2 = 0,cost[0]
            for i in range(1,len(cost)):
                mini = min(cost1,cost2)
                cost1 = cost2
                cost2 = mini+cost[i]
            min_cost=min(cost1,cost2)
        return min_cost

#sol2: using list (56 ms 14.3 MB)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        return min(dp[-1], dp[-2])