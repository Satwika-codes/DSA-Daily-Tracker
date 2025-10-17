# PROBLEM NUMBER:20
# https://leetcode.com/problems/valid-parentheses/
# 20.Valid Parentheses
# DIFFICULTY:
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # APPROACH:
        # This solution checks whether a string containing parentheses/brackets/braces is valid 
        # using a stack-based approach.
        # 1. Initialize an empty stack to keep track of opening brackets.
        # 2. Maintain a mapping (`pairs`) from each closing bracket to its corresponding opening one.
        # 3. Traverse each character in the string:
        #    - If the character is a closing bracket:
        #         • Check if the stack is empty or if the top of the stack doesn't match the corresponding opening bracket.
        #         • If either condition is true, return False (invalid sequence).
        #         • Otherwise, pop the top element (a valid pair found).
        #    - If it’s an opening bracket, push it onto the stack.
        # 4. After traversing all characters:
        #    - If the stack is empty, all brackets were matched correctly → return True.
        #    - Otherwise, return False (some brackets remain unmatched).
        # This approach ensures every opening bracket is properly closed in the correct order.
        # Time Complexity: O(n) — each character is processed once.
        # Space Complexity: O(n) — in the worst case (all opening brackets) the stack grows linearly.
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in pairs:  
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:  
                stack.append(ch)

        return len(stack) == 0