class Solution(object):
    def matchReplacement(self, s, sub, mappings):
        """
        :type s: str
        :type sub: str
        :type mappings: List[List[str]]
        :rtype: bool
        """
        # APPROACH:
        # 1. Preprocess the mappings list into a dictionary where each character in 'sub'
        #    maps to a set of characters it can be replaced with.
        # 2. Iterate through all possible starting indices in 's' where 'sub' can fit.
        # 3. For each position, compare characters of 'sub' with the corresponding
        #    characters in 's':
        #    - If characters are equal, it is a valid match.
        #    - Otherwise, check whether the current character of 'sub' can be replaced
        #      with the character from 's' using the mapping dictionary.
        # 4. If all characters match or can be replaced successfully for any window,
        #    return True.
        # 5. If no valid window is found, return False.

        # Time Complexity: O(len(s) * len(sub))
        # Space Complexity: O(len(mappings))
        
        mp = {}
        for a, b in mappings:
            if a not in mp:
                mp[a] = set()
            mp[a].add(b)

        n, m = len(s), len(sub)

        for i in range(n - m + 1):
            ok = True
            for j in range(m):
                if s[i + j] == sub[j]:
                    continue
                if sub[j] not in mp or s[i + j] not in mp[sub[j]]:
                    ok = False
                    break
            if ok:
                return True

        return False
