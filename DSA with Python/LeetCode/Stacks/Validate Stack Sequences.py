# PROBLEM NUMBER: 946
# https://leetcode.com/problems/validate-stack-sequences/
# 946. Validate Stack Sequences
# DIFFICULTY: MEDIUM

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """

        # Approach:
        # We simulate the stack operations
        # directly using the given pushed
        # and popped sequences.
        #
        # Push elements one by one from
        # the pushed array.
        #
        # After every push, keep popping
        # while the stack top matches the
        # current element in the popped array.
        #
        # If all elements can be matched and
        # the stack becomes empty at the end,
        # the sequences are valid.

        stack = []
        j = 0

        for x in pushed:

            stack.append(x)

            while (
                stack and
                j < len(popped) and
                stack[-1] == popped[j]
            ):
                stack.pop()
                j += 1

        return len(stack) == 0