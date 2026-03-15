# PROBLEM NUMBER: 1048
# https://leetcode.com/problems/longest-string-chain/
# 1048. Longest String Chain
# DIFFICULTY: MEDIUM
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Approach:
        # Step 1: The goal is to find the longest possible chain of words where each word can be formed by inserting exactly one character into the previous word.
        # Step 2: Sort the list of words by their length so that when processing a word, all possible predecessor words (shorter by one character) are already processed.
        # Step 3: Use a dictionary `dp` where dp[word] stores the length of the longest chain ending with that word.
        # Step 4: Initialize each word with a minimum chain length of 1 because every word itself can form a chain of length 1.
        # Step 5: For each word, try removing one character at every possible position to generate a potential predecessor string.
        # Step 6: If this generated predecessor exists in the dp dictionary, it means a valid chain can be formed, so update dp[word] as max(dp[word], dp[prev] + 1).
        # Step 7: While processing each word, also keep track of the global maximum chain length using the variable `max_length`.
        # Step 8: After checking all possible predecessors for every word, return `max_length`, which represents the length of the longest valid word chain.
        words.sort(key=len)
        dp = {}
        max_length = 1

        for word in words:
            dp[word] = 1  # minimum chain length

            for i in range(len(word)):
                # remove one character
                prev = word[:i] + word[i+1:]

                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)

            max_length = max(max_length, dp[word])

        return max_length