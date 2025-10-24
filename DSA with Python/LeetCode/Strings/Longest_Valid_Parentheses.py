# PROBLEM NUMBER: 32
# https://leetcode.com/problems/longest-valid-parentheses/
# 32. Longest Valid Parentheses
# DIFFICULTY: HARD
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 💡 Approach:
        # This solution uses a **stack-based approach** to find the length of the longest valid (well-formed) parentheses substring.
        # 1. Initialize a stack with -1 to handle base indices for valid substrings.
        # 2. Iterate through the string using index `i` and character `ch`:
        #    - If `ch` is '(', push its index onto the stack.
        #    - If `ch` is ')':
        #        - Pop one element from the stack (matching '(' if exists).
        #        - If the stack becomes empty, push the current index `i` as a new base for upcoming substrings.
        #        - Otherwise, calculate the valid length as `i - stack[-1]` and update `max_len`.
        # 3. Return `max_len` as the final result.
        # This approach ensures every valid pair is tracked and invalid boundaries are marked for future reference.
        # Time Complexity: O(n) — single pass through the string.
        # Space Complexity: O(n) — due to stack usage.

        stack = [-1]
        max_len = 0
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len