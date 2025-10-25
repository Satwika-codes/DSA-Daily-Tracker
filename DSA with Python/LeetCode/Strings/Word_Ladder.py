# PROBLEM NUMBER : 127
# https://leetcode.com/problems/word-ladder/
# 127. Word Ladder
# DIFFICULTY: HARD
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Approach:
        # This solution finds the shortest transformation sequence from `beginWord` to `endWord`
        # by changing one letter at a time such that each intermediate word exists in `wordList`.
        # It uses **Breadth-First Search (BFS)**.
        # 1. Convert `wordList` to a set `wordSet` for O(1) lookups. If `endWord` is not in the set, return 0.
        # 2. Initialize a queue with a tuple `(beginWord, 1)` where 1 represents the current transformation length.
        # 3. While the queue is not empty:
        #    - Pop the front word and its associated length.
        #    - If the word equals `endWord`, return the current length.
        #    - For each character position in the word, try replacing it with 'a' to 'z':
        #        - If the new word exists in `wordSet`, remove it from the set and append it to the queue with length +1.
        # 4. If BFS completes without finding `endWord`, return 0.
        # This BFS ensures the shortest path is found first.
        # Time Complexity: O(N * L * 26) — N = number of words, L = length of each word.
        # Space Complexity: O(N) — for the set and BFS queue.
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        queue.append((next_word, length + 1))
        
        return 0
        