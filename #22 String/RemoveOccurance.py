class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Keep processing until the part is no longer found in the string s
        while len(s) > 0 and part in s:
            # Find the index of the first occurrence of part in s
            index = s.find(part)
            # Remove the part from the string s
            s = s[:index] + s[index + len(part):]
        return s

# Example usage
sol = Solution()
s = "daabcabcababc"
part = "abc"
result = sol.removeOccurrences(s, part)
print(result)  # Output: "dab"
