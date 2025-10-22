# PROBLEM NUMBER: 17
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 17. Letter Combinations of a Phone Number
# DIFFICULTY: MEDIUM
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # APPROACH:  
        # This solution generates all possible letter combinations that a given string of digits could represent 
        # on a phone keypad using **Depth-First Search (DFS) / Backtracking**.
        # 1. If the input `digits` string is empty, return an empty list since no combinations can be formed.  
        # 2. Define a mapping `mp` of digits (2–9) to their corresponding letters on a phone keypad.  
        # 3. Initialize an empty list `ans` to store all valid combinations.  
        # 4. Define a recursive helper function `dfs(i, cur)`:
        #    - `i` represents the current index in the `digits` string.
        #    - `cur` holds the current combination being built.
        #    - If `i` equals the length of `digits`, append the built string `cur` to `ans` (base case).
        #    - Otherwise, iterate over each character corresponding to the current digit 
        #      and recursively call `dfs` for the next index with the updated string.
        # 5. Call `dfs(0, "")` to start building combinations from the first digit.  
        # 6. Return the final list `ans` containing all combinations.
        # This backtracking approach ensures all possible combinations are explored efficiently.
        # Time Complexity: O(4^n) — each digit may map to up to 4 letters.
        # Space Complexity: O(n) — recursion depth proportional to the length of `digits`.

        if not digits:
            return []
        
        mp = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        ans = []
        
        def dfs(i, cur):
            if i == len(digits):
                ans.append(cur)
                return
            for ch in mp[digits[i]]:
                dfs(i + 1, cur + ch)
        
        dfs(0, "")
        return ans







