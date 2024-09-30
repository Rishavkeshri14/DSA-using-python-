# Importing the Stack class from Python's collections module.
from collections import deque

# Function to reverse a string using a stack
def reverse_string(input_str):
    # Initialize an empty stack using deque
    stack = deque()

    # Push each character of the string into the stack
    for char in input_str:
        stack.append(char)

    # Initialize an empty string for the reversed result
    reversed_str = ""

    # Pop each character from the stack and append to the result string
    while stack:
        reversed_str += stack.pop()

    return reversed_str

# Example usage
if __name__ == "__main__":
    input_str = "babbar"
    result = reverse_string(input_str)
    print(f"Reversed string is: {result}")
