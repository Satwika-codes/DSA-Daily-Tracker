# PROBLEM NUMBER :2103
# https://leetcode.com/problems/rings-and-rods/
# 2103.Rings and Rods
# DIFFICULTY:EASY
class Solution(object):
    def countPoints(self, rings):
    
        # APPROACH:
        # - Each rod can have up to three colors: Red (R), Green (G), and Blue (B).
        # - Parse the string in pairs, where each pair represents a color and a rod number.
        # - Use a hashmap (or array of sets) to track which colors are present on each rod.
        # - A rod is counted only if it has all three colors.
        # - Return the total number of such rods.

        rods = [set() for _ in range(10)]

        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = int(rings[i + 1])
            rods[rod].add(color)

        count = 0
        for colors in rods:
            if len(colors) == 3:
                count += 1

        return count
