# PROBLEM NUMBER:-532
# https://leetcode.com/problems/k-diff-pairs-in-an-array/
# K-Diff Pairs in an Array
# DIFFICULTY:-EASY
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # APPROACH:
        # 1. If k is negative, no valid pairs exist, so return 0.
        # 2. Count the frequency of each number using a hash map.
        # 3. If k == 0, count how many numbers appear more than once,
        #    since pairs must have the same value.
        # 4. If k > 0, for each unique number x, check whether x + k
        #    exists in the map.
        # 5. Count each valid pair only once.

        # Time Complexity:
        # - O(n)

        # Space Complexity:
        # - O(n)
        
        if k < 0:
            return 0

        from collections import Counter
        cnt = Counter(nums)

        res = 0
        if k == 0:
            for v in cnt.values():
                if v > 1:
                    res += 1
        else:
            for x in cnt:
                if x + k in cnt:
                    res += 1

        return res
