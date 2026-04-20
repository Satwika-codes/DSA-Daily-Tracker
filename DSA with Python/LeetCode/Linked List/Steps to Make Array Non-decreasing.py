# PROBLEM NUMBER: 1964
# https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-strictly-increasing/
# 1964. Minimum Number of Operations to Make Arrays Strictly Increasing
# DIFFFICULTY: MEDIUM

class Solution(object):
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach:
        # We need to count how many rounds are required to remove elements
        # such that any element nums[i] < nums[i-1] gets removed.
        #
        # Key Idea:
        # Instead of simulating deletions step-by-step,
        # we track how many steps each element survives.
        #
        # Step 1: Use a stack:
        #         • Each element = (value, steps to be removed)
        #
        # Step 2: Traverse the array:
        #
        # Step 3: For each number:
        #         • Initialize steps = 0
        #
        # Step 4: While stack is not empty AND current number >= top value:
        #         • Pop elements (they won't affect current)
        #         • Update steps = max(steps, popped element steps)
        #
        # Step 5: If stack is still not empty:
        #         • Current element will be removed later
        #         • steps += 1
        #         • (because a bigger element exists on left)
        #
        # Step 6: Else:
        #         • No greater element on left → it stays forever
        #         • steps = 0
        #
        # Step 7: Track maximum steps across all elements
        #
        # Step 8: Push (num, steps) into stack
        #
        # Step 9: Return max steps

        stack = []  # (value, steps)
        res = 0

        for num in nums:
            steps = 0

            # remove elements <= current
            while stack and num >= stack[-1][0]:
                steps = max(steps, stack.pop()[1])

            if stack:
                steps += 1
            else:
                steps = 0

            res = max(res, steps)
            stack.append((num, steps))

        return res


