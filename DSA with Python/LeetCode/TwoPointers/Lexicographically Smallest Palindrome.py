# PROBLEM NUMBER: 2697
# https://leetcode.com/problems/lexicographically-smallest-palindrome/
# 2697. Lexicographically Smallest Palindrome
# DIFFICULTY: EASY
class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach:
        # We need to convert the given string into the lexicographically smallest palindrome.
        # A palindrome reads the same from left to right and right to left.
        
        # Step 1: Convert the string into a list so that characters can be modified easily.
        
        # Step 2: Use two pointers:
        #         i → starting index
        #         j → ending index
        
        # Step 3: Traverse the string while i < j.
        
        # Step 4: For each pair of characters s[i] and s[j]:
        #         • If they are already equal, move both pointers inward.
        #         • If they are different, choose the smaller character using min(s[i], s[j])
        #           and assign it to both positions to maintain palindrome property.
        
        # Step 5: Increment i and decrement j to continue checking the next pair.
        
        # Step 6: After processing all pairs, convert the list back to a string.
        
        # Step 7: Return the resulting smallest palindrome.

        s = list(s)
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                smaller = min(s[i], s[j])
                s[i] = smaller
                s[j] = smaller
            i += 1
            j -= 1
        
        return "".join(s)