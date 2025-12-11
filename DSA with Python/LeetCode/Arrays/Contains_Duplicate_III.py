# PROBLEM NUMBER: 220
# https://leetcode.com/problems/contains-duplicate-iii/
# 220. Contains Duplicate III
# DIFFICULTY: MEDIUM
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """

        # ----------------------------------------------------
        # APPROACH — BUCKET SORT (O(n)) — BEST POSSIBLE
        # ----------------------------------------------------
        # Idea:
        # We divide the number line into buckets of size (valueDiff + 1).
        #
        # Why?
        # If two numbers differ by at most valueDiff, they will either:
        #   - fall in the SAME bucket, or
        #   - fall in NEIGHBOR buckets.
        #
        # bucket_id = num // bucketSize
        #
        # Conditions to check for “almost duplicates”:
        #   1. Same bucket
        #   2. Previous bucket
        #   3. Next bucket
        #
        # Additionally, index difference must be ≤ indexDiff.
        # We maintain a sliding window of size indexDiff using buckets.
        #
        # Time:  O(n)
        # Space: O(n)
        #
        # NOTE:
        # If valueDiff < 0, impossible to satisfy |nums[i] - nums[j]| ≤ valueDiff.
        # ----------------------------------------------------

        if valueDiff < 0:
            return False

        bucket = {}
        size = valueDiff + 1  # bucket size

        for i, num in enumerate(nums):
            bucket_id = num // size

            # Case 1: same bucket → guaranteed diff ≤ valueDiff
            if bucket_id in bucket:
                return True

            # Case 2: previous bucket
            if bucket_id - 1 in bucket and abs(num - bucket[bucket_id - 1]) <= valueDiff:
                return True

            # Case 3: next bucket
            if bucket_id + 1 in bucket and abs(num - bucket[bucket_id + 1]) <= valueDiff:
                return True

            # Insert current number into its bucket
            bucket[bucket_id] = num

            # Maintain sliding window: remove element that falls out of indexDiff range
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // size
                del bucket[old_bucket_id]

        return False
