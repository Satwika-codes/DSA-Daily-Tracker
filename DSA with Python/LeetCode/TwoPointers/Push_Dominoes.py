# https://leetcode.com/problems/push-dominoes/
# PROBLEM NUMBER: 838
# 838. Push Dominoes
# DIFFICULTY: MEDIUM
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        # Approach:
        # Step 1: To simplify edge cases, add a virtual 'L' at the beginning and a virtual 'R' at the end of the domino string. This ensures that every sequence of '.' will always be bounded by two forces.
        # Step 2: Use two pointers `i` and `j` to represent the positions of the last seen non-dot domino and the current non-dot domino respectively.
        # Step 3: Iterate through the modified string `s` starting from index 1. Whenever the current character is '.', skip it because it belongs to a middle segment whose final state depends on surrounding forces.
        # Step 4: When a non-dot character is encountered at position `j`, calculate the number of dominoes between `i` and `j` using `middle = j - i - 1`.
        # Step 5: If `i` is not the artificial starting boundary, append the domino at position `i` to the result because it is already resolved.
        # Step 6: If the dominoes at `i` and `j` are the same (both 'L' or both 'R'), all dominoes in the middle will fall in that same direction, so fill the middle with that character repeated `middle` times.
        # Step 7: If the pattern is 'L ... R', the forces move away from each other so the dominoes in the middle remain upright, meaning we append `middle` number of '.' characters.
        # Step 8: If the pattern is 'R ... L', the forces move toward each other. In this case half of the dominoes fall to the right, half fall to the left, and if the count is odd the middle domino remains upright.
        # Step 9: After processing this segment, move `i` to `j` to start processing the next section.
        # Step 10: Continue until the entire string is processed, then join all collected parts of the result list into a single string and return it.

        s = 'L' + dominoes + 'R'
        result = []
        i = 0

        for j in range(1, len(s)):
            if s[j] == '.':
                continue

            middle = j - i - 1

            if i > 0:
                result.append(s[i])

            if s[i] == s[j]:
                result.append(s[i] * middle)
            elif s[i] == 'L' and s[j] == 'R':
                result.append('.' * middle)
            else:  # R ... L
                result.append('R' * (middle // 2))
                if middle % 2 == 1:
                    result.append('.')
                result.append('L' * (middle // 2))

            i = j

        return ''.join(result)