# PROBLEM NUMBER:2612
# https://leetcode.com/problems/minimum-reverse-operations/
# 2612. Minimum Reverse Operations
# DIFFICULTY: HARD
class Solution(object):
    def minReverseOperations(self, n, p, banned, k):
        """
        :type n: int
        :type p: int
        :type banned: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Approach:
        # We perform BFS starting from position p.

        # Reversing a subarray of length k moves index x to:
        # new_index = 2*l + k - 1 - x,
        # where l is the starting index of the reversed subarray.

        # For a given x:
        # l ranges from max(0, x - k + 1) to min(x, n - k),
        # which produces a continuous range [start, end] of reachable indices.

        # Key optimization:
        # - Reachable indices always have fixed parity.
        # - We maintain two sorted lists of unvisited indices (even and odd).
        # - Using binary search, we extract only valid indices in range
        #   and remove them once visited.

        # This ensures each index is processed once,
        # giving O(n log n) time and avoiding TLE.
        
        from collections import deque
        from bisect import bisect_left, bisect_right

        banned = set(banned)
        res = [-1] * n
        res[p] = 0

        even, odd = [], []
        for i in range(n):
            if i != p and i not in banned:
                if i % 2 == 0:
                    even.append(i)
                else:
                    odd.append(i)

        q = deque([p])

        while q:
            x = q.popleft()

            l_min = max(0, x - k + 1)
            l_max = min(x, n - k)
            if l_min > l_max:
                continue

            start = 2 * l_min + k - 1 - x
            end = 2 * l_max + k - 1 - x

            target = even if start % 2 == 0 else odd
            left = bisect_left(target, start)
            right = bisect_right(target, end)

            for i in target[left:right]:
                res[i] = res[x] + 1
                q.append(i)

            del target[left:right]

        return res
