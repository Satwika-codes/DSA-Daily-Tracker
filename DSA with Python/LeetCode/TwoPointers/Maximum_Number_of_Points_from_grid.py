# PROBLEM NUMBER: 2503
# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/
# 2503.Maximum Number of Points from Grid Queries
# DIFFICULTY: HARD
import heapq
class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """       
        # Approach:
        # - Sort queries with original indices
        # - Use a min-heap starting from (0,0)
        # - Expand cells in increasing grid value order
        # - For each query q, count cells with value < q
        

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        # (query_value, original_index)
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        res = [0] * len(queries)

        heap = [(grid[0][0], 0, 0)]  # (value, row, col)
        visited[0][0] = True

        count = 0
        idx = 0

        for q, qi in sorted_queries:
            while heap and heap[0][0] < q:
                val, r, c = heapq.heappop(heap)
                count += 1

                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        visited[nr][nc] = True
                        heapq.heappush(heap, (grid[nr][nc], nr, nc))

            res[qi] = count

        return res
