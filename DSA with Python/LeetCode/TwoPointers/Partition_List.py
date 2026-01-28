# PROBLEM NUMBER: 86
# https://leetcode.com/problems/partition-list/
# 86. Partition List
# DIFFICULTY: MEDIUM
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        # Approach:
        # The idea is to split the original linked list into two separate lists
        # while preserving the relative order of nodes.

        # 1. Create two dummy nodes:
        #    - one list (`less`) to store nodes with values less than x
        #    - another list (`greater`) to store nodes with values greater than
        #      or equal to x

        # 2. Traverse the original linked list:
        #    - If the current node's value is less than x, append it to the
        #      `less` list.
        #    - Otherwise, append it to the `greater` list.

        # 3. After traversal, terminate the `greater` list to avoid cycles.

        # 4. Connect the end of the `less` list to the head of the `greater` list.

        # 5. Return the head of the newly partitioned list.

        # Time Complexity: O(n)
        # Space Complexity: O(1)
    

        # Dummy heads
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        
        less = less_dummy
        greater = greater_dummy
        
        curr = head
        
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next
        
        # Important: avoid cycle
        greater.next = None
        
        # Connect lists
        less.next = greater_dummy.next
        
        return less_dummy.next
