# PROBLEM NUMBER:-2206
# https://leetcode.com/problems/divide-array-into-equal-pairs/
# Divide Array into Equal Pairs
# DIFFICULTY: EASY
class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # APPROACH:
        # The array can be divided into pairs of equal elements if and only if
        # every number appears an even number of times.

        # Steps:
        # 1) Count the frequency of each number in the array.
        # 2) Check each frequency:
        #    - If any number appears an odd number of times, pairing is impossible.
        # 3) If all frequencies are even, the array can be divided into pairs.

        # Key Insight:
        # - Each pair needs exactly two identical elements.
        # - Odd frequency means one element will always be left unpaired.

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        

        from collections import Counter

        freq = Counter(nums)

        for count in freq.values():
            if count % 2 != 0:
                return False

        return True
