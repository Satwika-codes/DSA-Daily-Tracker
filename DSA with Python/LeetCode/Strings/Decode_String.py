# PROBLEM NUMBER: 394
# https://leetcode.com/problems/decode-string/
# 394. Decode String
# DIFFICULTY: MEDIUM
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach:
        # - Use a stack to handle nested encodings.
        # - Traverse each character:
        #   • If it's a digit → build the full number (for multi-digit counts).  
        #   • If '[' → push current string and number to stack, then reset both.  
        #   • If ']' → pop from stack and repeat current string 'num' times, appending it to previous string.  
#   • Else → add character to current string.  
        # - Return the final decoded string.
        # Time: O(n), Space: O(n)
        stack = []
        curr_str = ""
        curr_num = 0
        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == "[":
                stack.append((curr_str, curr_num))
                curr_str, curr_num = "", 0
            elif c == "]":
                prev_str, num = stack.pop()
                curr_str = prev_str + curr_str * num
            else:
                curr_str += c
        return curr_str