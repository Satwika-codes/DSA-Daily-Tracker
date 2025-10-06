#PROBLEM NUMBER: 33
#https://leetcode.com/problems/search-in-rotated-sorted-array/
#DIFFICULTY:Medium
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        # APPROACH:
        # This solution searches for a `target` in a rotated sorted array `nums` using a modified binary search.
        # 1. Initialize two pointers, `low` and `high`, at the start and end of the array.
        # 2. While `low` <= `high`:
        #    - Compute the middle index `mid`.
        #    - If `nums[mid]` equals the `target`, return `mid`.
        #    - Check which half of the array is properly sorted:
        #       a) If the left half (`nums[low]` to `nums[mid]`) is sorted:
        #           - If `target` lies within this half, move `high` to `mid - 1`.
        #           - Otherwise, move `low` to `mid + 1`.
        #       b) If the right half (`nums[mid]` to `nums[high]`) is sorted:
        #           - If `target` lies within this half, move `low` to `mid + 1`.
        #           - Otherwise, move `high` to `mid - 1`.
        # 3. If the loop ends without finding the target, return -1.
        # This approach efficiently handles rotated sorted arrays while maintaining O(log n) time complexity.
        """
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]==target):
                  return mid
            elif(nums[low]<=nums[mid]):
                 if(nums[low]<=target<=nums[mid]):
                     high=mid-1
                 else:
                     low=mid+1
            elif(nums[mid]<=nums[high]):
                if(nums[mid]<=target<=nums[high]):
                     low=mid+1
                else:
                   high=mid-1
        return -1