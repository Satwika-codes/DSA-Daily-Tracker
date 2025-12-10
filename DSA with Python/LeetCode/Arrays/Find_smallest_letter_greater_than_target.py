# PROBLEM NUMBER: 744
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# 744. Find Smallest Letter Greater Than Target
# DIFFICULTY: EASY
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        # Approach:
        # Step 1: We need to find the smallest character strictly greater than 'target'.
        #         Since letters are sorted, we can apply Binary Search.
        #
        # Step 2: Use binary search:
        #         • If letters[mid] > target → potential answer, move left (r = mid - 1)
        #         • Else → move right (l = mid + 1)
        #
        # Step 3: After the loop, 'l' will point to the first letter > target.
        #
        # Step 4: If no such letter exists (l becomes equal to len(letters)),
        #         wrap around using modulo: letters[l % len(letters)]
        #         (because the list is circular as per problem requirement)
        #
        # Step 5: Return the letter at index l % len(letters).

        l, r = 0, len(letters) - 1
        while l <= r:
            mid = (l + r) // 2
            if letters[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return letters[l % len(letters)]
