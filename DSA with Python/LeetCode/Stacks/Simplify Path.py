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
        # We use a stack to simulate
        # directory navigation.
        #
        # Split the path using '/'
        # and process each component.
        #
        # • Ignore empty strings and '.'
        #   since they do not change the path.
        #
        # • For '..', move one directory
        #   up by popping from the stack.
        #
        # • Otherwise, push the directory
        #   name onto the stack.
        #
        # Finally, join all directories in
        # the stack to form the simplified
        # canonical path.

        stack = []

        parts = path.split('/')

        for part in parts:

            if part == '' or part == '.':
                continue

            elif part == '..':

                if stack:
                    stack.pop()

            else:
                stack.append(part)

        return '/' + '/'.join(stack)