# PROBLEM NUMBER: 733
# https://leetcode.com/problems/flood-fill/
# 733.Flood Fill
# DIFFICULTY: EASY
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        # Approach (DFS Flood Fill):
        #
        # Goal:
        # Recolor the starting pixel (sr, sc) and all connected pixels
        # that share the same original color (4-directionally: up/down/left/right).
        #
        # Steps:
        # 1. Store the old color of image[sr][sc].
        # 2. If the old color is already equal to the new color, return immediately
        #    (nothing needs to be changed).
        #
        # 3. Use DFS from (sr, sc):
        #       • If the current pixel is out of bounds → stop.
        #       • If the pixel color is not the old color → stop.
        #       • Otherwise, recolor it to the new color.
        #
        # 4. From each valid pixel, recursively move in 4 directions:
        #       (r+1,c), (r-1,c), (r,c+1), (r,c-1)
        #
        # 5. After DFS completes, the entire connected component is recolored.
        #
        # Time Complexity: O(m*n) worst case (every pixel visited once)
        # Space Complexity: O(m*n) recursion stack in worst case

        old = image[sr][sc]
        if old == color:
            return image
        
        m, n = len(image), len(image[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or image[r][c] != old:
                return
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image
