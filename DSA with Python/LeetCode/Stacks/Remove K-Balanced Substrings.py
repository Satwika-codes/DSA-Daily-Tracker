# PROBLEM NUMBER: 3703
# https://leetcode.com/problems/remove-k-balanced-substrings/
# 3703. Remove K-Balanced Substrings
# DIFFICULTY: MEDIUM

class Solution(object):
    def removeSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        # Approach:
        # We use a stack to store groups of
        # consecutive characters along with
        # their frequencies.
        #
        # Whenever we encounter matching
        # groups of '(' and ')' having at
        # least k occurrences each, we remove
        # k characters from both groups.
        #
        # After a removal, some groups may
        # become empty and are removed from
        # the stack.
        #
        # If adjacent groups become the same
        # character after deletion, merge them
        # into a single group.
        #
        # Finally, rebuild the string from
        # the remaining groups.

        stack = []  # [character, count]

        for ch in s:

            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1

            else:
                stack.append([ch, 1])

            while len(stack) >= 2:

                if (
                    stack[-2][0] == '(' and
                    stack[-1][0] == ')' and
                    stack[-2][1] >= k and
                    stack[-1][1] >= k
                ):

                    stack[-2][1] -= k
                    stack[-1][1] -= k

                    if stack[-1][1] == 0:
                        stack.pop()

                    if stack and stack[-1][1] == 0:
                        stack.pop()

                    # Merge adjacent equal groups
                    if (
                        len(stack) >= 2 and
                        stack[-1][0] == stack[-2][0]
                    ):

                        stack[-2][1] += stack[-1][1]
                        stack.pop()

                else:
                    break

        ans = []

        for ch, cnt in stack:
            ans.append(ch * cnt)

        return "".join(ans)