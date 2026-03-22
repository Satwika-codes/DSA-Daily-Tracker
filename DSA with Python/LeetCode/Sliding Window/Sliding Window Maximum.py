# PROBLEM NUMBER:239
# https://leetcode.com/problems/sliding-window-maximum/1
# 239.Sliding Window Maximum
# DIFFICULTY:HARD
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Approach:
        # We need to find the maximum element in every window of size k.
        #
        # Step 1: Use a deque to store indices of elements.
        #         The deque will store indices in decreasing order of values.
        #
        # Step 2: Traverse the array using index i.
        #
        # Step 3: Remove indices from the front of deque if they are
        #         out of the current window (i - k).
        #
        # Step 4: Maintain decreasing order in deque:
        #         • Remove indices from the back while the current element
        #           is greater than nums[dq[-1]].
        #
        # Step 5: Add the current index i to the deque.
        #
        # Step 6: Once the first window is formed (i >= k - 1),
        #         the front of the deque (dq[0]) holds the index of the
        #         maximum element of the current window.
        #
        # Step 7: Append nums[dq[0]] to the result.
        #
        # Step 8: Continue until all elements are processed and return result.
        dq = deque()   # stores indices
        result = []

        for i in range(len(nums)):

            # remove elements out of window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # remove smaller elements
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # add result when window is ready
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result