#PROBLEM NUMBER: 68
#https://leetcode.com/problems/text-justification/
#68. Text Justification
#DIFFICULTY: HARD
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # APPROACH:
        # This solution formats a list of words into fully justified text with each line having exactly `maxWidth` characters.
        # 1. Initialize:
        #    - `res`: to store the final justified lines.
        #    - `cur`: to hold words of the current line.
        #    - `num_of_letters`: to track the total number of characters in `cur` (excluding spaces).
        # 2. For each word `w` in `words`:
        #    - Check if adding `w` (plus necessary spaces) exceeds `maxWidth`.
        #    - If it does:
        #        • Distribute extra spaces evenly between words in `cur` using the pattern `i % (len(cur) - 1 or 1)`.
        #        • Append the justified line to `res`.
        #        • Reset `cur` and `num_of_letters` for the next line.
        #    - Otherwise, add `w` to `cur` and update `num_of_letters`.
        # 3. After processing all words:
        #    - Join the last line with single spaces (`' '.join(cur)`) and left-justify it using `.ljust(maxWidth)` 
        #      since the last line should be left-aligned.
        # This approach ensures that:
        # - Extra spaces are evenly distributed between words.
        # - If spacing isn’t divisible evenly, extra spaces go from left to right.
        # - The last line is left-aligned, as per text justification rules.
        # Time Complexity: O(n * k) — where n is the number of words and k is the average word length.
        # Space Complexity: O(n * k) — for storing the justified lines.
        res = []
        cur = []
        num_of_letters = 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur = []
                num_of_letters = 0
            cur.append(w)
            num_of_letters += len(w)
        res.append(' '.join(cur).ljust(maxWidth))
        return res