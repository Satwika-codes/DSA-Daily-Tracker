# PROBLEM NUMBER :149
# https://leetcode.com/problems/max-points-on-a-line/
# 149.Max Points On Line
# DIFFICULTY: HARD
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # APPROACH
        # We handle the edge case where the number of points is very small
        # For each point, we treat it as an anchor and calculate slopes with all other points
        # Slopes are stored using a hashmap to count how many points lie on the same line
        # Vertical lines are handled separately to avoid division by zero
        # Duplicate points are counted and added to the final result for that anchor
        # For every anchor point, we find the maximum number of points forming a line
        # The global maximum across all anchors is returned as the answer

        if len(points) <= 2:
            return len(points)

        max_points = 1
        for i in range(len(points)):
            slopes = {}
            same_point = 0
            curr_max = 0
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2:
                    same_point += 1
                else:
                    dx = x2 - x1
                    dy = y2 - y1
                    g = self.gcd(dx, dy)
                    dx //= g
                    dy //= g

                    slope = (dx, dy)
                    slopes[slope] = slopes.get(slope, 0) + 1
                    curr_max = max(curr_max, slopes[slope])

           
            max_points = max(max_points, curr_max + same_point + 1)

        return max_points

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
