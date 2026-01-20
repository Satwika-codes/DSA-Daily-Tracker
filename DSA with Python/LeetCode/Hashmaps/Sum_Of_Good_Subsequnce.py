# PROBLEM NUMBER: 3351
# https://leetcode.com/problems/sum-of-good-subsequences/
# 3351.Sum Of Good Subsequnce
# DIFFICULTY: HARD
class Solution(object):
    def sumOfGoodSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach:
        # We use dynamic programming with hash maps.
        # For each number x, maintain:
        # - cnt[x]: number of good subsequences ending at x
        # - total[x]: sum of elements of all good subsequences ending at x
        # For each occurrence of x:
        # 1) Start a new subsequence with x alone.
        # 2) Extend subsequences ending at x-1 and x+1 by appending x.
        # Transitions:
        # new_cnt = 1 + cnt[x-1] + cnt[x+1]
        # new_sum = x + (total[x-1] + cnt[x-1] * x) + (total[x+1] + cnt[x+1] * x)
        # Accumulate results into cnt[x] and total[x].
        # Finally, sum total[x] over all x to get the answer.
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        MOD = 10**9 + 7
        
        cnt = {}
        total = {}
        
        for x in nums:
            c1 = cnt.get(x - 1, 0)
            c2 = cnt.get(x + 1, 0)
            s1 = total.get(x - 1, 0)
            s2 = total.get(x + 1, 0)
            
            new_cnt = (1 + c1 + c2) % MOD
            new_sum = (x + s1 + c1 * x + s2 + c2 * x) % MOD
            
            cnt[x] = (cnt.get(x, 0) + new_cnt) % MOD
            total[x] = (total.get(x, 0) + new_sum) % MOD
        
        return sum(total.values()) % MOD
