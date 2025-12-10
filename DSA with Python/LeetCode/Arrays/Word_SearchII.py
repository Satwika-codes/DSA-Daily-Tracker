# PROBLEM NUMBER: 212
# https://leetcode.com/problems/word-search-ii/
# 212. Word Search II
# DIFFICULTY: HARD
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        # Approach:
        # This is the classic **Word Search II** problem.
        # A brute-force (checking each word separately using DFS) is too slow.
        # So we use a **Trie + DFS** optimization.
        #
        # Steps:
        # 1. Build a Trie from the list of words.
        #       - Each path represents a word.
        #       - Store the full word at the end using a special key '$'.
        #
        # 2. For each cell in the board, start DFS:
        #       - If the current character matches a Trie node, continue exploring.
        #       - Mark the cell as visited using '#'.
        #       - Explore neighbors (up, down, left, right).
        #
        # 3. Whenever we reach a Trie node containing '$', we found a complete word:
        #       - Add it to the result.
        #       - Delete '$' to avoid duplicates.
        #
        # 4. Smart Optimization:
        #       - After exploring a character, if the Trie node becomes empty,
        #         delete it. This **prunes the Trie** and avoids useless searches.
        #
        # Time Complexity:
        #   - Building Trie: O(total characters in words)
        #   - DFS: Each cell visited up to 4 directions but pruned early.
        #   - Much faster than brute-force.
        #
        # Space Complexity:
        #   - Trie storage + recursion stack.
        #
        # Overall: Very efficient for Word Search II.

        trie = {}
        for w in words:
            node = trie
            for c in w:
                node = node.setdefault(c, {})
            node['$'] = w  # store complete word

        res = []
        m, n = len(board), len(board[0])

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node:
                return

            nxt = node[ch]

            # Word found
            if '$' in nxt:
                res.append(nxt['$'])
                del nxt['$']  # avoid duplicates

            board[r][c] = '#'

            if r > 0: dfs(r-1, c, nxt)
            if r < m-1: dfs(r+1, c, nxt)
            if c > 0: dfs(r, c-1, nxt)
            if c < n-1: dfs(r, c+1, nxt)

            board[r][c] = ch

            # prune dead branch
            if not nxt:
                del node[ch]

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)

        return res
