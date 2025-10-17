# PROBLEM NUMBER: 12
# https://leetcode.com/problems/integer-to-roman/
# 12. INTEGER TO ROMAN
# DIFFICULTY: MEDIUM
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # APPROACH:
        # This solution converts an integer to its Roman numeral representation using a greedy subtraction-based approach.
        # 1. Maintain two parallel lists:
        #    - `val`: integer values in descending order.
        #    - `syms`: corresponding Roman numeral symbols.
        # 2. Initialize an empty string `roman` to build the final numeral.
        # 3. Iterate through the `val` list:
        #    - While the current value can be subtracted from `num`, append its corresponding Roman symbol to `roman`
        #      and subtract that value from `num`.
        # 4. Continue this process until `num` becomes zero.
        # 5. Return the constructed Roman numeral string.
        # This greedy approach ensures the largest possible Roman numeral symbols are used first, 
        # producing a valid and minimal Roman representation.
        # Time Complexity: O(1) — the loop runs over a fixed list of Roman numeral mappings.
        # Space Complexity: O(1) — constant extra space is used.
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman = ""
        for i in range(len(val)):
            while num >= val[i]:
                roman += syms[i]
                num -= val[i]
        return roman
        