# PROBLEM NUMBER: 67
# https://leetcode.com/problems/add-binary/
# 67.Add Binary
# Difficulty: Easy
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # APPROACH:
        # This solution performs binary addition of two binary strings `a` and `b`.
        # 1. Initialize two pointers `i` and `j` to the end of both strings, and a variable `carry` to 0.
        # 2. Use a list `result` to store the binary digits of the sum (in reverse order).
        # 3. Loop while there are remaining digits in either string or a carry value:
        #    - Start with `total = carry`.
        #    - If `i` or `j` are valid indices, add the corresponding binary digits to `total` and decrement the pointers.
        #    - Append `total % 2` (the current binary bit) to `result`.
        #    - Update `carry = total // 2` (to handle overflow to the next bit).
        # 4. After processing all bits, reverse the `result` list and join it into a string for the final binary sum.
        # This approach simulates manual binary addition efficiently in O(max(len(a), len(b))) time and O(1) extra space (excluding output storage).

        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2

        return ''.join(reversed(result))