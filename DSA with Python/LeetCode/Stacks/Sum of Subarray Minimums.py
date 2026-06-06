# PROBLEM NUMBER: 907
# https://leetcode.com/problems/sum-of-subarray-minimums/
# 907. Sum of Subarray Minimums
# DIFFICULTY: MEDIUM

class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        # Approach:
        # Instead of generating all subarrays,
        # we calculate how many subarrays use
        # each element as their minimum.
        #
        # For every element, find:
        # • How many consecutive elements on
        #   the left are greater than it.
        # • How many consecutive elements on
        #   the right are greater than or
        #   equal to it.
        #
        # Using Monotonic Stacks, we compute
        # these counts efficiently.
        #
        # Then each element contributes:
        #
        # arr[i] * left[i] * right[i]
        #
        # Summing all contributions gives
        # the final answer.

        MOD = 10**9 + 7

        n = len(arr)

        left = [0] * n
        right = [0] * n

        stack = []

        # Previous Less Element
        for i in range(n):

            count = 1

            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]

            left[i] = count

            stack.append((arr[i], count))

        stack = []

        # Next Less or Equal Element
        for i in range(n - 1, -1, -1):

            count = 1

            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]

            right[i] = count

            stack.append((arr[i], count))

        ans = 0

        for i in range(n):

            ans += arr[i] * left[i] * right[i]

            ans %= MOD

        return ans