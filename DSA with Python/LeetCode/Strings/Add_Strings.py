# PROBLEM NUMBER: 415
# https://leetcode.com/problems/add-strings/
# 415. Add Strings
# DIFFICULTY: EASY
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Approach:
        # This solution adds two non-negative integers represented as strings without converting them to integers directly.
        # 1. Initialize pointers `i` and `j` to the last indices of `num1` and `num2`.
        # 2. Initialize a `carry` variable to 0 and an empty list `result` to store the digits of the sum.
        # 3. Loop while there are digits left in either string or a non-zero carry:
        #    - Convert current characters to integers using `ord(char) - ord('0')`, or 0 if pointer is out of bounds.
        #    - Compute the sum: `total = n1 + n2 + carry`.
        #    - Update `carry = total // 10` and append `total % 10` to the result list.
        #    - Move pointers `i` and `j` one step left.
        # 4. Reverse the result list and join it to form the final sum string.
        # Time Complexity: O(max(m, n)) — iterates over the longer string.
        # Space Complexity: O(max(m, n)) — stores the resulting digits.
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = n1 + n2 + carry
            carry = total // 10
            result.append(str(total % 10))

            i -= 1
            j -= 1

        return ''.join(result[::-1])
        