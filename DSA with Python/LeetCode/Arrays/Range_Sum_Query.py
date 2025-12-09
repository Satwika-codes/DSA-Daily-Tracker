class NumArray(object):

    def __init__(self, nums):
        # Approach:
        # 1. Create a prefix sum array where pref[i] = sum of nums[0..i-1].
        # 2. Start with pref = [0] so that calculations become easier:
        #       pref[k] = pref[k-1] + nums[k-1]
        # 3. This allows O(1) range-sum queries later.
        self.pref = [0]
        for x in nums:
            self.pref.append(self.pref[-1] + x)

    def sumRange(self, left, right):
        # To find the sum from left to right:
        # 1. Use prefix sums: sum(left..right) = pref[right+1] - pref[left]
        # 2. This works because pref[right+1] = sum of first right+1 elements.
        # 3. And pref[left] = sum of first left elements.
        # 4. Their difference gives exactly the subarray sum.
        return self.pref[right + 1] - self.pref[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)