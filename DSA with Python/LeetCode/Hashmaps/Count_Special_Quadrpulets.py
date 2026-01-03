# PROBLEM NUMBER: 1995
# https://leetcode.com/problems/count-special-quadruplets/
# 1995.Count Special Quadruplets
# DIFFICULTY:EASY
class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        # Approach:
        # We directly check all possible quadruplets (a, b, c, d) such that
        # a < b < c < d and verify whether:
        # nums[a] + nums[b] + nums[c] == nums[d].

        # Since the array size is at most 50, an O(n^4) brute-force
        # solution is efficient enough and avoids all overcounting issues.
        

        n = len(nums)
        count = 0

        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c + 1, n):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            count += 1

        return count
