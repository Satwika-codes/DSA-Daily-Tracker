# PROBLEM NUMBER: 13
# https://leetcode.com/problems/roman-to-integer/
# 13. Roman to Integer
# DIFFICULTY: EASY
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # APPROACH:
        # This solution converts a Roman numeral string into its integer equivalent using a simple comparison-based approach.
        # 1. Create a dictionary `roman` that maps each Roman numeral character to its corresponding integer value.
        # 2. Initialize `total = 0` to store the final result.
        # 3. Traverse each character in the string `s`:
        #    - If the current numeral is smaller than the next one (e.g., 'I' before 'V' or 'X'), 
        #      subtract its value from `total` (to handle cases like IV = 4 or IX = 9).
        #    - Otherwise, add its value to `total`.
        # 4. After the loop, return `total`, which now contains the integer representation of the Roman numeral.
        # This approach correctly handles both standard and subtractive notations in Roman numerals.
        # Time Complexity: O(n) — each character is processed once.
        # Space Complexity: O(1) — uses only a fixed-size dictionary for Roman numeral mappings
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total
        