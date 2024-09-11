class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Helper function to check if a character is alphanumeric
        def valid(ch: str) -> bool:
            return ch.isalnum()

        # Helper function to convert a character to lowercase
        def toLowerCase(ch: str) -> str:
            return ch.lower()

        # Helper function to check if a string is a palindrome
        def checkPalindrome(a: str) -> bool:
            s = 0
            e = len(a) - 1
            while s <= e:
                if a[s] != a[e]:
                    return False
                s += 1
                e -= 1
            return True

        # Remove non-alphanumeric characters and convert to lowercase
        temp = ''.join(toLowerCase(ch) for ch in s if valid(ch))

        # Check if the processed string is a palindrome
        return checkPalindrome(temp)

# Example usage
solution = Solution()
input_str = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(input_str))  # Output: True

input_str = "race a car"
print(solution.isPalindrome(input_str))  # Output: False
