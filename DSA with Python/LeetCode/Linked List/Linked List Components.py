# PROBLEM NUMBER: 817
# https://leetcode.com/problems/linked-list-components/
# 817. Linked List Components
# DIFFICULTY: MEDIUM

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: Optional[ListNode]
        :type nums: List[int]
        :rtype: int
        """
        # Approach:
        # We need to count connected components formed by values in nums.
        #
        # Step 1: Convert nums into a set:
        #         • Enables O(1) lookup
        #
        # Step 2: Traverse the linked list
        #
        # Step 3: Identify end of a component:
        #         • If current node value is in set
        #         • AND next node is either:
        #             → None OR not in set
        #         • Then we found one complete component
        #
        # Step 4: Increment count for each such case
        #
        # Step 5: Continue traversal until end
        #
        # Step 6: Return total count

        num_set = set(nums)
        count = 0

        curr = head

        while curr:
            # start/end of a component (we count at the end)
            if curr.val in num_set and (not curr.next or curr.next.val not in num_set):
                count += 1

            curr = curr.next

        return count
    

