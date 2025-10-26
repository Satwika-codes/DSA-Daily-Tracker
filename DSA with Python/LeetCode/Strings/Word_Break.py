# PROBLEM NUMBER: 139
# https://leetcode.com/problems/word-break/
# 139. Word Break
# DIFFICULTY: MEDIUM
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Approach:
        # This solution determines if a string `s` can be segmented into words from `wordDict`
        # using **Breadth-First Search (BFS)** to explore all possible segmentations.
        # 1. Convert `wordDict` to a set `wordSet` for O(1) lookups.
        # 2. Initialize a queue with index 0 representing the starting position.
        # 3. Maintain a `visited` set to avoid revisiting the same start index.
        # 4. While the queue is not empty:
        #    - Pop a start index.
        #    - If start equals the length of `s`, return True (entire string segmented).
        #    - If start has already been visited, skip it.
        #    - For each end index from start+1 to len(s)+1:
        #        - If `s[start:end]` exists in `wordSet`, append `end` to the queue.
        # 5. If BFS completes without reaching the end, return False.
        # This BFS approach ensures all possible segmentations are explored efficiently without revisiting.
        # Time Complexity: O(n^2) — checking all substrings.
        # Space Complexity: O(n) — for queue and visited set.

        wordSet = set(wordDict)
        queue = deque([0])
        visited = set()
        
        while queue:
            start = queue.popleft()
            if start == len(s):
                return True
            if start in visited:
                continue
            visited.add(start)
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet:
                    queue.append(end)
        
        return False