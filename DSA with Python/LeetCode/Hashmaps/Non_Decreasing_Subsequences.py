class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, path):
            if len(path) >= 2:
                res.append(path[:])

            used = set()
            for i in range(start, len(nums)):
                if (path and nums[i] < path[-1]) or nums[i] in used:
                    continue

                used.add(nums[i])
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
