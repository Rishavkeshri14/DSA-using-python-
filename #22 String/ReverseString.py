class Solution:
    def reverse_string(self, s):
        """
        Reverses the given list of characters in place.
        
        :param s: List of characters to be reversed.
        """
        st = 0
        e = len(s) - 1

        # Swap characters from start to end until the middle is reached
        while st < e:
            # Swap the characters at indices st and e
            s[st], s[e] = s[e], s[st]
            # Move towards the middle
            st += 1
            e -= 1

# Example usage
if __name__ == "__main__":
    solution = Solution()
    char_list = ['h', 'e', 'l', 'l', 'o']
    print("Original list:", char_list)
    solution.reverse_string(char_list)
    print("Reversed list:", char_list)
  
