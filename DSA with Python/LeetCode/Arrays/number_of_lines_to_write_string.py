# PROBLEM NUMBER: 806
# https://leetcode.com/problems/number-of-lines-to-write-string/
# 806. Number of Lines To Write String
# DIFFICULTY: EASY
class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        # Approach:
        # Step 1: Each character has a fixed width given by 'widths'.
        #         We keep writing characters on a line until adding a character 
        #         would exceed 100 units.
        #
        # Step 2: Maintain:
        #         • 'lines' → number of lines needed.
        #         • 'width' → current width used in the current line.
        #
        # Step 3: For each character:
        #         • Find its width using widths[ord(ch) - ord('a')].
        #         • If adding this width exceeds 100:
        #               → Start a new line (lines += 1), reset width to this character's width.
        #         • Else:
        #               → Add it to the current line.
        #
        # Step 4: Final result is [total lines, width of last line].
        #
        # Time Complexity: O(n)

        lines = 1
        width = 0
        
        for ch in s:
            w = widths[ord(ch) - ord('a')]
            if width + w > 100:
                lines += 1
                width = w
            else:
                width += w
        
        return [lines, width]
