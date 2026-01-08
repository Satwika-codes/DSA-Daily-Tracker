# PROBLEM NUMBER :301
# https://leetcode.com/problems/remove-invalid-parentheses/
# Remove Invalid Parentheses
# DIFFICULTY:HARD
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Approach:
        # We use Breadth-First Search (BFS) to remove parentheses level by level.

        # Each level represents strings formed by removing the same number
        # of characters. As soon as we find valid strings at a level,
        # we stop further BFS to ensure minimum removals.

        # Steps:
        # 1. Start BFS with the original string.
        # 2. For each string, check if it is valid.
        # 3. If valid, add it to the result list.
        # 4. If no valid string is found at the current level,
        #    generate next-level strings by removing one parenthesis
        #    at each possible position.
        # 5. Use a visited set to avoid duplicate processing.

        # This guarantees all returned strings are valid and require
        # the minimum number of removals.
        

        from collections import deque

        def is_valid(st):
            balance = 0
            for ch in st:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        res = []
        visited = set([s])
        q = deque([s])
        found = False

        while q:
            curr = q.popleft()

            if is_valid(curr):
                res.append(curr)
                found = True

            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in '()':
                    continue
                nxt = curr[:i] + curr[i + 1:]
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return res
