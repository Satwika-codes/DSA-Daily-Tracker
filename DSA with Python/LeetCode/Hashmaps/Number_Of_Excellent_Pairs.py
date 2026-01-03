# PROBLEM NUMBER:1515
# https://leetcode.com/problems/count-excellent-pairs/
# 1515.Count Excellent Pairs
# DIFFICULTY:EASY
class Solution(object):
    def countExcellentPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """       
        # Approach:
        # An excellent pair (x, y) satisfies:
        # popcount(x) + popcount(y) >= k.

        # Since order matters, (x, y) and (y, x) are counted separately.

        # Steps:
        # 1. Remove duplicates from nums because duplicates do not affect
        #    the popcount values but would cause repeated counting.
        # 2. Compute the number of set bits (popcount) for each unique number.
        # 3. Count how many numbers have each popcount.
        # 4. For every pair of popcounts (i, j), if i + j >= k,
        #    add count[i] * count[j] to the answer.

        # Maximum popcount for constraints is small (≤ 30),
        # so this approach is efficient.
        

        from collections import Counter

        nums = set(nums)
        bit_counts = Counter(bin(x).count("1") for x in nums)

        result = 0
        for i in bit_counts:
            for j in bit_counts:
                if i + j >= k:
                    result += bit_counts[i] * bit_counts[j]

        return result
