# PROBLEM NUMBER: 3298
# https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string/
# Count Substrings That Can Be Rearranged to Contain a String
# DIFFICULTY: HARD
class Solution(object):
    def validSubstringCount(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Approach:
        # We need to count substrings of word1 such that
        # they contain all characters of word2 (with required frequency).
        #
        # Step 1: Use two hashmaps:
        #         • need → frequency of characters in word2
        #         • window → frequency of current window in word1
        #
        # Step 2: Track:
        #         • required → number of unique characters in word2
        #         • formed → how many characters currently satisfy required frequency
        #
        # Step 3: Use sliding window with left and right pointers
        #
        # Step 4: Expand window (move right):
        #         • Add character to window
        #         • If its frequency matches need → increment formed
        #
        # Step 5: When formed == required (valid window):
        #         • All substrings starting from current left
        #           and ending from right to end are valid
        #         • So add (n - right) to result
        #
        # Step 6: Shrink window from left:
        #         • Remove left character from window
        #         • If it breaks required frequency → decrement formed
        #
        # Step 7: Continue process until entire string is covered
        #
        # Step 8: Return total count

        need = Counter(word2)
        window = Counter()

        required = len(need)
        formed = 0

        left = 0
        res = 0
        n = len(word1)

        for right in range(n):
            ch = word1[right]
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            # shrink when valid
            while formed == required:
                res += (n - right)

                left_ch = word1[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1

                left += 1

        return res