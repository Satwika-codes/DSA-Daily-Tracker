# PROBLEM NUMBER: 1944
# https://leetcode.com/problems/number-of-visible-people-in-a-queue/
# 1994. Number of Visible People in a Queue
# DIFFICULTY: MEDIUM

class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        # Approach:
        # For each person, count how many people to the right are visible.
        #
        # Key Idea:
        # Use a monotonic decreasing stack while scanning right to left.
        #
        # Step 1: Traverse from right to left
        #         • Right side people are already processed
        #
        # Step 2: Use stack to store heights
        #         • Maintains decreasing order
        #
        # Step 3: For each person:
        #         • Pop all shorter people:
        #             → each popped person is visible
        #
        # Step 4: If stack still has a person:
        #         • That first taller/equal person is also visible
        #
        # Step 5: Total visible people:
        #         • popped count + possible blocker
        #
        # Step 6: Store answer for current person
        #
        # Step 7: Push current height into stack
        #
        # Step 8: Return result array

        n = len(heights)
        ans = [0] * n
        stack = []

        for i in range(n-1, -1, -1):
            seen = 0

            while stack and heights[i] > stack[-1]:
                stack.pop()
                seen += 1

            if stack:
                seen += 1

            ans[i] = seen
            stack.append(heights[i])

        return ans