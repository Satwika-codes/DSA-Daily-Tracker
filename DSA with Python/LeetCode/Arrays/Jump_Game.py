# PROBLEM NUMBER: 55
# https://leetcode.com/problems/jump-game/
# 55.Jump Game
# DIFFICULTY: MEDIUM
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Approach:
        # 1. Maintain a variable 'reach' to track the farthest index we can jump to.
        # 2. Iterate through each index 'i':
        #       - If 'i' is greater than 'reach', it means we cannot reach this index → return False.
        # 3. Update 'reach' = max(reach, i + nums[i]) to extend our maximum jump distance.
        # 4. If the loop completes without failure, all indices were reachable.
        # 5. Return True because we can reach the last index.
        reach = 0
        for i, x in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + x)
        return True