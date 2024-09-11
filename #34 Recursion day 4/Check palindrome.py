def check_palindrome(s, i, j):
    """
    Recursively checks if the substring of s from index i to j is a palindrome.
    
    Args:
    s (str): The string to check.
    i (int): The starting index of the substring.
    j (int): The ending index of the substring.
    
    Returns:
    bool: True if the substring is a palindrome, False otherwise.
    """
    # Base case: If indices cross, the substring is a palindrome
    if i > j:
        return True

    # Check if characters at current indices are different
    if s[i] != s[j]:
        return False
    else:
        # Recursive call to check the next substring
        return check_palindrome(s, i + 1, j - 1)

def main():
    name = "BookkooB"
    
    # Call the function with the full string range
    is_palindrome = check_palindrome(name, 0, len(name) - 1)

    if is_palindrome:
        print("It's a Palindrome")
    else:
        print("It's not a Palindrome")

# Execute the main function
if __name__ == "__main__":
    main()
