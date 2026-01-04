# PROBLEM NUMBER: 2426
# https://leetcode.com/problems/count-pairs-of-nodes-in-a-tree/
# 2426. Count Pairs of Nodes in a Tree
# DIFFICULTY: HARD
class Solution(object):
    def countPairs(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """

    
        # Approach:
        # For each node, we compute its degree (number of edges connected to it).
        # We also count how many times each edge appears between two nodes,
        # since multiple edges affect the final count.

        # Steps:
        # 1. Compute degree of every node.
        # 2. Sort the degree array.
        # 3. For each query q, use two pointers to count pairs (u, v) such that
        #    degree[u] + degree[v] > q.
        # 4. This overcounts pairs where the actual number of shared edges
        #    reduces the effective degree sum, so we subtract those invalid pairs
        #    using the edge frequency map.

        # This ensures correctness for multiple edges and large constraints.
        

        from collections import defaultdict

        degree = [0] * (n + 1)
        edge_count = defaultdict(int)

        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            if u > v:
                u, v = v, u
            edge_count[(u, v)] += 1

        sorted_deg = sorted(degree[1:])
        res = []

        for q in queries:
            left, right = 0, n - 1
            total = 0

            while left < right:
                if sorted_deg[left] + sorted_deg[right] > q:
                    total += right - left
                    right -= 1
                else:
                    left += 1

            for (u, v), cnt in edge_count.items():
                if degree[u] + degree[v] > q and degree[u] + degree[v] - cnt <= q:
                    total -= 1

            res.append(total)

        return res
