# Importing deque from the collections module to implement a stack.
from collections import deque

# Function to reverse a string using a stack
def reverse_string(input_str):
    """
    This function takes a string as input and returns the reversed version of the string 
    by using a stack (implemented with deque).
    
    Parameters:
    input_str (str): The string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    # Initialize an empty stack using deque
    stack = deque()

    # Push each character of the string into the stack
    for char in input_str:
        stack.append(char)

    # Initialize an empty string for the reversed result
    reversed_str = ""

    # Pop each character from the stack and append it to the reversed string
    while stack:
        reversed_str += stack.pop()

    # Return the reversed string
    return reversed_str

# Example usage
if __name__ == "__main__":
    # Example string
    input_str = "babbar"
    
    # Call the function to reverse the string
    result = reverse_string(input_str)
    
    # Print the result
    print(f"Reversed string is: {result}")
