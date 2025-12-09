# PROBLEM NUMBER: 476
# https://leetcode.com/problems/number-complement/
# 476. Number Complement
# DIFFICULTY: EASY
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Approach:
        # Step 1: Find the number of bits in the binary representation of num.
        # Step 2: Create a mask where all bits are set to 1 for the length of num's binary.
        #         This can be done by shifting 1 left by the number of bits and subtracting 1.
        # Step 3: XOR num with the mask to flip all bits (0 -> 1, 1 -> 0).
        # Step 4: Return the result of the XOR operation which is the complement.

        # Step 1 & 2: Create mask with all bits as 1 of the same length as num's binary
        mask = (1 << num.bit_length()) - 1
        
        # Step 3: XOR num with mask to get complement
        return num ^ mask
