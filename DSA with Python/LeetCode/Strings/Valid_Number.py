# PROBLEM NUMBER: 65
# https://leetcode.com/problems/valid-number/
# 65. Valid Number
# DIFFICULTY: HARD
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # APPROACH:
        # This solution checks if a given string `s` represents a valid number 
        # by parsing it character by character while keeping track of digits, 
        # decimal points, and exponents.
        # 1. Strip leading and trailing spaces using `strip()`.
        # 2. Initialize three flags:
        #    - `num`: Tracks if at least one digit has been seen.
        #    - `dot`: Tracks if a decimal point has been encountered.
        #    - `exp`: Tracks if an exponent ('e' or 'E') has been encountered.
        # 3. Iterate through each character:
        #    - If it's a digit, mark `num = True`.
        #    - If it's '+' or '-', it must appear only at the start or right after an exponent.
        #    - If it's '.', ensure no previous '.' or 'e' appeared.
        #    - If it's 'e' or 'E', ensure it appears only once and after at least one digit.
        #    - If any invalid character appears, return False.
        # 4. At the end, return `num`, ensuring at least one digit was present after parsing.
        # Time Complexity: O(n) — single pass over the string.
        # Space Complexity: O(1) — only constant extra space used.
        s = s.strip()
        num, dot, exp = False, False, False
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = True
            elif ch in ['+', '-']:
                if i > 0 and s[i-1].lower() != 'e':
                    return False
            elif ch == '.':
                if dot or exp:
                    return False
                dot = True
            elif ch.lower() == 'e':
                if exp or not num:
                    return False
                exp = True
                num = False
            else:
                return False
        return num