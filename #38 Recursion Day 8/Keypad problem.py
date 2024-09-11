from typing import List

class Solution:
    def __init__(self):
        # Mapping from digit to corresponding letters
        self.mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def solve(self, digits: str, output: str, index: int, ans: List[str]) -> None:
        # Base case: if the index is beyond the length of digits, add the output to the answer list
        if index >= len(digits):
            ans.append(output)
            return
        
        # Get the digit and corresponding letters
        number = int(digits[index])
        value = self.mapping[number]
        
        # Iterate through each letter in the mapped value
        for char in value:
            # Add the current letter to the output string
            output += char
            # Recursive call with the next index
            self.solve(digits, output, index + 1, ans)
            # Backtrack by removing the last letter added
            output = output[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        # If input is empty, return an empty list
        if not digits:
            return []
        
        ans = []
        # Start recursive solving from index 0 with an empty output
        self.solve(digits, "", 0, ans)
        return ans

# Example usage:
sol = Solution()
print(sol.letterCombinations("23"))  # Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
