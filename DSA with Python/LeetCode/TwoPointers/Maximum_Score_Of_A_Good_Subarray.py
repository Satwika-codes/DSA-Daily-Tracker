# PROBLEM NUMBER:1793
# https://leetcode.com/problems/maximum-score-of-a-good-subarray/solution/
# 1793. Maximum Score Of A Good Subarray
# DIFFICULTY: HARD
class Solution(object):
    def maximumScore(self, nums, k):
        
        # Approach:
        # ---------
        # We use a two-pointer expansion technique starting from index k.

        # 1. Initialize two pointers `left` and `right` at index k.
        # 2. Keep track of the minimum value (`curr_min`) in the current subarray.
        # 3. The score of a subarray is:
        #       score = minimum value * length of subarray
        # 4. Expand the subarray step-by-step:
        #    - If one side is exhausted, expand on the other side.
        #    - Otherwise, expand towards the side with the larger adjacent value
        #      to keep the minimum as large as possible.
        # 5. After each expansion:
        #    - Update the current minimum.
        #    - Compute the score and update the maximum score.
        # 6. Continue expanding until the entire array is covered.

        # This greedy expansion ensures that we maximize the score
        # for subarrays that must include index k.
        

        n = len(nums)
        
        left = right = k
        curr_min = nums[k]
        max_score = curr_min
        
        while left > 0 or right < n - 1:
            # Decide which side to expand
            if left == 0:
                right += 1
            elif right == n - 1:
                left -= 1
            elif nums[left - 1] > nums[right + 1]:
                left -= 1
            else:
                right += 1
            
            curr_min = min(curr_min, nums[left], nums[right])
            max_score = max(max_score, curr_min * (right - left + 1))
        
        return max_score
