# PROBLEM NUMBER:832
# https://leetcode.com/problems/flipping-an-image/
# 832.Flipping an Image
# DIFFICULTY:EASY
class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        # Approach:
        # We need to perform two operations on every row of the matrix:
        # 1. Flip the image horizontally.
        # 2. Invert the image (0 → 1 and 1 → 0).
        
        # Step 1: Traverse each row of the matrix.
        
        # Step 2: Flip the row horizontally by reversing it.
        #         This mirrors the row.
        
        # Step 3: After reversing, invert every element in the row.
        #         Since the values are only 0 and 1, we can invert using:
        #         row[i] = 1 - row[i]
        
        # Step 4: Repeat this process for all rows.
        
        # Step 5: Return the modified image matrix.
        for row in image:
            # reverse row
            row.reverse()

            # invert values
            for i in range(len(row)):
                row[i] = 1 - row[i]

        return image