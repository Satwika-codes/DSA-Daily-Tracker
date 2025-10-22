# PROBLEM NUMBER: 71
# https://leetcode.com/problems/simplify-path/
# 71. Simplify Path
# DIFFICULTY: MEDIUM
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # Approach:
        # This solution simplifies a Unix-style file path using a **stack-based approach**.
        # 1. Split the input `path` by '/' to handle each segment separately.
        # 2. Initialize an empty stack to keep track of valid directory names.
        # 3. Iterate through each part:
        #    - Ignore empty strings and "." since they represent the current directory.
        #    - If the part is "..", pop from the stack if it is not empty (move up one directory).
        #    - Otherwise, push the directory name onto the stack.
        # 4. Join the stack contents with '/' and prepend a leading '/' to form the canonical path.
        # 5. Return the simplified path.
        # Time Complexity: O(n) — each part of the path is processed once.
        # Space Complexity: O(n) — stack may store all valid directories.

        parts = path.split('/')
        stack = []

        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)