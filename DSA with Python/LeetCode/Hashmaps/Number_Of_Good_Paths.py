# PROBLEMNUMBER:2421
# https://leetcode.com/problems/number-of-good-paths/
# 2421.Number of Good Paths
# DIFFICULTY:HARD
class Solution(object):
    def numberOfGoodPaths(self, vals, edges):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        # APPROACH:
        # - A good path is defined where the maximum value on the path
        #   is equal to the values at both endpoints.
        # - Use Union-Find (Disjoint Set Union) to process nodes in
        #   increasing order of their values.
        # - Sort edges by the maximum value of their endpoints so that
        #   we only connect nodes when allowed.
        # - Maintain a count of how many nodes with the same value exist
        #   in each connected component.
        # - For each value group, when nodes are connected, the number of
        #   new good paths formed is combinations of nodes with that value.
        # - Add single-node paths initially and accumulate valid pairs.

        n = len(vals)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        from collections import defaultdict

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        nodes = sorted(range(n), key=lambda x: vals[x])
        value_groups = defaultdict(list)
        for node in nodes:
            value_groups[vals[node]].append(node)

        result = n  # single-node good paths

        active = [False] * n

        for value in sorted(value_groups):
            for node in value_groups[value]:
                active[node] = True
                for nei in adj[node]:
                    if active[nei]:
                        union(node, nei)

            component_count = defaultdict(int)
            for node in value_groups[value]:
                root = find(node)
                component_count[root] += 1

            for count in component_count.values():
                result += count * (count - 1) // 2

        return result
