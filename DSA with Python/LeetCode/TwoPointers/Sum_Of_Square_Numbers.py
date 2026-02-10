# PROBLEM NUMBER: 633
# https://leetcode.com/problems/sum-of-square-numbers/
# 633. Sum of Square Numbers
# DIFFICULTY: MEDIUM
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        
        # Approach:
        # We need to check if there exist two non-negative integers `a` and `b`
        # such that:

        #     a² + b² = c

        # Steps:
        # 1. Use two pointers:
        #    - `left` starts from 0
        #    - `right` starts from ⌊sqrt(c)⌋

        # 2. Compute the sum:
        #    - If left² + right² == c → return True
        #    - If sum < c → increase `left` (to increase sum)
        #    - If sum > c → decrease `right` (to decrease sum)

        # 3. Continue until `left` > `right`.

        # If no valid pair is found, return False.

        # Time Complexity:
        # O(√c)

        # Space Complexity:
        # O(1)

        # :type c: int
        # :rtype: bool
        

        left = 0
        right = int(c ** 0.5)

        while left <= right:
            curr_sum = left * left + right * right

            if curr_sum == c:
                return True
            elif curr_sum < c:
                left += 1
            else:
                right -= 1

        return False
