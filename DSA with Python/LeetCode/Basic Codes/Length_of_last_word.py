#PROBLEM NUMBER: 58
# https://leetcode.com/problems/length-of-last-word/
#DIFFICULTY-EASY
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        # APPROACH:
        # This solution finds the length of the last word in a given string `s`.
        # 1. Use `strip()` to remove any leading or trailing spaces from the string.
        # 2. Split the cleaned string into a list of words using `split()`, which separates by whitespace.
        # 3. Access the last word in the list using `[-1]` and return its length using `len()`.
        # This approach efficiently handles extra spaces and works in a single line, providing a clean and concise solution.
        :type s: str
        :rtype: int
        """
        return len(s.strip().split()[-1])