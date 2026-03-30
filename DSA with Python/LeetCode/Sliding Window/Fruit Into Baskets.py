# PROBLEM NUMBER:904
# https://leetcode.com/problems/fruit-into-baskets/
# 904.Fruit Into Baskets
# DIFFICULTY:MEDIUM
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        # Approach:
        # We need to find the longest subarray that contains at most 2 distinct fruits.
        #
        # This is a classic sliding window problem where we maintain a window
        # with at most 2 unique elements.
        #
        # Step 1: Use a hashmap (freq) to store count of fruits in current window.
        #
        # Step 2: Initialize two pointers:
        #         • left → start of window
        #         • right → end of window
        #
        # Step 3: Expand the window by moving right pointer:
        #         • Add fruits[right] to freq
        #
        # Step 4: If the number of distinct fruits exceeds 2:
        #         • Shrink the window from left
        #         • Decrease frequency of fruits[left]
        #         • Remove it from map if frequency becomes 0
        #         • Move left forward
        #
        # Step 5: At every step, window contains at most 2 types:
        #         • Update max_len with current window size
        #
        # Step 6: Return the maximum length found

        freq = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(fruits)):
            freq[fruits[right]] += 1

            # shrink window if more than 2 types
            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len