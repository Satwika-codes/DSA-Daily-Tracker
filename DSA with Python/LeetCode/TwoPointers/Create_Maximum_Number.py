# PROBLEM NUMBER: 321
# https://leetcode.com/problems/create-maximum-number/
# 321. Create Maximum Number
# DIFFICULTY: HARD
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        # APPROACH:
        # ---------
        # We want to create the maximum possible number of length k by picking digits
        # from nums1 and nums2 while maintaining their relative order within each array.

        # The solution works in three main steps:

        #  Pick maximum subsequence:
        #    - For any array, to pick t digits that form the maximum number,
        #      we use a monotonic decreasing stack.
        #    - We greedily remove smaller digits when a larger digit can replace them
        #      and we still have the option to drop elements.
        #    - This gives us the lexicographically largest subsequence of length t.

        #  Merge two subsequences:
        #    - Once we have subsequences from nums1 and nums2,
        #      we merge them to form the largest possible number.
        #    - At each step, we compare the remaining parts lexicographically
        #      and pick the larger one’s leading digit.

        # Try all valid splits:
        #    - We try all possible ways to split k digits between nums1 and nums2.
        #    - For each split, we:
        #        • pick the best subsequence from nums1
        #        • pick the best subsequence from nums2
        #        • merge them
        #    - Keep track of the maximum result obtained.

        # The maximum among all candidates is the answer.

        # Time Complexity:
        # - Picking subsequences: O(n)
        # - Merging: O(k) (amortized)
        # - Total: O(k * (n + m))

        # Space Complexity:
        # - O(k) for stacks and merged result.
        

        def pick_max(nums, t):
            stack = []
            drop = len(nums) - t
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:t]

        def merge(a, b):
            res = []
            while a or b:
                # lexicographical comparison of remaining parts
                if a > b:
                    res.append(a.pop(0))
                else:
                    res.append(b.pop(0))
            return res

        best = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            part1 = pick_max(nums1, i)
            part2 = pick_max(nums2, k - i)
            candidate = merge(part1[:], part2[:])
            best = max(best, candidate)

        return best
