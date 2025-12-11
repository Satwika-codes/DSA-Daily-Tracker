# PROBLEM NUMBER: 599
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
# 599.Minimum Index Sum of Two Lists
# DIFFICULTY: EASY
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        # Approach:
        # We want restaurants common to both lists with the minimum index sum.
        #
        # Steps:
        # 1. Store list1 items in a map → value: index  
        #        index_map[word] = index in list1
        #
        # 2. Iterate through list2 with index j:
        #       - If list2[j] exists in index_map:
        #             compute index_sum = j + index_map[word]
        #       - Track the minimum index_sum found so far.
        #
        # 3. If we find a smaller index_sum → reset result list.
        #    If equal → append the restaurant to result.
        #
        # Time Complexity: O(n + m)  
        # Space Complexity: O(n)

        index_map = {v: i for i, v in enumerate(list1)}
        min_sum = float('inf')
        result = []

        for j, word in enumerate(list2):
            if word in index_map:
                s = j + index_map[word]

                # Found a better (smaller) index sum
                if s < min_sum:
                    min_sum = s
                    result = [word]

                # Found another restaurant with the same minimum index sum
                elif s == min_sum:
                    result.append(word)

        return result
