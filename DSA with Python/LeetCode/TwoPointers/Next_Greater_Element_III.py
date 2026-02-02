# PROBLEM NUMBER: 556
# https://leetcode.com/problems/next-greater-element-iii/
# 556. Next Greater Element III
# DIFFICULTY: MEDIUM
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach:
        # - Convert the number to a list of digits.
        # - Find the first index `i` from the right such that digits[i] < digits[i+1].
        #   If no such index exists, no greater permutation is possible.
        # - Find the smallest digit on the right of `i` that is greater than digits[i]
        #   and swap them.
        # - Reverse the subarray to the right of index `i` to get the smallest
        #   greater permutation.
        # - Convert back to integer and ensure it fits in 32-bit signed integer range.

        # Time Complexity: O(d)
        # Space Complexity: O(d)
        # where d is the number of digits in n.
        

        digits = list(str(n))
        i = len(digits) - 2

        # Step 1: find first decreasing digit from right
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        if i < 0:
            return -1

        # Step 2: find next larger digit to swap
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1

        digits[i], digits[j] = digits[j], digits[i]

        # Step 3: reverse the suffix
        digits[i + 1:] = reversed(digits[i + 1:])

        res = int("".join(digits))

        return res if res < 2**31 else -1
