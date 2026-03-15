class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        g = 0
        i = 0 
        n = len(nums)

        while g < len(groups) and i < n:
            group = groups[g]
            length = len(group)
            if i + length <= n and nums[i:i + length] == group:
                i += length
                g += 1
            else:
                i += 1

        return g == len(groups)