# PROBLEM NUMBER: 844
# https://leetcode.com/problems/backspace-string-compare/
# 844. Backspace String Compare
# DIFFICULTY: EASY
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Approach:
        # We need to compare two strings after applying backspace operations.
        # The character '#' represents a backspace which removes the previous character.
        
        # Step 1: Create a helper function build(string) that simulates typing
        #         the string with backspaces applied.
        
        # Step 2: Use a stack to build the final string:
        #         • Traverse each character in the string.
        #         • If the character is '#':
        #               Pop the last character from the stack if it exists.
        #         • Otherwise:
        #               Push the character onto the stack.
        
        # Step 3: After processing the entire string, convert the stack
        #         into the final processed string.
        
        # Step 4: Apply the build function to both strings s and t.
        
        # Step 5: Compare the two processed strings.
        
        # Step 6: If they are equal, return True; otherwise return False.
        def build(string):
            stack = []
            for c in string:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return "".join(stack)

        return build(s) == build(t)