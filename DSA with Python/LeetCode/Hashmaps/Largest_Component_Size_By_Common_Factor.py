# PROBLEM NUMBER: 952
# https://leetcode.com/problems/largest-component-size-by-common-factor/
# Largest Component Size By Common Factor
# DIFFICULTY: HARD
class Solution(object):
    def largestComponentSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # APPROACH:
        # 1. Treat each number as a node in a graph.
        # 2. Two nodes are connected if the corresponding numbers share
        #    a common factor greater than 1.
        # 3. Use Union-Find (Disjoint Set Union) to group numbers by their factors.
        # 4. For each number, factorize it and union the number with its factors.
        # 5. Count the size of each connected component and return the maximum size.

        # Time Complexity:
        # - O(n * sqrt(max(nums)))

        # Space Complexity:
        # - O(n + max(nums))
        
        from collections import defaultdict

        parent = {}

        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for num in nums:
            x = num
            f = 2
            while f * f <= x:
                if x % f == 0:
                    union(num, f)
                    while x % f == 0:
                        x //= f
                f += 1
            if x > 1:
                union(num, x)

        count = defaultdict(int)
        for num in nums:
            count[find(num)] += 1

        return max(count.values())
