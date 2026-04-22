# PROBLEM NUMBER: 735
# https://leetcode.com/problems/asteroid-collision/
# 735. Asteroid Collision
# DIFFICULTY: MEDIUM

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # Approach:
        # We simulate asteroid collisions using a stack.
        #
        # Key Idea:
        # • Positive → moving right
        # • Negative → moving left
        # • Collision only happens when:
        #     → stack top > 0 AND current < 0
        #
        # Step 1: Use a stack to store surviving asteroids
        #
        # Step 2: Traverse each asteroid:
        #
        # Step 3: While collision condition exists:
        #         • Compare sizes:
        #
        #         Case 1: stack top < |current|
        #                 → stack top explodes → pop → continue
        #
        #         Case 2: stack top == |current|
        #                 → both explode → pop → stop
        #
        #         Case 3: stack top > |current|
        #                 → current explodes → stop
        #
        # Step 4: If no collision OR current survives:
        #         → push into stack
        #
        # Step 5: Return stack

        stack = []

        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    stack.pop()
                break
            else:
                stack.append(ast)

        return stack