def to_lower_case(ch):
    """
    Converts an uppercase character to lowercase.
    """
    if 'a' <= ch <= 'z':
        return ch
    else:
        return chr(ord(ch) - ord('A') + ord('a'))

def check_palindrome(a):
    """
    Checks if the input string 'a' is a palindrome.
    """
    s = 0
    e = len(a) - 1
    
    while s <= e:
        if to_lower_case(a[s]) != to_lower_case(a[e]):
            return False
        s += 1
        e -= 1
    return True

def reverse(name):
    """
    Reverses the input string 'name' in place.
    """
    return name[::-1]

def get_length(name):
    """
    Returns the length of the input string 'name'.
    """
    return len(name)

def get_max_occ_character(s):
    """
    Returns the most frequent character in the input string 's'.
    """
    arr = [0] * 26  # Array to count occurrences of each letter
    
    # Count occurrences of each letter
    for ch in s:
        # Convert to lowercase
        ch = to_lower_case(ch)
        number = ord(ch) - ord('a')
        arr[number] += 1
    
    # Find the character with the maximum occurrences
    maxi = -1
    ans = 0
    for i in range(26):
        if arr[i] > maxi:
            maxi = arr[i]
            ans = i
    
    return chr(ord('a') + ans)

# Main execution
if __name__ == "__main__":
    # Uncomment the following lines to test the functions:
    
    # name = input("Enter your name: ")
    # print("Your name is", name)
    # length = get_length(name)
    # print("Length:", length)
    # reversed_name = reverse(name)
    # print("Reversed name is", reversed_name)
    # print("Palindrome or Not:", check_palindrome(name))
    
    s = input("Enter a string: ")
    print("Character with maximum occurrences:", get_max_occ_character(s))
