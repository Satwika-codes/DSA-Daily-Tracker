# PROBLEM NUMBER:839
# https://leetcode.com/problems/similar-string-groups/
# 839.Similar String Groups
# DIFFICULTY:HARD
class Solution(object):
    def numSimilarGroups(self, strs):
         """
        :type strs: List[str]
        :rtype: int
        """      
        # APPROACH:
        # - Treat each string as a node in a graph.
        # - Two strings are connected if they are "similar", i.e.,
        #   they differ in exactly two positions or are identical.
        # - Use Union-Find (Disjoint Set Union) to group connected strings.
        # - Compare every pair of strings and union them if they are similar.
        # - The number of unique parents at the end represents the number
        #   of similar string groups.
            def are_similar(s1, s2):
            diff = 0
            for a, b in zip(s1, s2):
                if a != b:
                    diff += 1
                    if diff > 2:
                        return False
            return diff == 2 or diff == 0
        parent = list(range(len(strs)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

      
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if are_similar(strs[i], strs[j]):
                    union(i, j)
        groups = set(find(i) for i in range(len(strs)))
        return len(groups)