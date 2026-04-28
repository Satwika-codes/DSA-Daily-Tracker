# PROBLEM NUMBER:331
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
# 331. Verify Preorder Serialization of a Binary Tree
# DIFFICULTY:MEDIUM
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # Approach:
        # We validate preorder serialization of a binary tree using "slot counting".
        #
        # Key Idea:
        # Every node creates slots for its children.
        #
        # Step 1: Initialize slots = 1
        #         • Root starts with 1 available slot
        #
        # Step 2: Traverse each node in preorder
        #
        # Step 3: For every node:
        #         • Consume 1 slot (current node fills a slot)
        #         • If slots go negative → invalid serialization
        #
        # Step 4: If node is not '#':
        #         • It is a real node → adds 2 new slots (left + right child)
        #
        # Step 5: If node is '#':
        #         • It is null → adds no new slots
        #
        # Step 6: At end:
        #         • All slots must be exactly 0 for valid tree
        #
        # Insight:
        # • Real node = +2 slots
        # • Null node = +0 slots
        # • Every node consumes 1 slot

        slots = 1
        nodes = preorder.split(',')

        for node in nodes:
            slots -= 1

            if slots < 0:
                return False

            if node != '#':
                slots += 2

        return slots == 0