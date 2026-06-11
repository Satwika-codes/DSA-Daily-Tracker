# PROBLEM NUMBER: 2944
# https://leetcode.com/problems/minimum-number-of-coins-for-fruits/
# 2944. Minimum Number of Coins for Fruits
# DIFFICULTY: MEDIUM

class Solution(object):
    def minimumCoins(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Approach:
        # We use dynamic programming
        # starting from the last fruit
        # and move backwards.
        #
        # Let dp[i] represent the minimum
        # number of coins needed to obtain
        # all fruits starting from index i.
        #
        # When we buy the fruit at index i,
        # we pay prices[i] and can obtain
        # the next i + 1 fruits for free.
        #
        # Therefore, after buying fruit i,
        # the next fruit that may require
        # payment can lie in the range
        # [i + 1, 2 * i + 2].
        #
        # If buying fruit i already covers
        # all remaining fruits, then the
        # cost is simply prices[i].
        #
        # Otherwise, choose the minimum
        # cost among all valid next states
        # and add it to prices[i].
        #
        # Compute dp values from right to
        # left so that all future states
        # are already available when needed.
        #
        # The answer is stored in dp[0].
        #
        # Time Complexity: O(n²)
        # Space Complexity: O(n)

        n = len(prices)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):

            if 2 * i + 2 >= n:
                dp[i] = prices[i]
            else:
                dp[i] = prices[i] + min(
                    dp[j]
                    for j in range(i + 1, min(n, 2 * i + 3))
                )

        return dp[0]