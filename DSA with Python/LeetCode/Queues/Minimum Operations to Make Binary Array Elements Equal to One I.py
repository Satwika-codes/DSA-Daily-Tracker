# PROBLEM NUMBER: 3191
# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/
# 3191. Minimum Operations to Make Binary Array Elements Equal to One I
# DIFFICULTY: MEDIUM

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Approach:
        # We process the array from
        # left to right.
        #
        # Whenever we encounter a 0 at
        # index i, the only way to make
        # it become 1 is to perform an
        # operation starting at i.
        #
        # The operation flips the values
        # at indices i, i + 1, and i + 2.
        #
        # Therefore:
        # • If nums[i] is 0, perform the
        #   operation immediately.
        # • Count the operation and
        #   continue scanning.
        #
        # After processing all possible
        # starting positions, check if
        # every element is 1.
        #
        # If yes, return the number of
        # operations performed.
        #
        # Otherwise, it is impossible to
        # convert the entire array into
        # all 1s, so return -1.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        n = len(nums)
        ans = 0

        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ans += 1

        if all(x == 1 for x in nums):
            return ans

        return -1