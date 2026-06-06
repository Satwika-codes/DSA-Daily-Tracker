# PROBLEM NUMBER: 402
# https://leetcode.com/problems/remove-k-digits/
# 402. Remove K Digits
# DIFFICULTY: MEDIUM

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        # Approach:
        # We use a monotonic increasing stack
        # to build the smallest possible number.
        #
        # While traversing the digits, remove
        # larger previous digits whenever a
        # smaller current digit is found and
        # removals are still available.
        #
        # This ensures that smaller digits
        # appear earlier, producing a smaller
        # overall number.
        #
        # If removals remain after traversal,
        # remove digits from the end since
        # they contribute the most to the value.
        #
        # Finally, remove leading zeros and
        # return the resulting number.

        stack = []

        for digit in num:

            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # If removals still remain, remove from the end
        while k > 0:
            stack.pop()
            k -= 1

        result = ''.join(stack).lstrip('0')

        return result if result else "0"