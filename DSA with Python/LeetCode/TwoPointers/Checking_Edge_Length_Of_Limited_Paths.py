# PROBLEM NUMBER: 1697
# https://leetcode.com/problems/checking-edge-length-of-limited-paths/
# 1697.Checking Edge Length Of Limited Paths
# DIFFICULTY: HARD
class Solution(object):
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        """
        :type n: int
        :type edgeList: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Approach:
        # - This problem is solved using Offline Queries + Union-Find (DSU).
        # - Sort all edges by their weights in ascending order.
        # - Attach the original index to each query and sort queries by their limit.
        # - Progressively union nodes using edges whose weights are strictly less than
        #   the current query's limit.
        # - For each query, after adding all valid edges, check if the two nodes
        #   belong to the same connected component.
        # - Store results in the original query order.
        # - Time Complexity: O((E + Q) log E)
        
        
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
        
        edgeList.sort(key=lambda x: x[2])
        indexed_queries = [(p, q, limit, i) for i, (p, q, limit) in enumerate(queries)]
        indexed_queries.sort(key=lambda x: x[2])
        
        res = [False] * len(queries)
        ei = 0
        
        for u, v, limit, idx in indexed_queries:
            while ei < len(edgeList) and edgeList[ei][2] < limit:
                union(edgeList[ei][0], edgeList[ei][1])
                ei += 1
            res[idx] = find(u) == find(v)
        
        return res
