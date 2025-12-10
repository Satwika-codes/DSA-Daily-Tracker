# PROBLEM NUMBER: 746
# https://leetcode.com/problems/min-cost-climbing-stairs/
# 746. Min Cost Climbing Stairs
# DIFFICULTY: EASY
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        # Approach:
        # Step 1: Use Dynamic Programming where:
        #         dp[i] = minimum cost required to reach step i.
        #         Note: You can reach step i from either step i-1 or step i-2.
        #
        # Step 2: Base initialization:
        #         dp[0] = 0  (starting on ground)
        #         dp[1] = 0  (you can also start from step 1)
        #
        # Step 3: For each step i ≥ 2:
        #         dp[i] = min(
        #             dp[i-1] + cost[i-1],  # Coming from (i-1)
        #             dp[i-2] + cost[i-2]   # Coming from (i-2)
        #         )
        #
        # Step 4: Final answer = dp[n] → minimum cost needed to reach beyond last step.

        n = len(cost)
        dp = [0] * (n + 1)  # dp[i] = min cost to reach step i

        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]