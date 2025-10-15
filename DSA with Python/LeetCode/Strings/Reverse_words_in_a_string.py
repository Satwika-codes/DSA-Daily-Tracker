# PROBLEM MUMBER: 151
# https://leetcode.com/problems/reverse-words-in-a-string/
# 151 Reverse Words in a string
# DIFFICULTY: MEDIUM
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # APPROACH:
        # This solution reverses the order of words in a given string `s`.
        # 1. Split the input string `s` into a list of words using `split()`, which automatically removes extra spaces.
        # 2. Initialize two pointers: `left` at the start and `right` at the end of the list.
        # 3. Swap the words at `left` and `right` positions while moving both pointers toward the center until they meet.
        # 4. After all swaps, use `" ".join(words)` to combine the reversed list back into a single string.
        # This manual two-pointer swapping approach demonstrates in-place reversal logic instead of using built-in reverse methods.
        # Time Complexity: O(n) — where n is the number of words.
        # Space Complexity: O(n) — for storing the list of words.
        words=s.split()
        left=0
        right=len(words)-1
        while left<right:
            words[left],words[right]=words[right],words[left]
            left+=1
            right-=1
        return " ".join(words)