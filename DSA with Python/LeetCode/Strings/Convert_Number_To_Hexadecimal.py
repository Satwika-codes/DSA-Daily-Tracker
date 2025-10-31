# PROBLEM NUMBER: 405
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/
# 405. Convert a Number to Hexadecimal
# DIFFICULTY: EASY
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Approach:
        # Convert a given integer into its hexadecimal (base-16) representation.
        # Idea:
        # 1. Handle special cases:
        #       - If `num` is 0 → return "0".
        #       - If `num` is negative → convert it to its 32-bit unsigned equivalent 
        #         by adding 2^32 (as per two’s complement representation).
        # 2. Define a lookup string `hex_chars = "0123456789abcdef"` 
        #    that maps each remainder (0–15) to its hex digit.
        # 3. Build the hexadecimal string:
        #       - Repeatedly divide `num` by 16.
        #       - Use `num % 16` to find the current hex digit.
        #       - Prepend the corresponding character to the result.
        # 4. Continue until `num` becomes 0.
        # 5. Return the constructed hexadecimal string.
        if num == 0:
            return "0"
        if num < 0:
            num += 2 ** 32
        
        hex_chars = "0123456789abcdef"
        res = ""
        
        while num > 0:
            res = hex_chars[num % 16] + res
            num //= 16
        
        return res