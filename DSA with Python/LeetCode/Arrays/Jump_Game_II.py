# PROBLEM NUMBER: 45
# https://leetcode.com/problems/jump-game-ii/
# 45. Jump Game II
# DIFFICULTY: MEDIUM
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach (Greedy - O(n)):
        # We want to reach the last index using the minimum number of jumps.
        #
        # Key Idea:
        # - Treat the array like "levels" of BFS.
        # - `far`  = the farthest index we can reach while iterating.
        # - `end`  = boundary of the current jump (like finishing a level).
        # - When `i` reaches `end`, it means we must make a jump.
        #
        # Steps:
        # 1. Iterate from index 0 to n-2 (no need to jump after last index).
        # 2. Update `far` continuously as the farthest reachable position.
        # 3. When `i == end`, we must "take the jump":
        #       - Increase jump counter.
        #       - Move `end` to `far` (new boundary).
        # 4. Continue until the loop finishes.
        #
        # This greedy strategy ensures minimum jumps because we always expand
        # to the farthest possible range before jumping.

        jumps = 0
        end = 0
        far = 0

        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            if i == end:
                jumps += 1
                end = far

        return jumps
