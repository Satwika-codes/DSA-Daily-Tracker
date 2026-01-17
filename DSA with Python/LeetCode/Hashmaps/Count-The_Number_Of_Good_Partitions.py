# PROBLEM NUMBER :2963
# Https://leetcode.com/problems/count-the-number-of-good-partitions/4
# 2963. Count the Number of Good Partitions
# DIFFICULTY:HARD
class Solution(object):
    def numberOfGoodPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # """
        # APPROACH:
        # 1. For each distinct number, record its last occurrence index.
        # 2. Traverse the array while maintaining the farthest last index
        #    seen so far for the current segment.
        # 3. Whenever the current index equals this farthest boundary,
        #    a partition can safely end because no number in the segment
        #    appears later.
        # 4. Each valid partition point doubles the number of ways since
        #    we can either cut or continue.
        # 5. Return the total number of ways modulo 10^9 + 7.

        # Time Complexity:
        # - O(n)

        # Space Complexity:
        # - O(n)
        
        MOD = 10**9 + 7

        last = {}
        for i, x in enumerate(nums):
            last[x] = i

        ways = 1
        end = 0

        for i, x in enumerate(nums):
            end = max(end, last[x])
            if i == end and i != len(nums) - 1:
                ways = (ways * 2) % MOD

        return ways
