# PROBLEM NUMBER: 474
# https://leetcode.com/problems/ones-and-zeroes/
# 474. Ones and Zeroes
# DIFFICULTY: MEDIUM
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # Approach:
        # Steps:
        # 1. Preprocess all strings in `strs`:
        #       - For each string, count its number of 0’s and 1’s.
        #       - Store these counts in a list `counts`.
        # 2. Use a recursive DFS function `dfs(i, m_left, n_left)`:
        #       - `i` = current index in `strs`.
        #       - `m_left`, `n_left` = remaining 0’s and 1’s that can be used.
        # 3. For each string:
        #       - Option 1: **Skip it** → move to next string.
        #       - Option 2: **Take it** (if possible) → use up its 0’s and 1’s.
        #       - Return the maximum of these two options.
        # 4. Use **memoization** (`memo` dictionary) to cache intermediate results 
        #    and avoid recalculating overlapping subproblems.
        counts = []
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            counts.append((zeros, ones))
        
        memo = {}
        
        def dfs(i, m_left, n_left):
            if i == len(strs):
                return 0
            if (i, m_left, n_left) in memo:
                return memo[(i, m_left, n_left)]
            
            zeros, ones = counts[i]
            not_take = dfs(i + 1, m_left, n_left)
            take = 0
            if zeros <= m_left and ones <= n_left:
                take = 1 + dfs(i + 1, m_left - zeros, n_left - ones)
            
            memo[(i, m_left, n_left)] = max(take, not_take)
            return memo[(i, m_left, n_left)]
        
        return dfs(0, m, n)