# PROBLEM NUMBER : 854
# https://leetcode.com/problems/k-similar-strings/
# 854.K_Similar-Strings
# DIFFICULTY:HARD
class Solution(object):
    def kSimilarity(self, s1, s2):
        """ 
        :type s1: str 
        :type s2: str 
        :rtype: int 
        """
        # APPROACH:
        # - The goal is to transform s1 into s2 using the minimum number of swaps.
        # - Use BFS where each state represents a string configuration.
        # - At each step, find the first index where the current string
        #   differs from s2.
        # - Try swapping that index with a later index that moves the character
        #   closer to its correct position.
        # - BFS guarantees the first time we reach s2 is with minimum swaps.
    
        from collections import deque

        queue = deque([(s1, 0)])
        visited = set([s1])

        while queue:
            curr, steps = queue.popleft()
            if curr == s2:
                return steps

            i = 0
            while curr[i] == s2[i]:
                i += 1

            for j in range(i + 1, len(curr)):
                if curr[j] == s2[i] and curr[j] != s2[j]:
                    new_state = list(curr)
                    new_state[i], new_state[j] = new_state[j], new_state[i]
                    new_state = "".join(new_state)

                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, steps + 1))
