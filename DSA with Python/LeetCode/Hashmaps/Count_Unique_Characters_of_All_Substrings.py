# PROBLEM NUMBER:828
# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/
# 828.Count Unique Characters Of All Substrings Of a Given String
# DIFFICULTY:HARD
class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Approach:
        # Count the contribution of each character to all possible substrings.
        # For each character, track the indices of its previous and next occurrences.
        # Calculate contribution as (current_index - prev_index) * (next_index - current_index)
        # Sum contributions for all characters in the string to get the total count.
        # Use a dictionary to store indices of characters for efficient lookup.
        # This allows us to count unique characters in all substrings without generating substrings.
        
        char_indices = {}
        for i, c in enumerate(s):
            if c not in char_indices:
                char_indices[c] = []
            char_indices[c].append(i)
        
        total = 0
        for c in char_indices:
            indices = [-1] + char_indices[c] + [len(s)]
            for i in range(1, len(indices)-1):
                total += (indices[i] - indices[i-1]) * (indices[i+1] - indices[i])
        
        return total
