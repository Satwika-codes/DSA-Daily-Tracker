# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-string-to-binary-array/
# PROBLEM NUMBER: 3750
# 3750. Minimum Number of Flips to Convert Binary String to Binary Array
# DIFFICULTY: EASY
class Solution(object):
    def minimumFlips(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach:
        # Step 1: The goal is to determine how many bit positions differ between a binary number and its reversed version.
        # Step 2: First convert the integer `n` into its binary representation using `bin(n)` and remove the `0b` prefix to keep only the binary digits.
        # Step 3: Create another string `r` which is the reversed version of the binary string.
        # Step 4: Initialize a counter `flips` to track how many positions have different bits.
        # Step 5: Traverse through the binary string using a loop and compare each bit of the original string `s` with the corresponding bit in the reversed string `r`.
        # Step 6: If the bits at the same position are different, increment the `flips` counter because that position would require a flip to match.
        # Step 7: Continue checking all positions in the string.
        # Step 8: After finishing the traversal, return the total number of differing positions stored in `flips`.

        s = bin(n)[2:]
        r = s[::-1]

        flips = 0

        for i in range(len(s)):
            if s[i] != r[i]:
                flips += 1

        return flips