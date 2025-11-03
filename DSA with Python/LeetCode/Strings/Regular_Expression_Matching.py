# PROBLEM NUMBER: 10
# https://leetcode.com/problems/regular-expression-matching/
# 10. Regular Expression Matching
# DIFFICULTY: HARD
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Approach:
        # 1. The goal is to check if the string `s` matches the pattern `p`,
        #    where:
        #       - '*' matches zero or more of the preceding element.
        # 2. Use recursion with memoization (`dfs(i, j)`) to explore all possibilities:
        #       - `i` → current index in string `s`
        #       - `j` → current index in pattern `p`
        # 3. Base Case:
        #       - If `j` reaches the end of `p`, return True only if `i`
        #         also reaches the end of `s` (full match).
        # 4. For each recursive step:
        #       - Check if current characters match or if pattern has '.'.
        #       - If the next character in `p` is '*':
        #             → Option 1: Skip the current pattern (dfs(i, j + 2))
        #             → Option 2: Use '*' to match current character (if possible)
        #                        and move forward in `s` (dfs(i + 1, j))
        #       - Otherwise, move both pointers forward if they match.
        # 5. Store results in `memo` to avoid recomputation of overlapping subproblems.
        # Time Complexity: O(m * n)  # m = len(s), n = len(p)
        # Space Complexity: O(m * n) due to recursion and memoization
        memo = {}
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            first = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j + 1 < len(p) and p[j + 1] == '*':
                res = dfs(i, j + 2) or (first and dfs(i + 1, j))
            else:
                res = first and dfs(i + 1, j + 1)
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)