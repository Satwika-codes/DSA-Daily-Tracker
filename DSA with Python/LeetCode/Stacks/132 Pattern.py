# PROBLEM NUMBER: 456
# https://leetcode.com/problems/132-pattern/
# 456. 132 Pattern
# DIFFICULTY: MEDIUM

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Approach:
        # We traverse the array from right
        # to left while maintaining a
        # monotonic decreasing stack.
        #
        # The stack stores possible values
        # for the '3' in a 132 pattern.
        #
        # A variable 'third' keeps track of
        # the best candidate for the '2'
        # element of the pattern.
        #
        # Whenever the current number is
        # greater than the stack top, we
        # pop elements and update 'third'.
        #
        # If we later find a number smaller
        # than 'third', then we have found
        # a valid 132 pattern and return True.

        stack = []
        third = float('-inf')

        for i in range(len(nums) - 1, -1, -1):

            if nums[i] < third:
                return True

            while stack and nums[i] > stack[-1]:
                third = stack.pop()

            stack.append(nums[i])

        return False