# PROBEM NUMBER:84
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# 84. Largest Rectangle in Histogram
# DIFFICULTY: HARD

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Approach:
        # We need the largest rectangle possible in histogram.
        #
        # Step 1: Use a monotonic increasing stack:
        #         • Store indices of bars
        #
        # Step 2: Add a 0 at the end:
        #         • Forces remaining bars in stack to be processed
        #
        # Step 3: Traverse all bars
        #
        # Step 4: While current bar is smaller than stack top:
        #         • Current bar acts as right boundary
        #         • Pop taller bar and calculate area
        #
        # Step 5: For popped bar:
        #         • height = popped bar height
        #
        #         Width depends on:
        #         • If stack not empty:
        #             width = current_index - stack_top - 1
        #         • Else:
        #             width = current_index
        #
        # Step 6: Compute:
        #         area = height * width
        #         Update maximum area
        #
        # Step 7: Push current index into stack
        #
        # Step 8: Return maximum area

        stack = []
        max_area = 0

        heights.append(0)  # flush remaining bars

        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, h * width)

            stack.append(i)

        return max_area