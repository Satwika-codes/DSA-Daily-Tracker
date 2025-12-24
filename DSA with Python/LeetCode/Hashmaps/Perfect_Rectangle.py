# PROBLEM NUMBER :391
# https://leetcode.com/problems/perfect-rectangle/
# 391.Perfect Rectangle
# DIFFICULTY: HARD
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        APPROACH:
        - The goal is to check whether all given small rectangles perfectly form
          one large rectangle without overlaps or gaps.
        - Track the total area of all small rectangles and compare it with the
          area of the bounding rectangle formed by the extreme coordinates.
        - Use a set to track corner points:
            * Each rectangle contributes four corners.
            * Corners that appear even times cancel out.
            * In a perfect cover, only the four corners of the large rectangle
              should remain.
        - If total area matches and exactly four correct corners remain,
          the rectangles form a perfect cover.
        """

        area = 0
        corners = set()

        min_x = min_y = float('inf')
        max_x = max_y = float('-inf')

        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)

            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if point in corners:
                    corners.remove(point)
                else:
                    corners.add(point)

        expected_area = (max_x - min_x) * (max_y - min_y)

        if area != expected_area:
            return False

        expected_corners = {
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y)
        }

        return corners == expected_corners

        