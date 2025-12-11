# PROBLEM NUMBER: 494
# https://leetcode.com/problems/target-sum/
# Target Sum
# DIFFICULTY: MEDIUM
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Approach (DP Using HashMap for Sum Frequencies):
        #
        # Goal:
        # Each number can be assigned + or -. Count how many ways the final sum becomes target.
        #
        # Idea:
        # Use a dictionary dp where:
        #       key   = possible sum after processing some elements
        #       value = number of ways to reach that sum
        #
        # Steps:
        # 1. Initialize dp = {0: 1} → one way to have sum 0 before using any numbers.
        #
        # 2. For each number `num` in nums:
        #       • Create a new dictionary new_dp.
        #       • For each sum `s` currently in dp:
        #             - Add contribution to (s + num)
        #             - Add contribution to (s - num)
        #         (We update counts in new_dp to avoid overwriting dp mid-loop.)
        #
        # 3. Replace dp with new_dp for next iteration.
        #
        # 4. At the end, dp[target] = total ways to form target sum.
        #
        # Time Complexity: O(n * total_possible_sums)  
        #                  In worst case → O(n * 2000) ≈ acceptable.
        # Space Complexity: O(total_possible_sums)

        dp = {0: 1}

        for num in nums:
            new_dp = {}
            for s in dp:
                new_dp[s + num] = new_dp.get(s + num, 0) + dp[s]
                new_dp[s - num] = new_dp.get(s - num, 0) + dp[s]
            dp = new_dp

        return dp.get(target, 0)
