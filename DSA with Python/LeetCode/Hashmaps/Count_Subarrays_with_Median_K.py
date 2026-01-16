# PROBLEM NUMBER: 1248
# https://leetcode.com/problems/count-subarrays-with-median-k/
# COUNT SUBARRAYS WITH MEDIAN K
# DIFFICULTY: HARD
class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # APPROACH:
        # 1. Find the index of k in the array, since every valid subarray
        #    must include k as its median.
        # 2. Traverse to the right of k and maintain a balance value:
        #    - +1 for numbers greater than k
        #    - -1 for numbers less than k
        #    Store the frequency of each balance in a hashmap.
        # 3. Traverse to the left of k while updating the balance similarly.
        # 4. For each left-side balance, count how many right-side balances
        #    can combine with it to produce a total balance of 0 or 1,
        #    which corresponds to valid median conditions.
        # 5. Sum all such combinations to get the final count.

        # Time Complexity:
        # - O(n)

        # Space Complexity:
        # - O(n)
        
        from collections import defaultdict

        idx = nums.index(k)

        balance = 0
        right_count = defaultdict(int)
        right_count[0] = 1

        for i in range(idx + 1, len(nums)):
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1
            right_count[balance] += 1

        res = 0
        balance = 0
        for i in range(idx, -1, -1):
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1
            res += right_count[-balance] + right_count[1 - balance]

        return res
