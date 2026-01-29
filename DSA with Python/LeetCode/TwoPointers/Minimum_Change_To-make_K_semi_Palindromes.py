# PROBLEM NUMBER: 2911
# https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/
# 2911. Minimum Changes To Make K Semi-Palindromes
# DIFFICULTY: HARD
class Solution(object):
    def minimumChanges(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Approach:
        # - The problem is solved using Dynamic Programming with precomputation.
        # - First, precompute a cost matrix where cost[i][j] represents the minimum
        #   number of changes required to make the substring s[i..j] a semi-palindrome.
        # - A substring is checked by trying all possible valid divisors of its length
        #   and counting mismatches in symmetric positions with step size equal to the divisor.
        # - Next, use DP where dp[p][i] denotes the minimum changes needed to split
        #   the first i characters into p valid semi-palindromic substrings.
        # - Transition is done by trying all possible previous split points and
        #   adding the precomputed cost.
        # - The final answer is dp[k][n].
        
        
        n = len(s)
        INF = 10**9
        
        cost = [[0]*n for _ in range(n)]
        
        for i in range(n):
            for j in range(i+1, n):
                length = j - i + 1
                best = INF
                
                for d in range(1, length):
                    if length % d != 0:
                        continue
                    changes = 0
                    for start in range(d):
                        l = i + start
                        r = j - (d - start) + 1
                        while l < r:
                            if s[l] != s[r]:
                                changes += 1
                            l += d
                            r -= d
                    best = min(best, changes)
                
                cost[i][j] = best
        
        dp = [[INF]*(n+1) for _ in range(k+1)]
        dp[0][0] = 0
        
        for p in range(1, k+1):
            for i in range(p*2, n+1):
                for j in range((p-1)*2, i-1):
                    dp[p][i] = min(dp[p][i], dp[p-1][j] + cost[j][i-1])
        
        return dp[k][n]
