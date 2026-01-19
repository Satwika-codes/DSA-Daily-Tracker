# PROBLEM NUMBER:-954
# https://leetcode.com/problems/array-of-doubled-pairs/
# 954. Array of Doubled Pairs
# DIFFICULTY:-MEDIUM
class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # APPROACH:
        # 1. Count the frequency of each number in the array.
        # 2. Sort the unique numbers by their absolute values so smaller
        #    magnitudes are processed first.
        # 3. For each number x:
        #    - If its count is zero, continue.
        #    - Ensure there are at least count[x] occurrences of 2*x.
        #    - Reduce the count of 2*x accordingly.
        # 4. If all numbers can be paired successfully, return True.

        # Time Complexity:
        # - O(n log n)

        # Space Complexity:
        # - O(n)
        
        from collections import Counter

        count = Counter(arr)

        for x in sorted(count.keys(), key=abs):
            if count[x] == 0:
                continue
            if count[2 * x] < count[x]:
                return False
            count[2 * x] -= count[x]

        return True
