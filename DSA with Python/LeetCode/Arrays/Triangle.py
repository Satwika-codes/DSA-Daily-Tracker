# PROBLEM NUMBER: 120
# https://leetcode.com/problems/triangle/
# 120. Triangle
# DIFFICULTY: MEDIUM
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Approach:
        # Step 1: Start from the second last row of the triangle and move upwards.
        # Step 2: For each element in the current row, add the minimum of the two elements
        #         directly below it in the next row. This effectively reduces the problem
        #         by combining the optimal choices from the bottom up.
        # Step 3: Continue this process until reaching the top row.
        # Step 4: The top element (triangle[0][0]) will contain the minimum path sum from top to bottom.
        
        n = len(triangle)
        
        for row in range(n - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row + 1][col],
                                          triangle[row + 1][col + 1])
        
        return triangle[0][0]
