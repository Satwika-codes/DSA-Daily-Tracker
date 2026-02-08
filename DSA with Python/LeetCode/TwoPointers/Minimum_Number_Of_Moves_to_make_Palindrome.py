# PROBLEM NUMBER: 2193
# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/
# 2193. Minimum Number of Moves to Make Palindrome
# DIFFICULTY: HARD
class Solution(object):
    def minMovesToMakePalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """  
        # Approach:
        # We use a greedy two-pointer technique.

        # Idea:
        # - A palindrome reads the same from both ends.
        # - We compare characters from the left and right.
        # - If they match, move both pointers inward.
        # - If they don’t match, search from the right side
        #   for a matching character for the left pointer.
        # - Bring the matching character to the right position
        #   using adjacent swaps and count the swaps.

        # Special Case:
        # - If no matching character is found, it means the
        #   left character is the middle character of the palindrome.
        #   Swap it with the next character.

        # Time Complexity:
        # - O(n^2) in the worst case (due to swaps)

        # Space Complexity:
        # - O(n) because strings are converted to list
        
        s = list(s)
        left, right = 0, len(s) - 1
        moves = 0

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # search for matching char from right side
                k = right
                while k > left and s[k] != s[left]:
                    k -= 1

                if k == left:
                    # middle character case
                    s[left], s[left + 1] = s[left + 1], s[left]
                    moves += 1
                else:
                    # bring matching character to right
                    while k < right:
                        s[k], s[k + 1] = s[k + 1], s[k]
                        moves += 1
                        k += 1
                    left += 1
                    right -= 1

        return moves
