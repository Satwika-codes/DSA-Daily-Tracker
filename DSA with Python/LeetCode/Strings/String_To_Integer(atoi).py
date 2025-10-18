# PROBLEM NUMBER: 8 
# https://leetcode.com/problems/string-to-integer-atoi/
# 8.String to Integer(atoi)
# DIFFICULTY: MEDIUM
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # APPROACH:
        # This solution converts a string into a 32-bit signed integer (similar to the C/C++ atoi function).
        # 1. Remove any leading whitespace characters using `lstrip()`.
        # 2. Check if the string is empty after trimming; if yes, return 0.
        # 3. Determine the sign:
        #    - If the first character is '-' → mark sign as -1.
        #    - If it is '+' → keep sign as +1.
        #    - Otherwise, assume the number is positive.
        # 4. Traverse the remaining characters and construct the integer using only digits.
        #    - Stop as soon as a non-digit character is found.
        # 5. Multiply the number by the sign.
        # 6. Clamp the final result within the 32-bit integer range:
        #    - Minimum: -2³¹
        #    - Maximum: 2³¹ - 1
        # 7. Return the final integer value.
        # Time Complexity: O(n) — single pass through the string.
        # Space Complexity: O(1) — constant extra space used.
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        i = 0
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            i += 1
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        num *= sign
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num