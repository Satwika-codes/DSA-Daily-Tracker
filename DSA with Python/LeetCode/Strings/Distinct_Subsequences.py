# PROBLEM NUMBER: 115
# https://leetcode.com/problems/distinct-subsequences/
# 115. Distinct Subsequences
# DIFFICULTY: HARD
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # Approach:
        # The goal is to find the number of distinct subsequences of string `s`
        # that equal string `t`.
        # Idea:
        # We use **Depth-First Search (DFS)** with **memoization** to explore 
        # all possible ways to match `t` as a subsequence of `s`.
        # Recursion logic:
        #   - `dfs(i, j)` → number of subsequences of `s[i:]` that match `t[j:]`
        #   Cases:
        #   1. If `j == len(t)`: we have matched the entire `t` → return 1
        #   2. If `i == len(s)`: we've exhausted `s` but not matched all of `t` → return 0
        #   3. If `(i, j)` is in `memo`: return the cached result to avoid recomputation
        #   - If characters match (`s[i] == t[j]`):
        #         We can either:
        #           a) Take this match → move both pointers (i+1, j+1)
        #           b) Skip this char in `s` → move only `i` (i+1, j)
        #         So: dfs(i, j) = dfs(i+1, j+1) + dfs(i+1, j)
        #   - If characters don’t match:
        #         We skip the current `s[i]` → dfs(i+1, j)
        # Complexity:
        #   - Time:  O(m * n)   (Each state (i, j) computed once)
        #   - Space: O(m * n)   (Memoization storage + recursion stack)
        memo = {}
        
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            if s[i] == t[j]:
                memo[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                memo[(i, j)] = dfs(i + 1, j)
            return memo[(i, j)]
        
        return dfs(0, 0)
        