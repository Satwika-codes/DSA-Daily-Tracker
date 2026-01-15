# PROBLEM NUMBER: 140
# https://leetcode.com/problems/word-break/
# 140.Word Break II
# DIFFICULTY: HARD
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # APPROACH:
        # 1. Use DFS with memoization to generate all valid sentences.
        # 2. At each position in the string, try every word in the dictionary
        #    that matches the current prefix.
        # 3. Recursively solve the remaining substring and combine results.
        # 4. Memoize results for each starting index to avoid recomputation.
        # 5. Return all possible sentences formed using dictionary words.

        # Time Complexity:
        # - Exponential in worst case, but optimized with memoization

        # Space Complexity:
        # - O(n) for recursion stack and memo storage
        
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]

            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    for sub in dfs(end):
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)
            memo[start] = res
            return res

        return dfs(0)
