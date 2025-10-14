# PROBLEM NUMBER:49
# https://leetcode.com/problems/group-anagrams/
# 49.Group Anagrams
# DIFFICULTY:MEDIUM
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # APPROACH:
      # This solution groups words that are anagrams of each other using a character frequency count as a key.
      # 1. Initialize a defaultdict of lists `ans` to store grouped anagrams.
      # 2. For each string `s` in `strs`:
      #    - Create a list `count` of size 26 (for each lowercase letter).
      #    - Increment the count at the index corresponding to each character (`ord(char) - ord('a')`).
      #    - Convert this list into a tuple (immutable and hashable) to use as a key in the dictionary.
      #    - Append the word `s` to the list corresponding to that key.
      # 3. Finally, return the grouped values as a list of lists using `list(ans.values())`.
      # This approach effectively groups all anagrams together because anagrams share identical character frequency patterns.
      # Time Complexity: O(n * k) — where n = number of strings, k = average string length.
      # Space Complexity: O(n * k) — for storing frequency keys and grouped anagrams.
        ans=defaultdict(list)
        for s in strs:
            count=[0]*26
            for char in s:
                count[ord(char)-ord('a')]+=1
            ans[tuple(count)].append(s)
        return list(ans.values())