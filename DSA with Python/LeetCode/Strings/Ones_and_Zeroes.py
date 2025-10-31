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
        # The task is to find the most common (non-banned) word in a paragraph.
        # 1. Convert the entire paragraph to lowercase for case-insensitive comparison.
        # 2. Parse each character:
        #       - Build words from alphabetic characters.
        #       - When encountering a non-alphabetic character, finalize the current word.
        # 3. Add all parsed words into a list `words`.
        # 4. Create a `set` from the banned words for O(1) lookup.
        # 5. Count frequencies of all non-banned words using a dictionary `freq`.
        # 6. Track the word with the highest frequency.
        # 7. Return the most frequent non-banned word.
        # Complexity:
        #   - Time: O(n * k) — where n = number of strings, k = average string length.
        #   - Space: O(n * k) — for storing frequency keys and grouped anagrams.
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