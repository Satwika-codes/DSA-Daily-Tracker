# PROBLEM NUMBER: 220
# https://leetcode.com/problems/single-number-iii/
# 220. Contains Duplicate III
# DIFFICULTY: MEDIUM
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # APPROACH
        # Step 1: XOR all numbers in the array.
        #         - Since duplicates cancel out, the result will be XOR of the two unique numbers.
        # Step 2: Find the rightmost set bit in the XOR result.
        #         - This bit differs between the two unique numbers.
        # Step 3: Divide numbers into two groups based on this differing bit.
        #         - One group has this bit set, the other does not.
        # Step 4: XOR numbers within each group.
        #         - All duplicate numbers cancel out.
        #         - Each group results in one unique number.
        # Step 5: Return the two unique numbers.

        xor = 0
        for num in nums:
            xor ^= num

        diff = xor & -xor
        a = 0
        b = 0

        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num

        return [a, b]
