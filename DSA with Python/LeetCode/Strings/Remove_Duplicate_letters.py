# PROBLEM NUMBER: 316
# https://leetcode.com/problems/remove-duplicate-letters/
# 316. Remove Duplicate Letters
# DIFFICULTY: MEDIUM
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach:
        # 1. The goal is to remove duplicate letters so that the resulting string 
        #    is the smallest in **lexicographical order** among all possible results.
        # 2. Use a **stack** to build the result string:
        #       - Keep track of the **last occurrence** of each character using a dictionary.
        #       - Use a **set (seen)** to ensure each character appears only once in the stack.
        #       - For each character in the string:
        #             -If it's already seen, skip it.
        #             -Otherwise, while the stack is not empty and:
        #                - The top of the stack is lexicographically greater than the current char, and
        #                - The top character appears again later in the string (based on `last`),
        #              ➜ pop it from the stack and remove it from `seen`.
        #             -Add the current character to the stack and mark it as seen.
        # 3. Finally, join all characters from the stack to form the result string.
        last = {ch: i for i, ch in enumerate(s)}
        stack = []
        seen = set()

        for i, ch in enumerate(s):
            if ch in seen:
                continue
            while stack and ch < stack[-1] and i < last[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)

        return "".join(stack)